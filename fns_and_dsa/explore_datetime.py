import datetime

def display_current_datetime():
    current_date = datetime.now()
    print(f"Current date and time: {current_date}")

def calculate_future_date():
    number_of_days = int(input("enter a number of days: "))
    future_date = datetime.now() + datetime.timedelta(days=number_of_days)
    print(f"Future date: {future_date}")

