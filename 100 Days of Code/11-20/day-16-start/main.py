from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def Ask_for_coffee_type():
    """Asks what drink is wanted and returns the drink as a MenuItem"""
    coffee = input(f"What of the following drinks do you want:\n{Menu1.get_items()}: ")
    if coffee == "report":
        Coffee_Machine.report()
        Money1.report()
        Ask_for_coffee_type()
    coffee = Menu1.find_drink(coffee)
    if coffee is None:
        Ask_for_coffee_type()
    else:
        return coffee


def run_machine():
    drink = Ask_for_coffee_type()
    if Coffee_Machine.is_resource_sufficient(drink):
        if Money1.make_payment(drink.cost):
            Coffee_Machine.make_coffee(drink)
    use_machine_again = input("Do you want to use the machine again?\ny/n:").lower
    if use_machine_again != "n":
        run_machine()



# Define objects
Coffee_Machine = CoffeeMaker()
Menu1 = Menu()
Money1 = MoneyMachine()

#Run the machine
run_machine()