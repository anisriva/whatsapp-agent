from enum import Enum

class TimeZone(str, Enum):
    UTC = "utc"
    EST = "est"
    IST = "ist"
    
TZ_MAP = {
    TimeZone.UTC: "UTC",
    TimeZone.EST: "America/New_York",
    TimeZone.IST: "Asia/Kolkata",
}