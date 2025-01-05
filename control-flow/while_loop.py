# sum up numbers from user input and termniates when user enters 0
numbers = input("enter a list of numbers seperated by space: ")

# convert the input in to a list
new_number_list = numbers.split()

# covert list items to integers
updated_number_list = []
for num in new_number_list:
    updated_number_list.append(int(num))

# sum up the input in the updated list
total = sum(updated_number_list)
print("Here is the list of numbers you entered: {}".format(updated_number_list))
print("Here is the sum of all numbers in the list: {}".format(total))