import datetime

current_date = datetime.datetime.now()
current_month = current_date.month

def test(x,y):
    print(x+y)

#add time punch/calculate hours
def hours(day,day_of_week):


    time_punch = {
    "day": day,
    "month": current_month,
    "Day_of_week": day_of_week,
    "start": 'time_start',
    "end": 'time_end',
    "hours": ''
    }

    # Input start time in HH:MM format
    start_time_str = input("Enter the start time (HH:MM): ")
    start_time = datetime.datetime.strptime(start_time_str, '%H:%M')
    time_punch["start"] = start_time.strftime('%H:%M')

    # Input end time in HH:MM format
    end_time_str = input("Enter the end time (HH:MM): ")
    end_time = datetime.datetime.strptime(end_time_str, '%H:%M')
    time_punch["end"] = end_time.strftime('%H:%M')

    # Calculate the hours worked
    work_duration = end_time - start_time

    # Extract hours from the duration
    work_hours = work_duration.total_seconds() / 3600
    hours_worked = "%.2f" % work_hours
    time_punch["hours"] = hours_worked

    # Print the start and end times and the work duration
    print(f"Started working at: {start_time.strftime('%H:%M')}")
    print(f"Finished working at: {end_time.strftime('%H:%M')}")
    print(f"Work duration: {work_duration}")
    print(f"Work hours: {hours_worked} hours")
    print(time_punch)
    return time_punch



