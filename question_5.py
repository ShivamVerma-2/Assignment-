# Simple Billing Program

items = []  # List to store item prices

while True:
    print("\nBilling Menu")
    print("1. Create Bill (Add Item Price)")
    print("2. Display Item Prices and Total")
    print("3. Display Total Only")
    print("4. Exit")
    print("5.INVALID")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        price = float(input("Enter item price: "))
        items.append(price)
        print("Item added.")

    elif choice == '2':
        if not items:
            print("No items added yet.")
        else:
            print("Item Prices:")
            for i, price in enumerate(items, 1):
                print(f"Item {i}: {price}")
            print(f"Total Bill Amount: {sum(items)}")

    elif choice == '3':
        print(f"Total Bill Amount: {sum(items)}")

    elif choice == '4':
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please enter a number from 1 to 4.")
