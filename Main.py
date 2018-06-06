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
def recipe_menu_choice(option):
    if option == "1":
        print("Okay, let's enter a recipe!")
    elif option == "2":
        print("Okay, let's save your account!")
    elif option == "3":
        print("Okay, let's edit a recipe!")
    elif option == "4":
        print("Okay, let's view your recipes!")
    elif option == "5":
        print("Okay, let's setup a grocery list!")
    elif option == "6":
        print("Okay, let's declare a recipe your favorite!")
    elif option == "7":
        print("Okay, let's print a recipe!")
    elif option == "8":
        print("Okay, let's print a grocery list!")
    else:
        print(f"Sorry {user}, that option does not exist.")

#Script begins

main_menu()
user = get_user_name()
recipe_menu()
option = make_choice()
recipe_menu_choice(option)

exit(1)
