import functions
import storage

while True:
    checker = 0
    for j in range(len(storage.products_price_quantity)):
        if storage.products_price_quantity[j][3] != 0:
            checker += 1
    if storage.total == 0 and storage.change_available == [0, 0, 0, 0] or \
            checker == 0:
        print("NEED MAINTENANCE")
        n = input()
        if n == 'srvop17':
            functions.maintenance()
    else:
        command = input("Choose a menu option (Enter a command):\n"
                        "1. Insert a banknote\n"
                        "2. Show available products\n"
                        "3. Select a product\n"
                        "4. Get the change\n")
        if command == '1':
            functions.insert_banknote()
        elif command == '2':
            functions.show_available_products()
        elif command == '3':
            functions.buy()
        elif command == '4':
            functions.get_change()
        elif command == 'srvop17':
            functions.maintenance()
        else:
            print("Error: incorrect command")
