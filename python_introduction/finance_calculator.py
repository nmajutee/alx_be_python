# personal finance calculator
monthly_income = int(input('Enter your monthly income:'))
monthly_expenses = int(input('Enter your total monthly expenses:'))

# formula for calculating monthly savings
monthly_savings = monthly_income - monthly_expenses

# projected annual savings with interest
projected_savings = monthly_savings * 12 + round((monthly_savings * 12 * 0.05))

print('Your monthly savings are ${}'.format(monthly_savings))
print('Projected savings after one year, with interest, is: ${}.'.format(projected_savings))