1. Initialize an empty list called `shopping_list`.

2. Create an infinite loop:
   a. Print the following menu options:
      1. Add an item
      2. Remove an item
      3. View the list
      4. Exit

   b. Prompt the user to select an option (1, 2, 3, or 4).

   c. Based on the user's input:
      - If the input is "1":
          i. Prompt the user to enter the item name.
         ii. Append the item to `shopping_list`.
        iii. Print a success message.

      - If the input is "2":
          i. Prompt the user to enter the item name.
         ii. Check if the item exists in `shopping_list`.
            - If it exists, remove the item.
              Print a success message.
            - Otherwise, print "Item not found."

      - If the input is "3":
          i. Check if `shopping_list` is empty.
            - If empty, print "The list is empty."
            - Otherwise, print each item in the list.

      - If the input is "4":
          i. Exit the loop.

      - For any other input, print "Invalid option. Please try again."
