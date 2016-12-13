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
 * have a database where information is stored based with personalization details
 *
 *
 * @author trayvont
 *
 */

"""

"""
The function takes in a list, empty or with items with the intent of processing this list and being able to add, review, or remove elements of the list
Further, it should call a function or process requests to print to screen or transfer output into a textfile to save data
Plans to include loading saved data into the program to access data later
"""
def listProcessor(input):
    for element in input:
        print(element)

print("Welcome to FoodsCooked.py! We look forward to having you use our software and assisting in testing during the next stages of development.\n")
newList = ["Pizza", "Flour", "Water", "Milk", "Tomato Sauce", "Pepperoni", "Peppers", "Extra Cheese"]
listProcessor(newList)
