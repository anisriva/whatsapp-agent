import pytest
from datetime import datetime
from app.src.utils.datetime import (
    convert_naiveiso8601_to_utc_aware_timestamp,
    convert_to_naive_datetime,
    get_epoch_time_from_timestamp
)
from app.src.constants.timezone import TimeZone
import pytz

def test_convert_naiveiso8601_to_utc_aware_timestamp():
    naive_date_time = datetime(2023, 10, 16, 11, 43, 9)  # Naive datetime
    timezone = TimeZone.UTC  # Assuming this is a valid entry in TZ_MAP

    # Expecting the same time but in UTC
    expected = "2023-10-16T11:43:09+00:00"
    result = convert_naiveiso8601_to_utc_aware_timestamp(naive_date_time, timezone)
    
    assert result == expected

def test_convert_to_naive_datetime_without_tzinfo():
    date_time_without_tz = datetime(2023, 10, 16, 11, 43, 9)  # Naive datetime
    result = convert_to_naive_datetime(date_time_without_tz)

    # Should return as is since it's already naive
    expected = datetime(2023, 10, 16, 11, 43, 9)
    assert result == expected
