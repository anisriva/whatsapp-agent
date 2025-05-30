import pytz
from datetime import datetime
from pydantic import NaiveDatetime
from app.src.constants.timezone import TZ_MAP, TimeZone


def convert_naiveiso8601_to_utc_aware_timestamp(
    naive_date_time: NaiveDatetime, timezone: TimeZone
) -> str:
    tz = pytz.timezone(TZ_MAP[timezone])
    aware_time = tz.localize(naive_date_time)
    utc_time = aware_time.astimezone(pytz.UTC)
    # Return the time in ISO 8601 format with +00:00 to indicate UTC
    return utc_time.isoformat()


def convert_to_naive_datetime(date_time: datetime) -> datetime:
    if date_time.tzinfo:
        return date_time.astimezone().replace(tzinfo=None)
    return date_time


def get_epoch_time_from_timestamp(
    naive_date_time: NaiveDatetime, timezone: TimeZone
) -> float:
    utc_timestamp = convert_naiveiso8601_to_utc_aware_timestamp(naive_date_time, timezone)
    return datetime.fromisoformat(utc_timestamp).timestamp()

def convert_epoch_to_iso8601(epoch_time: int, timezone: TimeZone = TimeZone.UTC) -> str:
    tz = pytz.timezone(TZ_MAP[timezone])
    utc_time = datetime.fromtimestamp(epoch_time, tz)
    local_time = utc_time.astimezone(tz)
    # Return the time in ISO 8601 format
    return local_time.isoformat()

def get_epoch_time_from_utc_timestamp(utc_timestamp: str) -> float:
    time_split_0, time_split_1 = utc_timestamp.split(".")
    micro_seconds = time_split_1.split("Z")[0]
    updated_timestamp = f"{time_split_0}.{micro_seconds if len(micro_seconds) <= 6 else micro_seconds[:6]}Z"
    date_format = '%Y-%m-%dT%H:%M:%S.%fZ'
    #2024-10-16T11:43:09.108Z
    temp = datetime.strptime(updated_timestamp, date_format)
    return int(temp.timestamp())
