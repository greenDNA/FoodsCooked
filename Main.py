"""

/**
 * Goal of project is to provide a place where the user can interactively collect all the foods they have made or want to make
 * The user will also be able to store and retrieve recipes they are associated with
 * Plans to work around a GUI environment
 * Use save files where the user can sign into their account with security and have
 * the ability to recover their account in the case they forget their credentials.
 * Provide a grocery list the user can generate to know how much of a particular ingredient is needed from what they have at home
 * with dating so the user is able to track freshness of the ingredients
 *
 * Layout of foods cooked in Menu class. Further inspection of the food item will on the Menu will go through the Food class
 * and express the Ingredients to make-up said food item.
 *
 * @author trayvont
 *
 */

"""

# from sys import argv # I don't know if i'll need to take in command-line arguments at some point
import sys #import used for exit() function

#Objective of class is to manage a while loop and have functions defined later be able to modify whether or not the loop should continue or end immediately
class ProgramStatus():
    #constructor function. Set member variable running to True
    def __init__(self):
        self.running = True

    #alter value of running to False
    def make_False(self):
        self.running = False

    #alter value of running to True
    def make_True(self):
        self.running = True

    #getter function for ProgramStatus.running member variable
    def get_running(self):
        return self.running

    #setter function for ProgramStatus.running member variable
    def set_running(self, value):
        self.running = value

#Class to house all of my recipe related functionality
class Recipe():

    #Simple constructor
    def __init__(self, name):
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

#Message printed when application begins
def main_menu():
    print("Hello! Thank you for taking your cooking serious, I am excited to help you track all of your progress as a chef!")

#Function asks for user input and returns that string which is to be used as the user's name
def get_user_name():
    return input("What might your name be?\n> ")

#Generic function used to return user input with a prompter already configured
def make_choice():
    return input("Please enter the number for the option you want.\n> ")

#Function that prints to terminal all possible actions of the script, not all function, and possibly more added in future, or sub categories/menus used instead.
def recipe_menu():
    print("What would you like to do?")
    print("1. Enter recipe.")
    print("2. Account.")
    print("3. Edit recipe.")
    print("4. View recipes.")
    print("5. Setup grocery list.")
    print("6. Favorite a recipe.")
    print("7. Print a recipe.")
    print("8. Print grocery list.")
    print("0. Exit.")

#Function called when user is to add a new recipe into his or her account.
#Currently undergoing changes as Recipe() class is implemented
def new_recipe(recipe_list):
    print("What recipe will you be adding today?")
    #TODO while editing this get the recipe name then consider adding in the rest of Recipe.store_recipe() in this function
    name = input("> ")
    """
    recipe_list.append(name)
    print(recipe_list)
    print("\nIs what your list currently looks like.")
    print("-"*10)
    """
    recipe = Recipe(name)
    #test_list = [] #testing if new implementation of store_recipe() function worked, and it does
    recipe.store_recipe(recipe_list)
    for test in recipe_list:
        print(test.get_recipe_name() + "'s recipe is as follows:'")
        print("Ingredients")
        #the zip() function is built into python3 and maps xi and yi of two lists together
        for amount, ingredient in zip(test.get_ingredient_amount(), test.get_ingredients_list()):
            print("> " + amount + " " + ingredient)
        print("Steps")
        for step in test.get_steps_list():
            print("> " + step)
        print("Recipe complete.")


#Function to take the recipes from the main list and save the elements into a text file to access later
def save_recipe(recipe_list):
    #copy code from  new_recipe() temporarily
    #recipe = Recipe("Taco")
    #test_list = []
    #recipe.store_recipe(test_list)
    #end copy
    filename = open("recipe_class.txt", "w")#edited name from "recipe.txt"
    #The below code has been suggested online to just use write() since I want to add newlines or any delimiter. It is currently confusing to me to figure out how to delimit writelines(). I think I should just learn by coding right now and revisit later
    #filename.writelines(recipe_list)
    for test in recipe_list:
        filename.write(test.get_recipe_name() + '|')
        for ingredient in test.get_ingredients_list():
            filename.write(ingredient + '|')
        filename.write('~|') #Need to add a second delimiter to file so I can manipulate reading from files easier on one line. Thinking of using a name over symbols to delimit
        for step in test.get_steps_list():
            filename.write(step + '|')
        filename.write('~|') #End of steps as above, a second delimter
    filename.close()

