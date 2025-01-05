# find the maximim height in the list of numbers with using max() function
height = input("Enter a list of heights separated by spaces: ")
new_height = height.split()
count = 0
for i in new_height:
    count += 1
for i in range(0, count):
    new_height[i] = int(new_height[i])
max_height = 0
for i in new_height:
    if i > max_height:
        max_height = i
print(max_height)
