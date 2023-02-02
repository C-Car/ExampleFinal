import data
import sandwich_maker
import cashier

resources = data.resources
recipes = data.recipes
sandwich_maker_instance = sandwich_maker.SandwichMaker(resources)
cashier_instance = cashier.Cashier()




def main():
    is_on = True

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
            if sandwich_maker_instance.check_resources(sandwich["ingredients"]):
                payment = cashier_instance.process_coins()
                if cashier_instance.transaction_result(payment, sandwich["cost"]):
                    sandwich_maker_instance.make_sandwich(choice, sandwich["ingredients"])

if __name__=="__main__":
    main()