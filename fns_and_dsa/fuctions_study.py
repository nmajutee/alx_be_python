# this function greets a user
def name_of_func():
    user_input = input('enter your name: ')
    return f'Hello, {user_input}'

#print(name_of_func())

# this function prints the full name of the user
def print_fullname(firstname, lastname):
    firstname = input('Enter you first name: ')
    lastname = input('Enter last name: ')
    fullname = firstname + ' ' + lastname
    return f'Hello, {fullname}'

#print(print_fullname('nmaju', 'terence'))

# this function prints the sum of numbers from user input
def sum_of_numbers():
    i = int(input('Enter a number: '))
    total = 0
    for i in range(0, i):
        total = total + i
    return total

#print(sum_of_numbers())

# this function calculates the weight of a user
def weight_of_body():
    mass = float(input('Enter the mass of an object: '))
    gravity = 9.81
    return round(mass * gravity, 2)

#print(weight_of_body())

# this function checks for odd numbers and returns if the number is even or odd.

def is_odd_or_even():
    x = int(input('Enter a number to check: '))
    if x / 2 == 0:
        return 'is even'
    elif x / 2 != 0:
        return 'is odd'
    else:
        return 'is not a number'
    
    
print(is_odd_or_even())

def check_number(n):
    if n % 2 == 0:
        return 'even'
    return 'odd'

print(check_number())