"""Core forecasting logic for the weather forecast system."""

from __future__ import annotations

from dataclasses import dataclass
from datetime import date, timedelta
from statistics import mean
from typing import Iterable, List

from .data import CITY_WEATHER, WeatherEntry


@dataclass(frozen=True)
class DailyForecast:
    """Represents a single day's forecast."""

    date: date
    temp_c: float
    humidity: float
    condition: str


class UnknownCityError(KeyError):
    """Raised when the requested city is not present in the dataset."""

    def __init__(self, city: str) -> None:
        super().__init__(f"未找到城市: {city}")
        self.city = city


def _trend(values: Iterable[float]) -> float:
    """Return a simple linear trend based on the last two values."""

    values = list(values)
    if len(values) < 2:
        return 0.0
    return values[-1] - values[-2]


def _bounded(value: float, lower: float, upper: float) -> float:
    return max(lower, min(upper, value))


def _predict_condition(history: List[WeatherEntry]) -> str:
    """Predict the next condition based on recent observations."""

    recent = [entry["condition"] for entry in history[-3:]]
    # Prefer the most frequent condition; fall back to the latest entry.
    counts = {cond: recent.count(cond) for cond in set(recent)}
    sorted_conditions = sorted(counts.items(), key=lambda item: (-item[1], recent[::-1].index(item[0])))
    return sorted_conditions[0][0]


def forecast(city: str, days: int = 3) -> List[DailyForecast]:
    """Generate a simple forecast for the given city."""

    if city not in CITY_WEATHER:
        raise UnknownCityError(city)

    history = CITY_WEATHER[city]
    temps = [float(entry["temp_c"]) for entry in history]
    humidities = [float(entry["humidity"]) for entry in history]

    last_date: date = history[-1]["date"]
    result: List[DailyForecast] = []

    temp_trend = _trend(temps)
    humidity_trend = _trend(humidities)

    for index in range(1, days + 1):
        projected_date = last_date + timedelta(days=index)
        projected_temp = temps[-1] + temp_trend * index * 0.6
        projected_humidity = humidities[-1] + humidity_trend * index * 0.5

        # Stabilize projections using historical average.
        projected_temp = mean((projected_temp, temps[-1], mean(temps[-3:])))
        projected_humidity = mean((projected_humidity, humidities[-1], mean(humidities[-3:])))

        projected_temp = round(_bounded(projected_temp, min(temps) - 5, max(temps) + 5), 1)
        projected_humidity = round(_bounded(projected_humidity, 15, 100), 1)

        result.append(
            DailyForecast(
                date=projected_date,
                temp_c=projected_temp,
                humidity=projected_humidity,
                condition=_predict_condition(history),
            )
        )

    return result


__all__ = ["DailyForecast", "UnknownCityError", "forecast"]
