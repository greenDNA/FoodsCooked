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

class ProgramEngine():
    #constructor function. Set member variable running to True
    def __init__(self):
        self.running = True

    #alter value of running to False
    def make_False(self):
        self.running = False

    #alter value of running to True
    def make_True(self):
        self.running = True

    def get_running(self):
        return self.running

#Message printed when application begins
def main_menu():
    print("Hello! Thank you for taking your cooking serious, I am excited to help you track all of your progress as a chef!")

#Function asks for user input and returns that string which is to be used as the user's name
def get_user_name():
    return input("What might your name be?\n> ")

#Generic function used to return user input with a prompter already configured
def make_choice():
    return input("> ")

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

#Function used in tandem with recipe_menu() to logically decide what to do after recieving user input for the recipe_menu() function
def recipe_menu_choice(option, recipe_list, running):
    if option == "1":
        print("Okay, let's enter a recipe!")
        new_recipe(recipe_list)
        #return True
    elif option == "2":
        print("Okay, let's save your account!")
        running.make_False()
        print(running.get_running())
        #return running
    elif option == "3":
        print("Okay, let's edit a recipe!")
        running.make_False()
        print(running.get_running())
        #return running
    elif option == "4":
        print("Okay, let's view your recipes!")
        running.make_False()
        print(running.get_running())
        #return running
    elif option == "5":
        print("Okay, let's setup a grocery list!")
        running.make_False()
        print(running.get_running())
        #return running
    elif option == "6":
        print("Okay, let's declare a recipe your favorite!")
        running.make_False()
        print(running)
        #return running
    elif option == "7":
        print("Okay, let's print a recipe!")
        running.make_False()
        print(running.get_running())
        #return running
    elif option == "8":
        print("Okay, let's print a grocery list!")
        running.make_False()
        print(running.get_running())
        #return running
    else:
        print(f"Sorry {user}, that option does not exist.")
        running.make_False()
        print(running.get_running())
        #return running

def new_recipe(recipe_list):
    print("What recipe will you be adding today?")
    recipe_list.append(input("> "))
    print(recipe_list)
    print("\nIs what your list currently looks like.")

#Script begins

recipe_list = [] #list to hold recipes entered sequentially

running = ProgramEngine()
main_menu()
user = get_user_name()

while(running.get_running()):
    recipe_menu()
    option = make_choice()
    print(running.get_running())
    #running =
    recipe_menu_choice(option, recipe_list, running)
    print(running.get_running())
print("Goodbye!")
exit(1)
