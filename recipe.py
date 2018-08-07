#Class to house all of my recipe related functionality
class Recipe():

    #Simple constructor
    def __init__(self, name=""):
        self.recipe_name = name
        self.ingredients_list = []
        self.steps_list = []
        self.ingredient_amount = []

        print("Recipe object created.")

    #Getter function for recipe name
    def get_recipe_name(self):
        return self.recipe_name

    #Getter function for ingredients list
    def get_ingredients_list(self):
        return self.ingredients_list

    #Getter function for steps list
    def get_steps_list(self):
        return self.steps_list

    def get_ingredient_amount(self):
        return self.ingredient_amount

    #Function designed to store a proper recipe object
    def store_recipe(self, recipe_list):
        #TODO add variable "recipe_name"
        next_item = ''
        ingredient_count = 0
        step_count = 0
        print(f"What ingredients do you need for your {self.get_recipe_name()}?")
        #TODO learn how to use while loop and input statement, is it flush to get value or from input buffer? I use input(), but don't store it into a variable, so where does it go? C++ and Java have ways to access that "floating" stdin input. #        while input("Any others? 'N' to stop") != 'n'.lower():
        #loop infinitely until user chooses to stop
        while next_item != 'n'.lower():
            next_item = input("Any others? 'N' to stop.\n> ")
            if(next_item == 'n'.lower()):
                break
            self.ingredients_list.append(next_item)
            self.ingredient_amount.append(input(f"How many of {next_item}?\n> "))
            #learn to increment using loops to not need the += statement below
            ingredient_count += 1
            print(ingredient_count)
            #Closing with the comment above----------^^^^^
        next_item = ''
        print(f"What steps do you need to follow to make this {self.get_recipe_name()}?")
        while next_item != 'n'.lower():
            next_item = input("Any others? 'N' to stop.\n> ")
            if(next_item == 'n'.lower()):
                break
            self.steps_list.append(next_item)
            step_count += 1
            print(step_count)
        #TODO Anything else? Append. Anything else? Append.
        recipe_list.append(self)

    #Function to print the contents of a recipe object to the terminal
    def view(self):
        print(self.get_recipe_name())
        print(self.get_ingredients_list())
        print(self.get_steps_list())

    #Function to take string from a file holding Recipe objects and break them down into meaningful pieces of data
    def file_recipe_recover(self):
        pass

    #Function dedicated to taking a recipe and saving it to a temporary file, to then send to the operating system's printer queue. Deleting the file after submitting
    def print_recipe(self):
        tempfile = open('recipe_print.txt', 'w')
        tempfile.write('Recipe Name\n')
        tempfile.write(self.recipe_name + '\n')
        tempfile.write('Recipe Ingredients\n')
        for ingredient in self.ingredients_list:
            tempfile.write(ingredient + '\n')
        tempfile.write('Recipe Steps\n')
        for step in self.steps_list:
            tempfile.write(step + '\n')
        tempfile.close()
        os.startfile("recipe_print.txt", "print")
        #os.remove("recipe_print.txt")
#End of Recipe class
