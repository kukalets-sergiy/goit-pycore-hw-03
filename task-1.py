from datetime import datetime


def get_days_from_today(date: str) -> int | None:
    try:
        # Parse the input date string into a datetime object
        given_date = datetime.strptime(date, "%Y-%m-%d").date()
        # Get today's date
        today = datetime.today().date()
        # Calculate the difference in days between today and the given date
        return (today - given_date).days
    except ValueError:
        # If the input date string is not in the correct format, return None
        return None

print(get_days_from_today("2020-10-09"))
