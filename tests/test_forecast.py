from datetime import date, timedelta

import pytest

from weather_app.forecast import DailyForecast, UnknownCityError, forecast


def test_forecast_returns_requested_number_of_days():
    results = forecast("北京", days=5)
    assert len(results) == 5
    assert all(isinstance(item, DailyForecast) for item in results)


def test_forecast_dates_are_consecutive():
    results = forecast("上海", days=3)
    dates = [item.date for item in results]
    assert dates == [dates[0] + timedelta(days=i) for i in range(len(dates))]


def test_forecast_unknown_city():
    with pytest.raises(UnknownCityError):
        forecast("不存在的城市")
