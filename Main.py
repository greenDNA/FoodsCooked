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
import os #import used for os.startfile() that we use to print
from programstatus import ProgramStatus
from recipe import Recipe
import functionality as f

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
def save_recipe(recipe_list):
    filename = open("recipe_class.txt", "w")#edited name from "recipe.txt"
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
def load_recipe(recipe_list):
    #As I am overhauling this function, I am thinking of taking inspiration from the store_recipe() function
    file_list = []
    filename = open("recipe_class.txt", "r")

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

#Function used as a boolean value to refer to the user agreeing to some statement
def user_confirm():
    return input().lower() == 'y'


#Function used to ask user which recipe he/she wants to modify and to make the appropriate actions thereafter
#Comprehensive function
## TODO: Have lists coupled with a numerical value beside them(perhaps through enumerate), have numbers be a second form of user-input, develop looping in the function to perform several operations and not having to reload the function as the 'user'
def recipe_edit(recipe_list):
    option_choice = None #Variable that will hold the input the user enters
    ingredient_choice = None #Variable for holding the ingredient input the user enters
    step_choice = None #Variable that follows suit like 'ingredient_choice' variable
    #print out all recipes currently in the recipe_list as a reminder
    #for recipe in recipe_list:
    for index in range(len(recipe_list)):
        #TODO Modify statement to be more clean
        print(f"({index}) - {recipe_list[index].recipe_name}")
    print("Which would you like to modify?")
    #create index for recipe_list that will enumerate, and var recipe that will hold the value of recipe_list sequentially
    for index, recipe in enumerate(recipe_list):
        #TODO Revamp this code to accept an integer or string to select recipe to have modified
        print(f"{recipe.recipe_name}? Enter Y if yes.")
        #if upper or lowercase y is entered, default to lowercase and test for a match meaning 'yes'
        if user_confirm():
            while(True): #As long as running variable is true, loop
                #print recipe contents to the terminal will provide user with contents without having to go through separate menus/options
                recipe.view()
                print("What would you like to modify?\nEnter '1' for recipe name.\nEnter '2' for ingredients.\nEnter '3' for steps.\nAnything else to exit.")
                option_choice = make_choice()
                if option_choice == '1':
                    print("What would you like to change the recipe name to?")
                    temp_name = input("> ")
                    print(f"Are you sure you want to change the name to: {temp_name}? Enter 'Y' for yes.")
                    if user_confirm():
                        recipe.recipe_name = temp_name
                        print("Name changed!")
                elif option_choice == '2':
                    while(True):
                        print("Enter '1' to change an ingredient.\nEnter '2' to add an ingredient.\nEnter '3' to remove an ingredient.")
                        ingredient_choice = make_choice()
                        if ingredient_choice == '1':
                            print(recipe.ingredients_list)
                            print("What ingredient would you like to change?")
                            temp_ingredient = input("> ")
                            if temp_ingredient in recipe.ingredients_list:
                                print(f"Modify '{temp_ingredient}' with?")
                                modify_ingredient = input("> ")
                                print(f"Are you sure you want to change '{temp_ingredient}' to '{modify_ingredient}'? Y?")
                                if user_confirm():
                                    for iter, ingredient in enumerate(recipe.ingredients_list):
                                        if temp_ingredient in ingredient:
                                            print("Changed!")
                                            recipe.ingredients_list[iter] = modify_ingredient
                                else:
                                    print("User declined to change the ingredient.")
                            else:
                                print(f"Error, '{temp_ingredient}' not in recipe.")
                        elif ingredient_choice == '2':
                            print("What ingredient would you like to add?")
                            temp_ingredient = input("> ")
                            print(f"Are you sure you want to add '{temp_ingredient}' to the ingredients?")
                            if user_confirm():
                                recipe.ingredients_list.append(temp_ingredient)
                                print("Added!")
                            else:
                                print("Okay. Nevermind.")
                        elif ingredient_choice == '3':
                            print(recipe.ingredients_list)
                            print("What ingredient would you like to remove?")
                            temp_ingredient = input("> ")
                            if temp_ingredient in recipe.ingredients_list:
                                print(f"Are you sure you would like to remove '{temp_ingredient}'? Y?")
                                if user_confirm():
                                    recipe.ingredients_list.remove(temp_ingredient)
                                    print("Removed!")
                            else:
                                print("Invalid choice. Nevermind.")
                        else:
                            print("Error, invalid choice.")
                            print("Returning from loop.")
                            break

                elif option_choice == '3':
                    while(True):
                        print("Enter '1' to change a step.\nEnter '2' to add a step.\nEnter '3' to remove a step.")
                        step_choice = make_choice()
                        if step_choice == '1':
                            print(recipe.steps_list)
                            print("What step would you like to change?")
                            temp_step = input("> ")
                            if temp_step in recipe.steps_list:
                                print(f"Modify '{temp_step}' with?")
                                modify_step = input("> ")
                                print(f"Are you sure you want to change '{temp_step}' to '{modify_step}'? Y?")
                                if user_confirm():
                                    for iter, step in enumerate(recipe.steps_list):
                                        if temp_step in step:
                                            print("Changed!")
                                            recipe.steps_list[iter] = modify_step
                                else:
                                    print("User declined to change the step.")
                            else:
                                print(f"Error, '{temp_step}' not in recipe.")
                        elif step_choice == '2':
                            print("What step would you like to add?")
                            temp_step = input("> ")
                            print(f"Are you sure you want to add '{temp_step}' to the steps?")
                            if user_confirm():
                                recipe.steps_list.append(temp_step)
                                print("Added!")
                            else:
                                print("Okay. Nevermind.")
                        elif step_choice == '3':
                            print(recipe.steps_list)
                            print("What step would you like to remove?")
                            temp_step = input("> ")
                            if temp_step in recipe.steps_list:
                                print(f"Are you sure you would like to remove '{temp_step}'? Y?")
                                if user_confirm():
                                    recipe.steps_list.remove(temp_step)
                                    print("Removed!")
                            else:
                                print("Invalid choice. Nevermind.")
                        else:
                            print("Error, invalid choice.")
                            print("Returning from loop.")
                            break
                else:
                    #when user enters a value to stop editing recipes, exit while loop
                    print("Returning from loop.")
                    break
            #end of while loop, always exited via break statement
        else:
            print("Moving onto the next element.")
    print("Complete!")

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
        #os.startfile("recipe_class.txt", "print")
        for recipe in recipe_list:
            print(f"Would you like a printout of {recipe.recipe_name}? (Y?)")
            if input() == 'y'.lower():
                recipe.print_recipe()
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
