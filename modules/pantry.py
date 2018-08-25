from modules.shelf import Shelf

class Pantry():

    def __init__(self):
        self.pantry_contents = [] #a list of Shelf objects
        self.accessing_shelf = True
        self.option = None # Stores user input

    def create_pantry_shelf(self, name_of_shelf):
        """Function accepts a name argument used to create Shelf objects to add to list"""
        #Implement the list of pantry items as a dictionary
        #implement the list of pantry items as a class an arbitrary object with fields such as name, type of category, expiry date, quantity, etc
        print("DEBUG")
        self.print_pantry_shelves()
        self.pantry_contents.append(Shelf(name_of_shelf))
        print("DEBUG")
        self.print_pantry_shelves()

    def remove_pantry_shelf(self, name_of_shelf):
        """Function to delete an entire shelf"""
        print("DEBUG")
        self.print_pantry_shelves()
        for index, shelf in enumerate(self.pantry_contents):
            if name_of_shelf.lower() in shelf.shelf_name.lower():
                del self.pantry_contents[index]
                break
        print("DEBUG")
        self.print_pantry_shelves()

    def print_pantry_contents(self):
        """Function to print out all contents in the pantry"""
        print()
        for shelf in self.pantry_contents:
            shelf.print_shelf_contents()
        print()

    def print_pantry_shelves(self):
        """Function to print out names of all shelves in pantry"""
        print()
        for shelf in self.pantry_contents:
            print(shelf.shelf_name)
        print()

    def access_shelf(self, name_of_shelf):
        """Function to access a reference to a shelf and and apply operations to that specific shelf"""
        # TODO refactor
        for shelf in self.pantry_contents:
            if name_of_shelf.lower() in shelf.shelf_name.lower():
                while(self.accessing_shelf):
                    shelf.print_shelf_contents()
                    print("Below are options for the pantry shelves:\n1) - Add to Shelf\n2) - Remove from Shelf\nOther) - Exit")
                    self.option = input("> ")
                    if(self.option == '1'):
                        print("What would you like to add to the shelf?")
                        self.option = input("> ")
                        shelf.add_to_shelf(self.option)
                    elif self.option == '2':
                        print("What would you like to remove from the shelf?")
                        self.option = input("> ")
                        shelf.remove_from_shelf(self.option)
                    else:
                        self.accessing_shelf = False
                    # Add to shelf, remove from shelf,
        self.accessing_shelf = True

    def save_pantry(self):
        """Function to save pantry contents to designated user's file"""
        #filename = open("recipe_class.txt", "w")#edited name from "recipe.txt"
        # TODO edit filename line to work based on variables and not be predetermined
        filename = open("pantry_file.txt", "w")
        for shelf in self.pantry_contents:
            filename.write(shelf.shelf_name + '|')
            filename.write('~|')  # Add tilde for uniformity
            for item in shelf.contents:
                filename.write(item + '|')
            filename.write('\n')  # End of steps as above, a second delimter. Add newline after formatting
        filename.close()

    def load_pantry(self):
        """Function to load pantry contents to designated user's file"""
        # TODO edit filename line to work based on variables and not be predetermined
        # filename = open("recipe_class.txt", "r")
        filename = open("pantry_file.txt", "r")
        final_list = []
        for shelf_index, line in enumerate(filename):
            parse_line = line.strip('\n').split('~') #break the line into an array delimited by the '~', newline at end of line stripepd away
            for split_parse in parse_line:
                final_list.append(split_parse.strip('|'))
            for index, parse in enumerate(final_list):
                if index == 0:
                    self.pantry_contents.append(Shelf(parse))
                else:
                    # TODO FIX HERE
                    for number, item in enumerate(parse.strip('|').split('|')):
                        self.pantry_contents[shelf_index].contents.append(parse)
        filename.close()

    def load_recipe(recipe_list, recipefilename):

        for line in filename:
            # TODO have the instructions be cleaned up and coded neater alike the example below
            recipe = Recipe()  # Creation of a new Recipe object
            final_list = []  # Represents data parsed into a completed list that can be iterated and put into variables
            counter = 0  # Controls which part of the recipe object will be modified/appended to; also resets to 0 on each new line read in from file
            file_list = line.strip('\n').split(
                '~')  # break the line into an array delimited by '~' characters as the formatting
            for split_list in file_list:
                final_list.append(split_list.strip('|').split('|'))
            for final_iter in final_list:  # List of Lists to be iterated
                for element in final_iter:  # List to be iterated, and we know what elements we are using by the 'counter' variable. Better solution somewhere to improve this?
                    if (counter == 0):
                        recipe.recipe_name = element
                    elif (counter == 1):
                        recipe.ingredients_list.append(element)
                    else:
                        recipe.steps_list.append(element)
                counter += 1
            recipe.view()
            # Add new recipe object to main recipe_list, list
            recipe_list.append(recipe)
        filename.close()



    def print_pantry_operations(self):
        print("Pantry options.")
        print("1. Create a shelf.")
        print("2. Remove a shelf.")
        print("3. Print pantry contents.")
        print("4. Print pantry shelves.")
        print("5. Access a shelf.")
        print("6. Save shelf.")
        print("7. Load shelf.")
        print("9. Reprint pantry operations.")
        print("0. Exit menu.")
        print()

    def pantry_menu_choice(self, option, status):
        if option == "1":
            print("Okay, let's create a shelf.")
            name = input("Name of shelf: ")
            self.create_pantry_shelf(name)
        elif option == "2":
            print("Okay, let's remove a shelf.")
            name = input("What shelf would you like to remove?\nName of shelf: ")
            self.remove_pantry_shelf(name)
        elif option == "3":
            print("Okay, let's print pantry contents.")
            self.print_pantry_contents()
        elif option == "4":
            print("Okay, let's print pantry shelves")
            self.print_pantry_shelves()
        elif option == "5":
            print("Okay, let's access a shelf.")
            name = input("What shelf would you like to access?\nName of shelf: ")
            self.access_shelf(name)
        elif option == "6":
            self.save_pantry()
        elif option == "7":
            self.load_pantry()
        elif option == "9":
            self.print_pantry_operations()
        elif option == "0":
            print("Exiting from pantry operations.")
            status.running = False
        else:
            print("Sorry, that option does not exist.")
            print("Exiting from pantry operations.")
            status.running = False

