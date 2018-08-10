#from Main import user_confirm, make_choice
from recipe import Recipe
# Modue file used to housekeep general functionality that does not need to exist as a variable

#Generic function used to return user input with a prompter already configured
def make_choice():
    return input("Please enter the number for the option you want.\n> ")

#Function used as a boolean value to refer to the user agreeing to some statement
def user_confirm():
    return input().lower() == 'y'

def modify_recipe_name(recipe):
    """Function used to modify recipe_name value of a recipe object"""
    print("What would you like to change the recipe name to?")
    temp_name = input("> ")
    print(f"Are you sure you want to change the name to: {temp_name}? Enter 'Y' for yes.")
    if user_confirm():
        recipe.recipe_name = temp_name
        print("Name changed!")

def change_ingredient(recipe):
    """Function used to change value of an ingredient in the list to another string value"""
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

def add_ingredient(recipe):
    """Function used to add an ingredient to the recipe's list"""
    print("What ingredient would you like to add?")
    temp_ingredient = input("> ")
    print(f"Are you sure you want to add '{temp_ingredient}' to the ingredients?")
    if user_confirm():
        recipe.ingredients_list.append(temp_ingredient)
        print("Added!")
    else:
        print("Okay. Nevermind.")

def remove_ingredient(recipe):
    """Function used to remove an ingredient from the recipe's list"""
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

def modify_ingredients(recipe):
    """Function used to enter menu to modify ingredients_list in recipe object"""
    while(True):
        print("Enter '1' to change an ingredient.\nEnter '2' to add an ingredient.\nEnter '3' to remove an ingredient.")
        ingredient_choice = make_choice()
        if ingredient_choice == '1':
            change_ingredient(recipe)
        elif ingredient_choice == '2':
            add_ingredient(recipe)
        elif ingredient_choice == '3':
            remove_ingredient(recipe)
        else:
            print("Error, invalid choice.")
            print("Returning from loop.")
            break

def change_step(recipe):
    """Function used to change value of steps_list in recipe object"""
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

def add_step(recipe):
    """Function used to add a step to the list in a recipe object"""
    print("What step would you like to add?")
    temp_step = input("> ")
    print(f"Are you sure you want to add '{temp_step}' to the steps?")
    if user_confirm():
        recipe.steps_list.append(temp_step)
        print("Added!")
    else:
        print("Okay. Nevermind.")

def remove_step(recipe):
    """Function used to remove a step in a recipe object's list"""
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

def modify_steps(recipe):
    """Function used to enter menu to modify steps_list in recipe object"""
    while(True):
        print("Enter '1' to change a step.\nEnter '2' to add a step.\nEnter '3' to remove a step.")
        step_choice = make_choice()
        if step_choice == '1':
            change_step(recipe)
        elif step_choice == '2':
            add_step(recipe)
        elif step_choice == '3':
            remove_step(recipe)
        else:
            print("Error, invalid choice.")
            print("Returning from loop.")
            break

def print_recipe_list_with_indices(recipe_list):
    #print out all recipes currently in the recipe_list as a reminder
    #for recipe in recipe_list:
    for index in range(len(recipe_list)):
        #TODO Modify statement to be more clean
        print(f"({index}) - {recipe_list[index].recipe_name}")

def choose_recipe(recipe_list, length):
    """Function used to take in user input and map that value to a recipe in the main recipe_list by index, or recipe_name"""
    user_input = input('> ')
    #isdigit() only works for nonnegative integers
    if user_input.isdigit(): #and user_input in range(length):
        #user_input variable converted to integer value
        as_int = int(user_input)
        if as_int < length:
        #if user_input in range(length):
            #are you sure statement
            return recipe_list[as_int]
        elif as_int >= length:
            return False
    else:
        for index in range(length):
            #Case insensitive
            if user_input.lower() == recipe_list[index].recipe_name.lower():
                #are you sure statement
                return recipe_list[index]
        return False #Incorrect value entered
