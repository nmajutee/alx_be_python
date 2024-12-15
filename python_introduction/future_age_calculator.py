# user input age calculator
user_age = int(input("How old are you?"))
current_year = 2023
birth_year = current_year - user_age
future_year = 2050

# formula to calculate future age
future_age = future_year - birth_year
print('In 2050, you will be {} years old.'.format(future_age))