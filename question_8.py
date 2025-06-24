import csv


address_book = [
    ["Name", "Address", "Mobile", "Email"],
    ["Alice Smith", "123 Elm Street", "1234567890", "alice@example.com"],
    ["Bob Johnson", "456 Oak Avenue", "9876543210", "bob@example.com"]
]

with open("address_book.csv", mode="w", newline='') as file:
    writer = csv.writer(file)
    writer.writerows(address_book)

print("CSV file 'address_book.csv' created.")
