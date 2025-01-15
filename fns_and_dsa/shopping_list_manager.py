def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            items_to_add = (input('enter the item(s) name (seperated by spaces): ').lower()).split()
            shopping_list.extend(items_to_add)
            print(f'updated shopping list: {shopping_list}')
            pass
        elif choice == '2':
            # Prompt for and remove an item
            items_to_remove = (input('enter name(s) to remove item(s) (seperated by spaces): ')).lower().split()
            for item in items_to_remove:
                if item in shopping_list:
                    shopping_list.remove(item)
                    print(f'{item} has been removed from the list.')
                else:
                    print(f'{item} is not in the shopping list.')
            pass
        elif choice == '3':
            # Display the shopping list
            print(shopping_list)
            pass
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()