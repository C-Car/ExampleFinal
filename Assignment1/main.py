### Data ###

recipes = {
    "small": {
        "ingredients": {
            "bread": 2,  ## slice
            "ham": 4,  ## slice
            "cheese": 4,  ## ounces
        },
        "cost": 1.75,
    },
    "medium": {
        "ingredients": {
            "bread": 4,  ## slice
            "ham": 6,  ## slice
            "cheese": 8,  ## ounces
        },
        "cost": 3.25,
    },
    "large": {
        "ingredients": {
            "bread": 6,  ## slice
            "ham": 8,  ## slice
            "cheese": 12,  ## ounces
        },
        "cost": 5.5,
    }
}

resources = {
    "bread": 12,  ## slice
    "ham": 18,  ## slice
    "cheese": 24,  ## ounces
}


### Complete functions ###


class SandwichMachine:

    def __init__(self, machine_resources):
        """Receives resources as input.
           Hint: bind input variable to self variable"""
        self.machine_resources = machine_resources

    def check_resources(self, ingredients):
        for item in ingredients:
            if ingredients[item] > self.machine_resources[item]:
                print(f"Sorry, there is not enough {item}.")
                return False
            return True

    def process_coins(self):
        print("Please insert coins.")
        total = int(input("How many dollars?")) * 1
        total += int(input("How many half dollars?")) * .5
        total += int(input("How many quarters?")) * .25
        total += int(input("How many dimes?")) * .10
        total += int(input("How many nickels?")) * .05
        total += int(input("How many pennies?")) * .01
        return total

    def transaction_result(self, coins, cost):
        if coins >= cost:
            change = round(coins - cost, 2)
            print(f"Here is ${change} in change.")
            return True
        else:
            print("Sorry, that is not enough money. You have not been charged.")
            return False

    def make_sandwich(self, sandwich_size, order_ingredients):
        for item in order_ingredients:
            self.machine_resources[item] -= order_ingredients[item]
        print(f"{sandwich_size} sandwich is ready. Enjoy!")

is_on = True

sandwich_maker = SandwichMachine(resources)

while is_on:
    choice = input("What would you like? (small/ medium/ large/ off/ report): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Bread: {resources['bread']} slice(s)")
        print(f"Ham: {resources['ham']} slice(s)")
        print(f"Cheese: {resources['cheese']} pound(s)")
    else:
        sandwich = recipes[choice]
        if sandwich_maker.check_resources(sandwich["ingredients"]):
            payment = sandwich_maker.process_coins()
            if sandwich_maker.transaction_result(payment, sandwich["cost"]):
                sandwich_maker.make_sandwich(choice, sandwich["ingredients"])
