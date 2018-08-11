class Shelf():
    """Class created to work with pantry.py to identify what is on the shelves"""

    def __init__(self, name):
        """Constructor assigns name argument to the Shelf object and assigns an empty list to store contents later on"""
        self.shelf_name = name # name of shelf in pantry
        self.contents = [] # list of items on shelf

    def print_shelf_contents(self):
        """Function prints list of shelf contents to terminal"""
        print(self.shelf_name + " - ", end='')
        print(self.contents)

    def add_to_shelf(self, item):
        """Function to add an item into the shelf"""
        # TODO allow items to be incremented and disallow duplicates
        # TODO are you sure statement
        print("DEBUG")
        self.print_shelf_contents()
        self.contents.append(item)
        print("DEBUG")
        self.print_shelf_contents()

    def remove_from_shelf(self, item):
        """Function to remove an item from the shelf"""
        # TODO allow for more than one item to be removed from the list. Check for item being in list, and not having a negative quantity
        # TODO are you sure statement
        print("DEBUG")
        self.print_shelf_contents()
        self.contents.remove(item)
        print("DEBUG")
        self.print_shelf_contents()
