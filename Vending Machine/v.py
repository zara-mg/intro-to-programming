# List of items available in the vending machine
items = [
    [0, 'water', 2, 50],      # [code, name, price (AED), stock]
    [1, 'coca cola', 5, 30],
    [2, 'apple juice', 4, 20],
    [3, 'lays', 3, 40],
    [4, 'takis', 6, 25],
    [5, 'KitKat', 3, 35],
    [6, 'm&ms', 4, 30]
]

is_quit = False

while not is_quit:
    print("Welcome to the vending machine")
    
    # Display items
    for i in items:
        print(f"Item Name: {i[1]} - Price: {i[2]} AED - Code: {i[0]} - Stock: {i[3]}")

    # Ask the user for the code of the item they want
    try:
        query = int(input("Enter the code number of the item you want to get: "))
    except ValueError:
        print("INVALID CODE. Please enter a valid number.")
        continue

    # Check if the code is valid
    item = None
    for i in items:
        if query == i[0]:
            item = i
            break

    if not item:
        print('INVALID CODE. Please try again.')
        continue

    # Check if the item is in stock
    if item[3] <= 0:
        print(f"Sorry, {item[1]} is out of stock.")
        continue

    # Display the selected item and ask for payment
    print(f"Great, {item[1]} will cost you {item[2]} AED.")
    
    try:
        money = float(input(f"Enter at least {item[2]} AED to purchase: "))
    except ValueError:
        print("Please enter a valid amount.")
        continue

    if money < item[2]:
        print(f"Insufficient amount. Please enter at least {item[2]} AED.")
        continue

    # Dispense the item and calculate change
    item[3] -= 1  # Reduce stock
    change = money - item[2]
    print(f"Thank you for buying! Here is your {item[1]}.")

    if change > 0:
        print(f"Your change is {change:.2f} AED.")

    # Ask if the user wants to continue or quit
    query = input("To quit the machine enter 'q'. To continue buying, enter anything: ")
    if query.lower() == 'q':
        is_quit = True

    print('')

# Allow the admin to add additional items
print("Admin: Add new items to the vending machine.")
while True:
    add_item = input("Would you like to add an item? (yes/no): ").lower()
    if add_item == 'no':
        break
    elif add_item == 'yes':
        try:
            code = int(input("Enter the item code: "))
            name = input("Enter the item name: ")
            price = float(input("Enter the item price (AED): "))
            stock = int(input("Enter the item stock: "))
            items.append([code, name, price, stock])
            print(f"Item {name} added successfully.")
        except ValueError:
            print("Invalid input. Please enter valid details.")
    else:
        print("Invalid choice. Please enter 'yes' or 'no'.")

print("Thank you for using the vending machine!")
