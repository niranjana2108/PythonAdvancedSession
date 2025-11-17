from datetime import datetime, date, time
from zoneinfo import ZoneInfo


class DateTimeExamples:
    def __init__(self):
        print("=== Date & Time Examples ===")

    def show_current_datetime(self):
        """Display current system date and time"""
        now = datetime.now()
        print(f"Current datetime: {now}")

    def create_custom_datetime(self):
        """Create custom date and time objects"""
        today = date.today()
        custom_time = time(10, 30, 0)
        custom_datetime = datetime(2025, 11, 13, 14, 45)
        print(f"Today's Date: {today}")
        print(f"Custom Time: {custom_time}")
        print(f"Custom Datetime: {custom_datetime}")

    def parse_and_format(self):
        """Convert datetime <-> string"""
        now = datetime.now()
        formatted = now.strftime("%m-%Y-%d %H:%M:%S")
        parsed = datetime.strptime("13-11-2025 15:00:00", "%d-%m-%Y %H:%M:%S")
        print(f"Formatted Datetime: {formatted}")
        print(f"Parsed Datetime: {parsed}")

    def show_timezones(self):
        """Display UTC and India time"""
        utc_time = datetime.now(ZoneInfo("UTC"))
        india_time = datetime.now(ZoneInfo("Asia/Kolkata"))
        print(f"UTC Time: {utc_time}")
        print(f"India Time: {india_time}")

    def show_dst_effect(self):
        """Show daylight saving time example"""
        ny_time = datetime(2025, 3, 10, 12, 0, tzinfo=ZoneInfo("America/New_York"))
        print(f"New York Time (DST aware): {ny_time}")


if __name__ == "__main__":
    demo = DateTimeExamples()
    demo.show_current_datetime()
    demo.create_custom_datetime()
    demo.parse_and_format()
    demo.show_timezones()
    demo.show_dst_effect()
