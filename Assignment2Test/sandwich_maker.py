import data
resources = data.resources
recipes = data.recipes


class SandwichMaker:
    def __init__(self, resources):
        self.machine_resources = resources

    def check_resources(self, ingredients):
        """Returns True when order can be made, False if ingredients are insufficient."""

        recipes[1] = recipes['small']
        recipes[2] = recipes['medium']
        recipes[3] = recipes['large']

        y = (resources["bread"])
        x = (resources["ham"])
        z = (resources["cheese"])

        self.ingredients = ingredients
        rando = self.ingredients

        bread = str(resources["bread"])
        ham = str(resources["ham"])
        cheese = str(resources["cheese"])

        print("There is " + bread + " bread slices")
        print("There is " + ham + " ham slices")
        print("There is " + cheese + " cheese slices")


        try:
            int(rando)
            type = int(rando)

            if type == 1 and y >= 2 and x >= 4 and z >= 4:
                print('Enough ingredients, small coming up')
                print('')
                return True
            elif type == 2 and y >= 4 and x >= 6 and z >= 8:
                print('Enough ingredients, medium coming up')
                print('')
                return True
            elif type == 3 and y >= 6 and x >= 8 and z >= 12:
                print('Enough ingredients, large coming up')
                print('')
                return True
            else:
                print("Not enough resources :(")
                exit()
                return False


        except ValueError:
            try:
                float(rando)
            except ValueError:
                print("This is not a number")
                print('')





    def make_sandwich(self, sandwich_size):

        user_choice = self.ingredients
        if user_choice == '1':
            resources["bread"] -= 2
            resources["ham"] -= 4
            resources["cheese"] -= 4
            print('Small sandwich is ready.Bon appetit!')
            return(resources)




        elif user_choice == '2':
            resources["bread"] -= 4
            resources["ham"] -= 6
            resources["cheese"] -= 8
            print('Medium sandwich is ready.Bon appetit!')
            return (resources)



        elif user_choice == '3':
            resources["bread"] -= 6
            resources["ham"] -= 8
            resources["cheese"] -= 12
            print('Large sandwich is ready.Bon appetit!')
            return (resources)



        else:
            print("Wrong input")