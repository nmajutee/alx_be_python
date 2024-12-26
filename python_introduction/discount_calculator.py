initial_amount = float(input('Enter the total amount of your purchase: '))

if initial_amount <= 1000: # give a 10% discount
    applied_discount = initial_amount - (initial_amount * 0.10)
    print('You have received a 10% discount. Your new total is: {}'.format(applied_discount))
elif initial_amount > 500 and initial_amount <= 999:
    applied_discount = initial_amount - (initial_amount * 0.05)
    print('You have received a 5% discount. Your new total is: {}'.format(applied_discount))
else:
    print('No discount applied. Your total is: {}'.format(initial_amount))