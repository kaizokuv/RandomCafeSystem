dorder_list = []
dtotal_price = 0

sorder_list = []
stotal_price = 0

def add_to_dorder(drink, price):
    global dorder_list, dtotal_price
    dorder_list.append((drink, price))
    dtotal_price += price

def add_to_sorder(snack, price):
    global sorder_list, stotal_price
    sorder_list.append((snack, price))
    stotal_price += price

def total_price():
    return dtotal_price + stotal_price

def mainmenu():
    print("")
    print("---Main Menu---")
    print("1. View Full Menu")
    print("2. Order A Snack")
    print("3. Order A Drink")
    print("4. View Current Order and Total")
    print("5. Checkout")
    print("6. Exit")
    print("")

def cafemenu():
    print("")
    print("---Snacks---")
    print("Donuts: RM5-7")
    print("Muffins: RM7-9")
    print("Cakes: RM10-14")
    print("")
    print("---Drinks---")  
    print("Americano: RM8-RM9")
    print("Latte: RM10-RM13")
    print("Frappe: RM14-RM17")
    print("")

   # print("---Extras---")
   # print("Oreos: RM1")
   # print("Whipped Cream: RM2")
   # print("Extra Shot: RM2 Per Shot")
   # print("Chocolate Drizzle: RM3")
   # print("Caramel Drizzle: RM3")
   # print("")

    print("---Custom Drinks---")
    print("Please Choose Your Ingredients With Our Make Your Own Drinks(MYOD) Menu :D")
    print("")

def main():
    while True:
        try:
            mainmenu()
            q1 = input("Welcome, choose your option: ")

            match q1:
                case "1":
                    cafemenu()
                case "2":
                    snacks()
                case "3":
                    drinks()
                case "4":
                    overall()
                case "5":
                    checkout()
                case "6":
                    print("")
                    print("Thank you, please come again")
                    print("")
                    exit()
                case _:
                    print("Please select a valid option.")
                    print("")
        except BackToMainMenu:
            continue

def snacks():
    while True:
        print("")
        print("1. Donuts")
        print("2. Muffins")
        print("3. Cakes")
        print("4. View Menu")
        print("5. Back To Main Menu")
        q2 = input("Please choose your snack of choice:")

        match q2:
            case "1":
                donutmenu()
            case "2":
                muffinmenu()
            case "3":
                cakemenu()
            case "4":
                cafemenu()
            case "5":
                return
            case _:
                print("Please select a valid option.")
                print("")

def donutmenu():
    while True:
        print("")
        print("---Donuts---")
        print("1. Original Donut: RM5")
        print("2. Sugar Donut: RM6")
        print("3. Chocolate Donut: RM7")
        q2a = input("Please choose your donut of choice: ")

        match q2a:
            case "1":
                print("")
                print("You have ordered an Original Donut for RM5")
                add_to_sorder("Original Donut", 5)
                afterorder()
            case "2":
                print("")
                print("You have ordered a Sugar Donut for RM6")
                add_to_sorder("Sugar Donut", 6)
                afterorder()
            case "3":
                print("")
                print("You have ordered a Chocolate Donut for RM7")
                add_to_sorder("Chocolate Donut", 7)
                afterorder()
            case _:
                 print("Please select a valid option.")
                 print("")

def muffinmenu():
    while True:
        print("")
        print("---Muffins---")
        print("1. Sugar Muffin: RM7")
        print("2. Chocolate Chip Muffin: RM8")
        print("3. Banana Chocolate Muffin: RM9")
        q2b = input("Please choose your muffin of choice: ")

        match q2b:
            case "1":
                print("")
                print("You have ordered a Sugar Muffin for RM7")
                add_to_sorder("Sugar Muffin", 7)
                afterorder()
            case "2":
                print("")
                print("You have ordered a Chocolate Chip Muffin for RM8")
                add_to_sorder("Chocolate Chip Muffin", 8)
                afterorder()
            case "3":
                print("")
                print("You have ordered a Banana Chocolate Muffin for RM9")
                add_to_sorder("Banana Chocolate Muffin", 9)
                afterorder()
            case _:
                 print("Please select a valid option.")
                 print("")
def cakemenu():
    while True:
        print("")
        print("---Cakes---")
        print("1. Powdered Sugar Butter Cake: RM10")
        print("2. Chocolate Cake: RM11")
        print("3. Carrot Cake: RM12")
        print("4. Red Velvet Cake: RM13")
        print("5. Strawberry Cheesecake: RM14")
        q2c = input("Please choose your cake of choice: ")

        match q2c:
            case "1":
                print("")
                print("You have ordered a Powdered Sugar Butter Cake for RM10")
                add_to_sorder("Powdered Sugar Butter Cake", 10)
                afterorder()
            case "2":
                print("")
                print("You have ordered a Chocolate Cake for RM11")
                add_to_sorder("Chocolate Cake", 11)
                afterorder()
            case "3":
                print("")
                print("You have ordered a Carrot Cake for RM12")
                add_to_sorder("Carrot Cake", 12)
                afterorder()
            case "4":
                print("")
                print("You have ordered a Red Velvet Cake for RM13")
                add_to_sorder("Red Velvet Cake", 13)
                afterorder()
            case "5":
                print("")
                print("You have ordered a Strawberry Cheesecake for RM14")
                add_to_sorder("Strawberry Cheesecake", 14)
                afterorder()
            case _:
                 print("Please select a valid option.")
                 print("")

