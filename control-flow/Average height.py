# find the averge height with for loop. don't use sum() or len()
height = input("Enter a list of heights separated by spaces: ")
new_height = height.split()
count = 0
for i in new_height:
    count += 1
for i in range(0, count):
    new_height[i] = int(new_height[i])
total = 0
for i in new_height:
    total += i
average = round(total / count)
print(average)