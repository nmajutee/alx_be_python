# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
"""total = 0
for i in range(101):
    total = total + i
    print(total)"""

# sets in python
print(set())
print(len(set()))
A = {1, 2, 3, 4, 5, 6, 9}
B = {3, 4, 5, 8, 9}

# A n B => {3, 4, 5, 9}
# A u B => {1, 2, 3, 4, 5, 6, 8, 9}
# A / B => {1, 2, 6}
# B / A => {8}
# (A / B) u (B / A) = {1, 2, 6, 8} - Symetric difference

print(len(A))
print(len(B))

for item in A:
    print(item)

# add() method
A.add(100)
print(A)

# update() method
A.update({7, 11, 15, 25})
print(A)
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = {'tomato', 'potato', 'cabbage', 'onion', 'carrot'}
fruits.update(vegetables)
print(fruits)

# remove() method
print(A)
A.remove(25)
print(A)

# pop() method
print(A)
A.pop()
print(A)

# clear() method
"""print(A)
A.clear()
print(A)"""

# deleting a set
"""print(A)
del A
print(A)"""

# converting a list to a set
fruits = ['banana', 'orange', 'mango', 'lemon', 'banana', 'apple']
print(set(fruits))

# A n B => {3, 4, 5, 9}
# A u B => {1, 2, 3, 4, 5, 6, 8, 9}
# A / B => {1, 2, 6}
# B / A => {8}
# (A / B) u (B / A) = {1, 2, 6, 8} - Symetric difference

A = {1, 2, 3, 4, 5, 6, 9}
B = {3, 4, 5, 8, 9}
print(f'A = {A}')
print(f'B = {B}')
print(A.union(B))
print(A.intersection(B))
print(A.difference(B))
print(B.difference(A))
print(A.symmetric_difference(B))

# sets and list allows you to remove duplicate
# no duplicate items
# no order
# no indices