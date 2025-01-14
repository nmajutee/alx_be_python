# tuples
t = tuple()
print(t)

years = (2012, 2015, 2016, 2016, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025)

print(years[-2])

print(2023 in years)

start_year = 2023
for year in years:
    print(year - start_year)

# using count() method 
"""year = int(input('Enter a year to check: ') )  
print(f'how many does {year} appear in years = {years}: {years.count(year)}')"""

tp1 = (1, 2, 3)
tp2 = (4, 5, 6)
print(tp1 + tp2)

# slicing of tuples
nordic_countries = ('finland', 'sweden', 'norway', 'denmark', 'icenland')
scandinavian_countries = nordic_countries[1:4]
print(scandinavian_countries)
print(list(scandinavian_countries))

# deleting a tuple
"""del tp1
print(tp1)"""

