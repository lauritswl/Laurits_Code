# TODO: import MENU and resources
from library import MENU
from library import resources
# TODO: Create report function


def report():
    """Prints a report of the machine"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


# TODO: Check resources function


def if_enough_resources(COFFEE):
    for i in MENU[COFFEE]["ingredients"]:
        if MENU[COFFEE]["ingredients"][i] > resources[i]:
            print(f"Please refill {i}")
            return True
    return False

# TODO: Get Money Function


def get_money(COFFEE):
    """Runs an input loop and returns total money"""
    balance = MENU[COFFEE]["cost"]
    print(f"Your {COFFEE} costs {balance}$. The machine takes the following coins:")
    coins = [1, 5, 10, 25]
    for coin_worth in coins:
        amount_of_coins = int(input(f"You still need to pay {balance}$...\nHow many {coin_worth} cents do you want to input: "))
        balance -= amount_of_coins * (coin_worth/100)
        balance = round(balance, 2)
    print(f"You get back {balance}$")
    return -balance

# TODO: Create coffee function


def make_coffee(COFFEE):
    for i in MENU[COFFEE]["ingredients"]:
        resources[i] -= MENU[COFFEE]["ingredients"][i]
    print(f"Here is your {COFFEE}☕")


# TODO: run functions
run_coffee_machine = True
ask_if_end = False
while run_coffee_machine:
    coffee_type = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffee_type == "report":
        report()
    else:
        ask_if_end = if_enough_resources(COFFEE=coffee_type)
        if not ask_if_end:
            resources["money"] += get_money(COFFEE=coffee_type)
            make_coffee(COFFEE=coffee_type)
        else:
            run_coffee_machine = input("Do you want to continue using the machine? 0 for no or 1 for yes: ")

print("The final stats of the machine was:")
report()