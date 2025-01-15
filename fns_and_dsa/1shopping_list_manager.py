"""Shopping List Manager"""

shopping_list = []
select_menu_option = input('enter your choice:\n 1. add item(s)\n 2. remove item(s)\n 3. view shopping list\n 4. exit\n')

# function to add items to the shopping list
def add_items_to_list():
    if select_menu_option == '1':
        
        # prompts user to enter a list of items to add
        items_to_add = (input('enter the item(s) name (seperated by spaces): ').lower()).split()
        shopping_list.append(items_to_add)
        print(f'updated shopping list: {shopping_list}')
        return 'item added successfully.'
    else:
        return 'select a valid option'

# function that removes items from the list
def remove_items_from_list():
    if select_menu_option == '2':
        # promt user to list the items to remove
        items_to_remove = (input('enter name(s) to remove item(s) (seperated by spaces): ')).lower().split()
        
        for item in items_to_remove:
            if item in shopping_list:
                shopping_list.remove(item)
                print(f'{item} has been removed from the list.')
            else:
                print(f'{item} is not in the shopping list.')
    else:
        print('invalid input')

# function that views items in the shopping list
def view_shopping_list():
    return shopping_list

# function that exists the program
def exit_program():
    return exit()