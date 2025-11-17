from datetime import datetime
from zoneinfo import ZoneInfo


class DateTimePractice:
    def __init__(self):
        print("=== Practice Exercises ===")

    def age_calculator(self):
        """Calculate age from user’s birth date"""
        try:
            birth_str = input("Enter your birth date (dd-mm-yyyy): ")
            birth_date = datetime.strptime(birth_str, "%d-%m-%Y")
            today = datetime.today()
            age_days = (today - birth_date).days
            age_years = age_days // 365
            print(f"You are approximately {age_years} years and {age_days % 365} days old.")
        except ValueError:
            print("Invalid date format. Please use dd-mm-yyyy.")

    def local_vs_utc(self):
        """Display local and UTC time with difference"""
        local_zone = ZoneInfo("Asia/Kolkata")
        utc_zone = ZoneInfo("UTC")

        local_time = datetime.now(local_zone)
        utc_time = datetime.now(utc_zone)

        diff = (local_time - utc_time).total_seconds() / 3600
        print(f"Local Time: {local_time}")
        print(f"UTC Time:   {utc_time}")
        print(f"Time difference: {diff:.1f} hours")


if __name__ == "__main__":
    app = DateTimePractice()
    app.age_calculator()
    app.local_vs_utc()
