import data
import cashier
import sandwich_maker

from sandwich_maker import SandwichMaker
from cashier import Cashier


# Make an instance of other classes here
resources = data.resources
recipes = data.recipes
sandwich_maker_instance = SandwichMaker(resources)
cashier_instance = Cashier()

#check
#process
#transaction
#make


def main():
    input('Hit enter to view available resources')


    rando = input("What sandwich do you want? type '1' for S, '2' for M, '3' for L")
    sandwich_maker_instance.check_resources(rando)
    cashier_instance.process_coins(rando)
    cashier_instance.transaction_result(resources,rando)
    sandwich_maker_instance.make_sandwich(rando)

    input('Hit enter to view available resources')
    rando = input("What sandwich do you want? type '1' for S, '2' for M, '3' for L")
    sandwich_maker_instance.check_resources(rando)
    cashier_instance.process_coins(rando)
    cashier_instance.transaction_result(resources, rando)
    sandwich_maker_instance.make_sandwich(rando)

    input('Hit enter to view available resources')
    rando = input("What sandwich do you want? type '1' for S, '2' for M, '3' for L")
    sandwich_maker_instance.check_resources(rando)
    cashier_instance.process_coins(rando)
    cashier_instance.transaction_result(resources, rando)
    sandwich_maker_instance.make_sandwich(rando)

    input('Hit enter to view available resources')
    rando = input("What sandwich do you want? type '1' for S, '2' for M, '3' for L")
    sandwich_maker_instance.check_resources(rando)
    cashier_instance.process_coins(rando)
    cashier_instance.transaction_result(resources, rando)
    sandwich_maker_instance.make_sandwich(rando)

    input('Hit enter to view available resources')
    rando = input("What sandwich do you want? type '1' for S, '2' for M, '3' for L")
    sandwich_maker_instance.check_resources(rando)
    cashier_instance.process_coins(rando)
    cashier_instance.transaction_result(resources, rando)
    sandwich_maker_instance.make_sandwich(rando)





if __name__=="__main__":
    main()