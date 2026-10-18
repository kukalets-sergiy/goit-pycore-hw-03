from datetime import datetime, timedelta


def get_upcoming_birthdays(users: list[dict]) -> list[dict]:
    # Get today's date
    today = datetime.today().date()
    # Initialize an empty list to store upcoming birthdays
    upcoming_birthdays = []

    # Loop through each user in the provided list of users
    for user in users:
        # Parse the user's birthday string into a date object
        birthday = datetime.strptime(
            user["birthday"], "%Y.%m.%d"
        ).date()

        # Replace the year of the birthday with the current year to check if it has already occurred this year
        birthday_this_year = birthday.replace(year=today.year)

        # If the birthday has already occurred this year, set the birthday to next year
        if birthday_this_year < today:
            birthday_this_year = birthday.replace(year=today.year + 1)

        # Check if the birthday is within the next 7 days
        if 0 <= (birthday_this_year - today).days <= 6:
            # Set the congratulation date to the birthday this year
            congratulation_date = birthday_this_year

            # If the congratulation date falls on Saturday (5) or Sunday (6), move it to the next Monday
            if congratulation_date.weekday() == 5:
                congratulation_date += timedelta(days=2)
            elif congratulation_date.weekday() == 6:
                congratulation_date += timedelta(days=1)

            # Add the user's name and the congratulation date to the list of upcoming birthdays
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })

    return upcoming_birthdays

users = [
    {"name": "John Doe", "birthday": "1985.10.24"},
    {"name": "Jane Smith", "birthday": "1990.10.22"},
    {"name": "Michael Jackson", "birthday": "1968.11.22"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
