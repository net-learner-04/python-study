MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

RESOURCE = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}

POWER = True
TRY = 0

def get_resource(coffee_menu, value):
    resource = 0
    if value != "cost":
        if value in MENU[coffee_menu]["ingredients"]:
            resource += MENU[coffee_menu]["ingredients"][value]
    else:
        resource += MENU[coffee_menu][value]
    return resource

def report(choice):    
    if choice == "report":
        print(f"Water: {RESOURCE["water"]}ml")
        print(f"Milk: {RESOURCE["milk"]}ml")
        print(f"Coffee: {RESOURCE["coffee"]}g")
        print(f"Money: ${RESOURCE["money"]}")
    else:
        return

def enough_resource(coffee_menu):
    if coffee_menu == "cappuccino" or coffee_menu == "latte":
        if RESOURCE["water"] < get_resource(coffee_menu, "water"):
            print("Sorry there is not enough water.")
            return False
        elif RESOURCE["milk"] < get_resource(coffee_menu, "milk"):
            print("Sorry there is not enough milk.")
            return False
        elif RESOURCE["coffee"] < get_resource(coffee_menu, "coffee"):
            print("Sorry there is not enough coffee.")
            return False
        else:
            return True
    else:
        if RESOURCE["water"] < get_resource(coffee_menu, "water"):
            print("Sorry there is not enough water.")
            return False
        elif RESOURCE["coffee"] < get_resource(coffee_menu, "coffee"):
            print("Sorry there is not enough coffee.")
            return False
        else:
            return True

def make_coffee(coffee_menu):
    if enough_resource(coffee_menu):
        if coffee_menu == "cappuccino" or coffee_menu == "latte":
            RESOURCE["water"] -= get_resource(coffee_menu, "water")
            RESOURCE["milk"] -= get_resource(coffee_menu, "milk")
            RESOURCE["coffee"] -= get_resource(coffee_menu, "coffee")
            RESOURCE["money"] += MENU[coffee_menu]["cost"]
        else:
            RESOURCE["water"] -= get_resource(coffee_menu, "water")
            RESOURCE["coffee"] -= get_resource(coffee_menu, "coffee")
            RESOURCE["money"] += MENU[coffee_menu]["cost"]
        print(f"Here is your {coffee_menu}. Enjoy!")
    else:
        return

def coin_process(coffee_menu):
    print("Please insert coins.")
    
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))
    
    calc = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    need = MENU[coffee_menu]["cost"]
    
    if need > calc:
        print("Sorry there is not enough money.")
        return
    elif need == calc:
        make_coffee(coffee_menu)
    else:
        change = calc - need
        print(f"Here is ${round(change, 2)} dollars in change.")
        make_coffee(coffee_menu)

def menu(coffee_menu):
    coin_process(coffee_menu)

while POWER:
    select = input("What would you like? (espresso/latte/cappuccino): ").lower()
    
    if select == "off":
        POWER = False
    elif select == "report":
        report(select)
    elif select in MENU:
        if enough_resource(select):
            menu(select)
    else:
        TRY += 1
        print(f"Please select a valid menu option. Tries remaining: {TRY}")
        if TRY > 3:
            POWER = False