#Function to take recipes from text file and load them into the main list of the script "recipe_list"
def load_recipe(recipe_list):
    test_list = []
    filename = open("recipe.txt", "r")

    #recipe_list = filename.readlines() #Returns a new list of each line as a string, but I want to append to the current list "recipe_list", and not use a new list
    #iterate file line by line and append the line to the list while removing newline character used as delimiter
    for recipe in filename:
        recipe_list.append(recipe.strip()) #remove newline character from being added as a character in list element strings
    filename.close()

#Function used to ask user which recipe he/she wants to modify and to make the appropriate actions thereafter
def recipe_edit(recipe_list):
    print(recipe_list)
    print("Which would you like to modify?")
    #create index for recipe_list that will enumerate, and var recipe that will hold the value of recipe_list sequentially
    for index, recipe in enumerate(recipe_list):
        print(f"{recipe}? Enter Y if yes.")
        #if upper or lowercase y is entered, default to lowercase and test for a match meaning 'yes'
        if input().lower() == "y":
            print("Enter the new recipe: ", end ="")
            #take user input and replace value at current index of recipe_list to the new string the user gives
            #TODO add a safecheck, are you sure message later on
            recipe_list[index] = input()
            break

#Function used in tandem with recipe_menu() to logically decide what to do after recieving user input for the recipe_menu() function
def recipe_menu_choice(option, recipe_list, running):
    if option == "1":
        print("Okay, let's enter a recipe!")
        new_recipe(recipe_list)
    elif option == "2":
        #TODO needs work on load being used twice, it'll continue to append to list, perhaps emptying or deleting list, or creating a new list would be best. A self.x_list member variable may solve that
        print("Okay, let's manage your account!")
        print("\nWhat would you like to do?")
        print("1. Save.")
        print("2. Load.")
        choice = make_choice()
        if choice == "1":
            save_recipe(recipe_list)
        elif choice == "2":
            load_recipe(recipe_list)
        else:
            print(f"Sorry {user}, that option does not exist.")
            running.make_False()
    elif option == "3":
        print("Okay, let's edit a recipe!")
        recipe_edit(recipe_list)
    elif option == "4":
        print("Okay, let's view your recipes!\n")
        for recipe in recipe_list:
            recipe.view()
    elif option == "5":
        print("Okay, let's setup a grocery list!")
        #How many of each ingredient do you need in the recipe
        #How many ingredients do you have
        #Compare 'pantry' with recipe and what is missing you need
        running.make_False()
    elif option == "6":
        print("Okay, let's declare a recipe your favorite!")
        #set a flag or option for a recipe, member variable maybe and have that declare it as favorite
        running.make_False()
    elif option == "7":
        print("Okay, let's print a recipe!")
        #setup connection to a printer device and print one or more recipes
        running.make_False()
    elif option == "8":
        print("Okay, let's print a grocery list!")
        #draft a grocery list and print the necessary ingredients you need
        #maybe add an option for saving/loading inventory of ingredients already owned. Add and subtract those numbers with the recipe requirements so you know what you need and do not need to get. I dunno if I want to add a cooking simulator add-on eventually to this project. But if I do be able to handle: Not enough ingredients scenario. Maybe this project leads to a cooking game? RPG?
        running.make_False()
    elif option == "9":
        recipe_menu()
    else:
        print(f"Sorry {user}, that option does not exist.")
        running.make_False()

#Script begins

recipe_list = [] #list to hold recipes entered sequentially

status = ProgramStatus()
main_menu()
user = get_user_name()
recipe_menu()

while(status.get_running()):
    print("Enter '9' to print the menu again.")
    option = make_choice()
    recipe_menu_choice(option, recipe_list, status)
print("Goodbye!")
exit(1)
