import data
resources = data.resources
recipes = data.recipes

from sandwich_maker import SandwichMaker


class Cashier:
    def __init__(self):
        pass

    def process_coins(self,choice):
        """Returns the total calculated from coins inserted.
           Hint: include input() function here, e.g. input("how many quarters?: ")"""

        self.choice = choice
        user_choice = self.choice

        user_choice = int(user_choice)

        selection = (recipes[(user_choice)]["cost"])
        print("You chose " + str(user_choice) + " so your total is $:" + str(selection))

        dollar = input("How many dollars?: ")
        print("You inserted " + dollar + " dollar")
        dollar = int(dollar)

        half_dollar = input("How many half dollars?: ")
        half_dollar = int(half_dollar) * .25
        print("You inserted " + str(half_dollar) + " half dollar")

        quarter = input("How many quarters?: ")
        quarter = int(quarter) * .25
        print("You inserted " + str(quarter) + " quarters")

        nickel = input("How many nickels?: ")
        nickel = int(nickel) * .05
        print("You inserted " + str(nickel) + " nickel")

        total = dollar + half_dollar + quarter + nickel
        print("This is the amount of money you gave me: $")
        print(total)
        print('')

        self.total = total


    def transaction_result(self, coins, cost):
        """Return True when the payment is accepted, or False if money is insufficient.
           Hint: use the output of process_coins() function for cost input"""
        self.cost = cost

        user_choice = self.cost

        user_choice = int(user_choice)
        selection = (recipes[(user_choice)]["cost"])

        if self.total == selection:
            print('Payment accepted')
            print('')
            return True

        elif self.total > selection:
            print('Here is your change')
            change = self.total - selection
            print(change)
            print('')

        else:
            print('“Sorry, that’s not enough money.Money refunded.')
            print('')
            exit()
            return False