"""Command line interface for the weather forecast system."""

from __future__ import annotations

import argparse
from typing import Iterable

from .forecast import DailyForecast, UnknownCityError, forecast


def _format_forecast(rows: Iterable[DailyForecast]) -> str:
    header = f"{'日期':<12}{'温度(°C)':>12}{'湿度(%)':>12}{'天气':>10}"
    lines = [header, "-" * len(header)]
    for row in rows:
        lines.append(f"{row.date:%Y-%m-%d}{row.temp_c:>12.1f}{row.humidity:>12.1f}{row.condition:>10}")
    return "\n".join(lines)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="基于历史数据的简单天气预报系统")
    parser.add_argument("city", help="要查询的城市名称")
    parser.add_argument("--days", type=int, default=3, help="需要预测的天数 (默认: 3)")
    return parser


def main(argv: Iterable[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(list(argv) if argv is not None else None)

    try:
        data = forecast(args.city, days=args.days)
    except UnknownCityError as error:
        parser.error(str(error))
        return 2

    print(_format_forecast(data))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
