import datetime

# Initialize an empty dictionary to store hours worked by week
weekly_hours = {}
current_week_start = None

while True:
    try:
        # Prompt for the date worked (in the format YYYY-MM-DD)
        #date_str = input("Enter the date worked (YY-MM-DD): ")
        now = datetime.date.today()
        year = (now.year)
        month = (now.month)
        day = (now.day)
        date =f"{year}-{month}-{day}"
        # Convert the date input to a datetime object
        date_str = date
        date_worked = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        print(date_worked)
        # Find the next Wednesday from the given date
        while date_worked.weekday() != 2:  # Wednesday is 2 in Python's date.weekday()
            date_worked += datetime.timedelta(days=1)

        # Check if the current week has changed
        if date_worked != current_week_start:
            if current_week_start is not None:
                total_hours = sum(weekly_hours.values())
                print("Weekly Summary for {} to {}: {:.2f} hours".format(current_week_start, date_worked - datetime.timedelta(days=1), total_hours))
            current_week_start = date_worked
            weekly_hours = {}

        # Prompt for the hours worked on that day
        hours_worked = float(input("Enter hours worked on {}: ".format(date_worked)))

        # Add the hours worked to the dictionary
        weekly_hours[date_worked] = weekly_hours.get(date_worked, 0) + hours_worked

        another_entry = input("Do you want to add more hours? (yes/no): ").lower()
        if another_entry != "yes":
            break
    except (ValueError, KeyError):
        print("Invalid input. Please try again.")

# Calculate and display the last week's summary
total_hours = sum(weekly_hours.values())
print("Weekly Summary for {} to {}: {:.2f} hours".format(current_week_start, date_worked, total_hours))

