IMPORT datetime FROM datetime module

FUNCTION display_current_datetime():
    current_date = GET current date and time using datetime.now()
    formatted_date = FORMAT current_date as "YYYY-MM-DD HH:MM:SS"
    PRINT "Current Date and Time:", formatted_date

FUNCTION calculate_future_date():
    current_date = GET current date and time using datetime.now()
    number_of_days = PROMPT user to input number of days (integer)
    future_date = current_date + timedelta(days=number_of_days)
    formatted_future_date = FORMAT future_date as "YYYY-MM-DD"
    PRINT "Future Date after", number_of_days, "days:", formatted_future_date

# Main script execution
CALL display_current_datetime()
CALL calculate_future_date()
