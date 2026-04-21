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

profit = 0
off = False

def is_resource_sufficient(drink_ingredients):
   for item in drink_ingredients:
       if drink_ingredients[item] >= resources[item]:
           print(f"Sorry there is not enough {item}")
           return False
   return True


def process_coins():
    quarters = float(input("How many quarters: "))
    dimes = float(input("How many dimes: "))
    nickles = float(input("How many nickles: "))
    pennies = float(input("How many pennies: "))
    quarter = 0.25
    dime = 0.10
    nickle = 0.05
    pennie = 0.01
    total = (quarters * quarter) + (dimes * dime) + (nickles * nickle) + (pennies * pennie)
    return total

def is_transaction_successful(money_received, drink_cost):
    if money_received < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = round(money_received - drink_cost, 2)
        print(f"Here is the remaining ${change} in change.")
        global profit
        profit += drink_cost
        return True


def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name}☕")

while not off:
    coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffee == "off":
        off = True
    elif coffee == "report":
       print(f"Water: {resources["water"]}ml")
       print(f"Milk: {resources["milk"]}ml")
       print(f"Coffee: {resources["coffee"]}g")
       print(f"Money: ${profit}")
    else:
        drink = MENU[coffee]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(coffee, drink["ingredients"])
