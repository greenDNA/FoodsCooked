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

I got an error about Attribute when importing Main into functionality, as functionality is already imported into Main. Upon removing the Main import from functionality and moving Functions to functionality.py solved the problem. I just don't understand why python couldn't find functions defined in functionality.py

"""

# from sys import argv # I don't know if i'll need to take in command-line arguments at some point
from modules.programstatus import ProgramStatus
from modules.recipe import Recipe
from modules import functionality as f
from modules.account import Account


#Message printed when application begins
def main_menu():
    print("Hello! Thank you for taking your cooking serious, I am excited to help you track all of your progress as a chef!")

#Function asks for user input and returns that string which is to be used as the user's name
def get_user_name():
    return input("What might your name be?\n> ")

def ask_user_type():
    """Method to print to terminal a request for the user to enter if they want a new account, load an account, or to use express."""
    print("Are you a new, returning, or express user?\n1) - New\n2) - Load\n3) - Express")
    mode = input("> ")
    if mode == '1':
        return 'new'
    elif mode == '2':
        return 'load'
    else:
        return 'express'


def prompt_access_from_account():
    """Ask user to select an area of the account to examine"""
    print("Enter the number for the part of your account would you like to manage.\n1) - Recipes\n2) - Pantry")
    setting = input("Which number will you choose?\n> ")
    while setting.isnumeric() is not True:
        setting = input("Incorrect input, enter a number.\n1) - Recipes\n2) - Pantry")
    if setting == '1':
        return 'recipe'
    elif setting == '2':
        return 'pantry'
    else:
        return 'quit'



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
    #Code below this comment unnecessary
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
def save_recipe(recipe_list, recipefilename):
    #filename = open("recipe_class.txt", "w")#edited name from "recipe.txt"
    filename = open(recipefilename, "w")
    for recipe in recipe_list:
        filename.write(recipe.get_recipe_name() + '|')
        filename.write('~|') #Add tilde for uniformity
        for ingredient in recipe.get_ingredients_list():
            filename.write(ingredient + '|')
        filename.write('~|') #Need to add a second delimiter to file so I can manipulate reading from files easier on one line. Thinking of using a name over symbols to delimit
        for step in recipe.get_steps_list():
            filename.write(step + '|')
        filename.write('\n') #End of steps as above, a second delimter. Add newline after formatting
    filename.close()

#Function to take recipes from text file and load them into the main list of the script "recipe_list"
#Recipe objects are stored as a line of text, delimited by pipes(|) and tildes(~)
def load_recipe(recipe_list, recipefilename):
    #As I am overhauling this function, I am thinking of taking inspiration from the store_recipe() function
    file_list = []
    #filename = open("recipe_class.txt", "r")
    filename = open(recipefilename, "r")

    #Example formatting
    #NAME|~|INGREDIENT|INGREDIENT|INGREDIENT|INGREDIENT|~|STEP|STEP|STEP|STEP|STEP|STEP|~|

    #line is a string read in from the recipe_class.txt file
    for line in filename:
        #TODO have the instructions be cleaned up and coded neater alike the example below
        recipe = Recipe() #Creation of a new Recipe object
        final_list = [] #Represents data parsed into a completed list that can be iterated and put into variables
        counter = 0 #Controls which part of the recipe object will be modified/appended to; also resets to 0 on each new line read in from file
        file_list = line.strip('\n').split('~') #break the line into an array delimited by '~' characters as the formatting
        for split_list in file_list:
            final_list.append(split_list.strip('|').split('|'))
        for final_iter in final_list:#List of Lists to be iterated
            for element in final_iter:#List to be iterated, and we know what elements we are using by the 'counter' variable. Better solution somewhere to improve this?
                if(counter == 0):
                    recipe.recipe_name = element
                elif(counter == 1):
                    recipe.ingredients_list.append(element)
                else:
                    recipe.steps_list.append(element)
            counter += 1
        recipe.view()
        #Add new recipe object to main recipe_list, list
        recipe_list.append(recipe)
    filename.close()

#Function used to ask user which recipe he/she wants to modify and to make the appropriate actions thereafter
#Comprehensive function
## TODO: Have lists coupled with a numerical value beside them(perhaps through enumerate), have numbers be a second form of user-input, develop looping in the function to perform several operations and not having to reload the function as the 'user'
def recipe_edit(recipe_list):
    option_choice = None #Variable that will hold the input the user enters
    #ingredient_choice = None #Variable for holding the ingredient input the user enters
    #step_choice = None #Variable that follows suit like 'ingredient_choice' variable

    while(True):
        f.print_recipe_list_with_indices(recipe_list)
        print("Which would you like to modify?")
        #TODO take user input here about the index or name of the recipe to examine
        #take user input and match it to index and/or recipe_name
        recipe = f.choose_recipe(recipe_list, len(recipe_list))
        if recipe == False:
            while(recipe == False):
                print("Invalid input, try again or exit?")
                option_choice = input("Y or N?\n> ")
                if(option_choice.lower() == 'y'):
                    recipe = f.choose_recipe(recipe_list, len(recipe_list))
                else:
                    return
        #TODO Implement a line around here that handles breaking from the while loop or recipe_edit function entirely.
        #The return statement above appears to have solved the issue, but code needs cleanup still

        ##create index for recipe_list that will enumerate, and var recipe that will hold the value of recipe_list sequentially
        #for index, recipe in enumerate(recipe_list):
        #    #TODO Revamp this code to accept an integer or string to select recipe to have modified
        #    print(f"{index} - {recipe.recipe_name}? Enter Y, index, or recipe name if yes.")
        #    #if upper or lowercase y is entered, default to lowercase and test for a match meaning 'yes'
        #    if f.user_confirm():
        while(True): #As long as running variable is true, loop
            #print recipe contents to the terminal will provide user with contents without having to go through separate menus/options
            print()
            recipe.view()
            print("What would you like to modify?\nEnter '1' for recipe name.\nEnter '2' for ingredients.\nEnter '3' for steps.\nAnything else to exit.")
            option_choice = f.make_choice()
            if option_choice == '1':
                f.modify_recipe_name(recipe)
            elif option_choice == '2':
                #Script checks for values 1-3, and if user does not enter one of the values, exit loop
                f.modify_ingredients(recipe)
            elif option_choice == '3':
                #Script checks for values 1-3, and if user does not enter one of the values, exit loop
                f.modify_steps(recipe)

            else:
                #when user enters a value to stop editing recipes, exit while loop
                print("Error, invalid choice.")
                print("Returning from loop.")
                break
                #end of while loop, always exited via break statement
            #else:
            #    print("Moving onto the next element.")
        #print("Complete!")
        #if(something)
            #break
    #EndOfWhileLoop

#Function used in tandem with recipe_menu() to logically decide what to do after recieving user input for the recipe_menu() function
def recipe_menu_choice(option, recipe_list, running, recipefilename):
    if option == "1":
        print("Okay, let's enter a recipe!")
        new_recipe(recipe_list)
    elif option == "2":
        #TODO needs work on load being used twice, it'll continue to append to list, perhaps emptying or deleting list, or creating a new list would be best. A self.x_list member variable may solve that
        print("Okay, let's manage your account!")
        print("\nWhat would you like to do?")
        print("1. Save.")
        print("2. Load.")
        choice = f.make_choice()
        if choice == "1":
            save_recipe(recipe_list, recipefilename)
        elif choice == "2":
            load_recipe(recipe_list, recipefilename)
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
        #Best implemented with user account data
        running.make_False()
    elif option == "6":
        print("Okay, let's declare a recipe your favorite!")
        #set a flag or option for a recipe, member variable maybe and have that declare it as favorite
        #most relevant to user save data account
        running.make_False()
    elif option == "7":
        print("Okay, let's print a recipe!")
        #setup connection to a printer device and print one or more recipes
        #os.startfile("recipe_class.txt", "print")
        for recipe in recipe_list:
            print(f"Would you like a printout of {recipe.recipe_name}? (Y?)")
            if input() == 'y'.lower():
                recipe.print_recipe()
    elif option == "8":
        print("Okay, let's print a grocery list!")
        #draft a grocery list and print the necessary ingredients you need
        #maybe add an option for saving/loading inventory of ingredients already owned. Add and subtract those numbers with the recipe requirements so you know what you need and do not need to get. I dunno if I want to add a cooking simulator add-on eventually to this project. But if I do be able to handle: Not enough ingredients scenario. Maybe this project leads to a cooking game? RPG?
        #can only implement after writing a grocery list
        running.make_False()
    elif option == "9":
        Recipe.recipe_menu()
    else:
        print(f"Sorry {user}, that option does not exist.")
        running.make_False()

#Script begins

recipe_list = [] #list to hold recipes entered sequentially
status = ProgramStatus()
main_menu() # prints welcome message

# new user enter XXX, returning user enter XXX, or express mode which has access to a public account to view and create recipes(admin account can modify public recipes from express mode)
#if new, create a new user account, else if returning load user account
user = 'generic' #get_user_name()

while(True):
    """Inside is a loop to manage deciding on user account to select"""
    user_account = Account(ask_user_type())  # User chooses account mode. Account object created and returned
    status.account_mode = True
    #decide user mode pantry/recipes
    while(status.account_mode):
        """Deciding what part of account to access"""
        status.account_access = prompt_access_from_account()
        if status.account_access.lower() == 'pantry'.lower():
            status.running = True
            while status.running:
                user_account.pantry.print_pantry_operations()
                """All code in here accesses pantry options"""
                print("Enter '9' to print the menu again.")
                option = f.make_choice()
                user_account.pantry.pantry_menu_choice(option, status)
        elif status.account_access.lower() == 'recipe'.lower():
            status.running = True
            while status.running:
                Recipe.recipe_menu()
                """All code in here accesses recipe options"""
                print("Enter '9' to print the menu again.")
                option = f.make_choice()
                recipe_menu_choice(option, recipe_list, status, user_account.recipefilename)
        elif status.account_access.lower() == 'quit'.lower():
            """Code executed to sign-out of user account"""
            status.account_mode = False
    break
print("Goodbye!")


""" Example test code to check how the account module works with the pantry module
while(True):
    #summin
    account.pantry.create_pantry_shelf('meat')
    account.pantry.create_pantry_shelf('vegetable')
    account.pantry.access_shelf('meat')
    account.pantry.print_pantry_shelves()
    account.pantry.print_pantry_contents()
    account.pantry.remove_pantry_shelf('vegetable')
"""

#exit(1)
