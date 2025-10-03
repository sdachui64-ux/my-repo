"""Sample weather history data used for forecasting."""

from __future__ import annotations

from datetime import date, timedelta
from typing import Dict, List

WeatherEntry = Dict[str, object]

# Generate sample historical data for a few cities.
_base_date = date(2024, 4, 1)

CITY_WEATHER: Dict[str, List[WeatherEntry]] = {
    "北京": [
        {"date": _base_date + timedelta(days=offset), "temp_c": temp, "humidity": humidity, "condition": condition}
        for offset, temp, humidity, condition in [
            (0, 18.0, 35, "晴"),
            (1, 19.5, 33, "多云"),
            (2, 21.0, 30, "晴"),
            (3, 22.5, 28, "晴"),
            (4, 24.0, 27, "多云"),
            (5, 23.0, 35, "小雨"),
            (6, 24.5, 32, "多云"),
        ]
    ],
    "上海": [
        {"date": _base_date + timedelta(days=offset), "temp_c": temp, "humidity": humidity, "condition": condition}
        for offset, temp, humidity, condition in [
            (0, 20.0, 60, "阴"),
            (1, 21.0, 62, "小雨"),
            (2, 20.5, 64, "小雨"),
            (3, 22.0, 58, "多云"),
            (4, 23.5, 56, "晴"),
            (5, 24.0, 55, "晴"),
            (6, 25.0, 54, "晴"),
        ]
    ],
    "广州": [
        {"date": _base_date + timedelta(days=offset), "temp_c": temp, "humidity": humidity, "condition": condition}
        for offset, temp, humidity, condition in [
            (0, 26.0, 75, "多云"),
            (1, 27.5, 78, "雷阵雨"),
            (2, 28.0, 80, "雷阵雨"),
            (3, 29.5, 74, "多云"),
            (4, 30.0, 70, "晴"),
            (5, 31.0, 69, "晴"),
            (6, 32.0, 67, "晴"),
        ]
    ],
}
