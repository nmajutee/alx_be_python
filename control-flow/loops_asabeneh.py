countries = ['finland', 'sweden', 'denmark', 'iceland']
countries_with_land = []
countries_with_way =[]
countries_with_den = []
for i in countries:
    if 'land' in i:
        countries_with_land.append(i)
        print(f'Countries ending in "land": {countries_with_land}')
    elif 'way' in i:
        countries_with_way.append(i)
        print(f'Countries ending in "way": {countries_with_way}')
    elif 'den' in i:
        countries_with_den.append(i)
        print(f'Countries ending in "den": {countries_with_den}')
        
    else:
        break
        
# Exercise: Level 1
# 1. Iterate 0 to 10 using for loop, do the same using while loop.
# for loop

for i in range(11):
    print(i)
    
# while loop

i = 0
while i <= 10:
    print(i)
    i += 1
    
# 2. Iterate 10 to 0 using for loop, do the same using while loop.

for i in range(10, 0, -1):
    print(i)
    
i = 10
while i >= 0:
    print(i)
    i -= 1

# Write a loop that makes seven calls to print(), so we get on the output the following triangle:
n = int(input('enter a number to draw a pattern: '))
for i in range(n):
    count = 0
    for j in range(i):
        print('#', end='')
    print('#')

# Use nested loops to create the following:

n = int(input('enter a number to draw a pattern: '))
for i in range(n):
    count = 0
    while count < n:
        count +=1
        print('# ', end='')
    print('#')