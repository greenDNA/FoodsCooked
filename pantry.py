from shelf import Shelf

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
        for element in self.pantry_contents:
            element.print_shelf_contents()

    def print_pantry_shelves(self):
        """Function to print out names of all shelves in pantry"""
        for element in self.pantry_contents:
            print(element.shelf_name)

    def access_shelf(self, name_of_shelf):
        """Function to access a reference to a shelf and and apply operations to that specific shelf"""
        # TODO refactor
        for shelf in self.pantry_contents:
            if name_of_shelf.lower() in shelf.shelf_name.lower():
                while(self.accessing_shelf):
                    shelf.print_shelf_contents()
                    print("Below are options for the pantry shelves:\n1) - Add to Shelf\n2) - Remove from Shelf\n")
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