def drinks():
    while True:
        print("")
        print("1. Americanos")
        print("2. Lattes")
        print("3. Frappes")
        print("4. Make Your Own Drink (MYOD) Menu")
        print("5. View Menu")
        print("6. Back To Main Menu")
        q3 = input("Please choose your drink of choice:")

        match q3:
            case "1":
                americanomenu()
            case "2":
                lattemenu()
            case "3":
                frappemenu()
            case "4":
                print("This menu is currently unavailable.")
                print("")
                #myodmenu()
            case "5":
                cafemenu()
            case "6":
                return
            case _:
                print("Please select a valid option.")
                print("")

def americanomenu():
    while True:
        print("")
        print("---Americanos---")
        print("1. Original Americano: RM8")
        print("2. Caramel Americano: RM9")
        q3a = input("Please choose your americano of choice: ")

        match q3a:
            case "1":
                print("")
                print("You have ordered an Original Americano for RM8")
                add_to_dorder("Original Americano", 8)
                afterorder()
            case "2":
                print("")
                print("You have ordered a Caramel Americano for RM9")
                add_to_dorder("Caramel Americano", 9)
                afterorder()
            case _:
                 print("Please select a valid option.")
                 print("")

def lattemenu():
    while True:
        print("")
        print("---Lattes---")
        print("1. Original Latte: RM10")
        print("2. Chocolate Latte:RM11")
        print("3. Vanilla Latte: RM12")
        print("4. Caramel Latte: RM13")
        q3b = input("Please choose your latte of choice: ")
        print("")

        match q3b:
            case "1":
                print("")
                print("You have ordered an Original Latte for RM10")
                add_to_dorder("Original Latte", 10)
                afterorder()
            case "2":
                print("")
                print("You have ordered a Chocolate Latte for RM11")
                add_to_dorder("Chocolate Latte", 11)
                afterorder()
            case "3":
                print("")
                print("You have ordered a Vanilla Latte for RM12")
                add_to_dorder("Vanilla Latte", 12)
                afterorder()
            case "4":
                print("")
                print("You have ordered a Caramel Latte for RM13")
                add_to_dorder("Caramel Latte", 13)
                afterorder()
            case _:
                 print("Please select a valid option.")
                 print("")

def frappemenu():
    while True:
        print("")
        print("---Frappes---")
        print("1. Original Frappe: RM14")
        print("2. Chocolate Frappe:RM15")
        print("3. Vanilla Frappe: RM16")
        print("4. Caramel Frappe: RM17")
        q3c = input("Please choose your frappe of choice: ")
        print("")

        match q3c:
            case "1":
                print("")
                print("You have ordered an Original Frappe for RM14")
                add_to_dorder("Original Frappe", 14)
                afterorder()
            case "2":
                print("")
                print("You have ordered a Chocolate Frappe for RM15")
                add_to_dorder("Chocolate Frappe", 15)
                afterorder()
            case "3":
                print("")
                print("You have ordered a Vanilla Frappe for RM16")
                add_to_dorder("Vanilla Frappe", 16)
                afterorder()
            case "4":
                print("")
                print("You have ordered a Caramel Frappe for RM17")
                add_to_dorder("Caramel Frappe", 17)
                afterorder()
            case _:
                 print("Please select a valid option.")
                 print("")

#def myodmenu():
    #while True:
        #print("")
        #print("---Milks---")
        #print("Normal: RM3")
        #print("Almond: RM4")

def afterorder():
    while True:
        print("")
        print("---What Now?---")
        print("1. Back To Main Menu")
        print("2. View Full Menu")
        print("3. Order Another Snack")
        print("4. Order Another Drink")
        print("5. View Current Order and Total")
        print("6. Checkout")
        print("7. Exit")
        ao = input("Please select an option: ")
        print("")

        match ao:
            case "1":
                raise BackToMainMenu()
            case "2":
                cafemenu()
            case "3":
                snacks()
            case "4":
                drinks()
            case "5":
                overall()
            case "6":
                checkout()
            case "7":
                    print("")
                    print("Thank you, please come again")
                    print("")
                    exit()
            case _:
                print("Please select a valid option.")
                print("")

def overall():
    print("")
    print("---Current Order---")
    if not dorder_list and not sorder_list:
        print("No orders yet.")
    else:
        print("---Snacks---")
        for snack, price in sorder_list:
            print(f"{snack}: RM{price}")
        print("")
        print("Your current total for snacks is RM", stotal_price)
        print("")
        print("---Drinks---")
        for drink, price in dorder_list:
            print(f"{drink}: RM{price}")
        print("")
        print("Your current total for drinks is RM", dtotal_price)
        print("")
        print(f"Your current total is RM{total_price()}")
    print("")
    input("Press any key to return")

def checkout():
    global dtotal_price, stotal_price
    print("")
    print("Proceeding to checkout...")
    if not dorder_list and not sorder_list:
        print("No items to checkout.")
    else:
        print("---Final Order---")
        print("")
        print("---Food---")
        for snack, price in sorder_list:
            print(f"{snack}: RM{price}")
        print("")
        print("Your final total for snacks is RM", stotal_price)
        print("")
        print("---Drinks---")
        for drink, price in dorder_list:
            print(f"{drink}: RM{price}")
        print("")
        print("Your final total for drinks is RM", dtotal_price)
        print("")
        print("Thank you for your order!")
        print(f"Your total is RM{total_price()}")
        dorder_list.clear()
        dtotal_price = 0
        sorder_list.clear()
        stotal_price = 0
    print("")
    input("Press any key to return")

class BackToMainMenu(Exception):
    pass

if __name__ == "__main__":
    main()
