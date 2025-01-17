from datetime import datetime
from datetime import timedelta

"""function (1) shows the current date and time, and function (2) calculates a future date from user input.
    """

def display_current_datetime():
    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    return f'current date and time: {current_date}'

def calculate_future_date():
    current_date = datetime.now()
    number_of_days = int(input('Enter the number of days to add to the current date: '))
    future_date = current_date + timedelta(number_of_days)
    formatted_future_date = current_date.strftime('%Y-%m-%d')
    return f'Future date: {formatted_future_date}'

if __name__ == "__main__":
    print(display_current_datetime())
    print(calculate_future_date())
