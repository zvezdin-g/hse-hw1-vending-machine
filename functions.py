import storage


def insert_banknote():
    try:
        insert = int(input("Insert a banknote: "))
        if insert in storage.bill_types:
            sum_of_change = 10 * storage.change_available[0] + 5 * storage.change_available[1] + 2 * \
                            storage.change_available[2] + storage.change_available[3]
            change_checker = 0
            for z in storage.products_price_quantity:
                temp = storage.total + insert - z[2]
                if (0 <= temp <= sum_of_change) and (z[3] != 0):
                    change_checker += 1
            if change_checker != 0:
                storage.total += insert
                print("Your balance: %s RUB" % storage.total)
            else:
                print("Error: There is no at least one product that can be bought with the full change.")
        else:
            print("ERROR: This banknote is not acceptable")
    except ValueError:
        print("ERROR: Enter a number")


def get_change():
    if storage.total != 0:
        a, b, c, d = 0, 0, 0, 0
        # a - number of 10RUB, b - number of 5RUB
        # c - number of 2RUB, d -number of 1RUB
        change_it = storage.total
        while change_it - 10 >= 0 and storage.change_available[0] != 0:
            change_it, a = change_it - 10, a + 1
            storage.change_available[0] -= 1
        while change_it - 5 >= 0 and storage.change_available[1] != 0:
            change_it, b = change_it - 5, b + 1
            storage.change_available[1] -= 1
        while change_it - 2 >= 0 and storage.change_available[2] != 0:
            change_it, c = change_it - 2, c + 1
            storage.change_available[2] -= 1
        while change_it - 1 >= 0 and storage.change_available[3] != 0:
            change_it, d = change_it - 1, d + 1
            storage.change_available[3] -= 1
        summary = 10 * a + 5 * b + 2 * c + d
        if summary == storage.total:
            print("Here is your change: %s RUB\nNumber of coins 10 RUB: %s\n"
                  "Number of coins 5 RUB: %s\nNumber of coins 2 RUB: %s\n"
                  "Number of coins 1 RUB: %s" % (storage.total, a, b, c, d))
            storage.total = 0
        else:
            print("Error: there are no enough change available")
    else:
        print("Error: Your balance is 0 RUB")


def show_available_products():
    print("*************** All products that are currently present ****************")
    for k in ["№", "Name", "Price", "Quantity"]:
        print("%-20s" % k, end='')
    print(" ")
    for rows in storage.products_price_quantity:
        if rows[3] > 0:
            for cells in rows:
                print("%-20s" % cells, end='')
            print(" ")
    print("************************************************************************")


def buy():
    try:
        list_of_available_prices = []
        for i in range(len(storage.products_price_quantity)):
            if storage.products_price_quantity[i][3] > 0:
                list_of_available_prices.append(storage.products_price_quantity[i][2])
        minimum = min(list_of_available_prices)
        if storage.total >= minimum:
            print("*** All products that are present and can be bought with the current credit. ***")
            for k in ["№", "Name", "Price", "Quantity"]:
                print("%-20s" % k, end='')
            print(" ")
            for rows in storage.products_price_quantity:
                if rows[3] > 0 and rows[2] <= storage.total:
                    for cells in rows:
                        print("%-20s" % cells, end='')
                    print(" ")
            print("********************************************************************************")
            number = int(input("Enter a product's number (№): "))
            if 1 <= number <= 6:
                if storage.products_price_quantity[number - 1][3] != 0:
                    sum_of_change = 10 * storage.change_available[0] + 5 * storage.change_available[1] + 2 * \
                                    storage.change_available[2] + storage.change_available[3]
                    if 0 <= storage.total - storage.products_price_quantity[number - 1][2] <= sum_of_change:
                        storage.total = storage.total - storage.products_price_quantity[number - 1][2]
                        storage.products_price_quantity[number - 1][3] -= 1
                        print("You've bought %s. Price: %s RUB. Your balance: %s RUB" %
                              (storage.products_price_quantity[number - 1][1],
                               storage.products_price_quantity[number - 1][2],
                               storage.total))
                    else:
                        print(
                            "Sorry, the change can't be dispensed with available coins or you don't have money to buy "
                            "this product")
                else:
                    print("Error: 0 items left")
            else:
                print("Error: Choose number from the list")
        else:
            print("Error: Your balance is only %s RUB. Use command 1 to insert a banknote." % storage.total)
    except ValueError:
        print("Error: Enter a number")


def maintenance():
    print("***************** SERVICE MENU *****************************************")
    for m in range(len(storage.products_price_quantity)):
        storage.products_price_quantity[m][3] = 15
    print("The remaining quantity of all products was set to maximum")
    storage.change_available = [400, 400, 400, 400]
    print("The remaining amount of each coin denomination was set to maximum")
    print("The number of banknotes in the cash accepting module: %s" % storage.total)
    storage.total = 0
    print("The number of banknotes in the cash accepting module was reset")
    print("************************************************************************")
    press_any_key = input("Press any key to return back to main menu")
