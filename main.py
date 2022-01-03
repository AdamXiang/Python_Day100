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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0
total_money = 0
quarters = 0
dimes = 0
nickles = 0
pennies = 0
machine_operating = True


def insert_coins(q, d, n, p):
    """Input how many quarters, dimes, nickles, pennies, return the total money"""
    q = float(input("how many quarters?: "))
    d = float(input("how many dimes?: "))
    n = float(input("how many nickles?: "))
    p = float(input("how many pennies?: "))
    return q * 0.25 + d * 0.1 + n * 0.05 + p * 0.01


def check_resources(coffee_want_to_buy):
    """Input the coffee that user wants to buy, check the resources whether is enough, return True or False"""
    if coffee_want_to_buy != "espresso":
        if resources["water"] < MENU[coffee_want_to_buy]["ingredients"]["water"]:
            print("Sorry there is not enough water. ")
            return False
        elif resources["milk"] < MENU[coffee_want_to_buy]["ingredients"]["milk"]:
            print("Sorry there is not enough milk. ")
            return False
        elif resources["coffee"] < MENU[coffee_want_to_buy]["ingredients"]["coffee"]:
            print("Sorry there is not enough milk. ")
            return False
        else:
            return True
    else:
        if resources["water"] < MENU[coffee_want_to_buy]["ingredients"]["water"]:
            print("Sorry there is not enough water. ")
            return False
        elif resources["coffee"] < MENU[coffee_want_to_buy]["ingredients"]["coffee"]:
            print("Sorry there is not enough milk. ")
            return False
        else:
            return True


def inventory_remains(r, cof):
    """Input the resources and coffee you want to buy, return the resources remain after buying the coffer"""
    if cof != "espresso":
        r["water"] -= MENU[cof]["ingredients"]["water"]
        r["milk"] -= MENU[cof]["ingredients"]["milk"]
        r["coffee"] -= MENU[cof]["ingredients"]["coffee"]
    else:
        r["water"] -= MENU[cof]["ingredients"]["water"]
        r["coffee"] -= MENU[cof]["ingredients"]["coffee"]


while machine_operating:
    coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if coffee == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print("Money: ${:.2f}".format(money))
    elif coffee == "off":
        machine_operating = False
    else:
        if check_resources(coffee):
            print("Please insert coins.")
            total_money = insert_coins(quarters, dimes, nickles, pennies)

            if total_money == MENU[coffee]["cost"]:
                money += total_money
                inventory_remains(resources, coffee)
                print(f"Here is your {coffee} ☕. Enjoy!")
            elif total_money > MENU[coffee]["cost"]:
                money += MENU[coffee]["cost"]
                inventory_remains(resources, coffee)
                print("Here is ${:.2f} in change.".format(total_money - MENU[coffee]['cost']))
                print(f"Here is your {coffee} ☕. Enjoy!")
            else:
                print("Sorry that's not enough money. Money refunded.")
