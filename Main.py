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
    print("2. Save account.")
    print("3. Edit recipe.")
    print("4. View recipes.")
    print("5. Setup grocery list.")
    print("6. Favorite a recipe.")
    print("7. Print a recipe.")
    print("8. Print grocery list.")
    print("0. Exit.")

#Function to take the recipes from the main list and save the elements into a text file to access later
def save_recipe(recipe_list):
    filename = open("recipe.txt", "w")
    for element in recipe_list:
        filename.write(element)
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
        print("Okay, let's save your account!")
        save_recipe(recipe_list)
    elif option == "3":
        print("Okay, let's edit a recipe!")
        recipe_edit(recipe_list)
    elif option == "4":
        print("Okay, let's view your recipes!")
        print(recipe_list)
    elif option == "5":
        print("Okay, let's setup a grocery list!")
        running.make_False()
    elif option == "6":
        print("Okay, let's declare a recipe your favorite!")
        running.make_False()
    elif option == "7":
        print("Okay, let's print a recipe!")
        running.make_False()
    elif option == "8":
        print("Okay, let's print a grocery list!")
        running.make_False()
    elif option == "9":
        recipe_menu()
    else:
        print(f"Sorry {user}, that option does not exist.")
        running.make_False()

def new_recipe(recipe_list):
    print("What recipe will you be adding today?")
    recipe_list.append(input("> "))
    print(recipe_list)
    print("\nIs what your list currently looks like.")

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
