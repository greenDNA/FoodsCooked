from pantry import Pantry

class Account():
#import a library or module that handles passwords, their storage, and command line entering of passwords being hidden, as well as encrypting and decrypting the data
# TODO probably need to add a database to manage data, i have mysql installed
    def __init__(self, mode):
        self.name = None
        self.username = None
        self.password = None
        self.pantry = None
        self.favorite_recipe = None
        self.email = None
        self.backup_authentication = None
        self.security_question = None
        self.pantry = None
        self.passwordfilename = None #'passwords.txt' # name of password file
        self.authorized = False
        self.password_confirm = False
        self.recipefile = False

        if mode == 'new':
            self.create_account()
        elif mode == 'load':
            self.load_account()
        elif mode == 'express':
            self.express_account()
        else:
            pass

    def user_creation_wizard(self):
        """Fucntion to handle prompts to the user creation process"""
        print("Please enter your name.")
        self.name = input("Name: ")
        print("Please enter your username.")
        self.username = input("Username: ")
        while not self.password_confirm:
            print("Please enter your password.")
            self.password = input("Password: ")
            print("Please re-enter your password.")
            if self.password == input('Confirm Password: '):
                print("Password confirmed successfully.")
                self.password_confirm = True
        self.passwordfilename = self.username + '_pass.txt'
        self.recipefilename = self.username + '_recipe.txt'


    def create_account(self):
        """Function to create new user accounts"""
        self.user_creation_wizard()
        self.save_account()

        self.pantry = Pantry()
        # return to main menu looping login screen


    def load_account(self):
        """Function to load a user account that is stored locally"""
        if self.attempt_login():
            #proceed
            return
        else:
            #deny
            self.create_account()
        # return to main menu looping login screen

    def express_account(self):
        """Function with no user and accesses public recipes"""
        # check if account is guest or not if the username has a value or not
        self.username = False
        # return to main menu looping login screen


    def attempt_login(self):
        """Take a username and password and attempt the login process for authentication"""
        print("Thank you for returning. Please enter your username followed by your password.")
        self.username = input("Username: ")
        self.password = input("Password: ")
        self.passwordfilename = self.username + "_pass.txt"
        openfile = open(self.passwordfilename, 'r')
        for line in openfile:
            if self.username in line and self.password in line:
                print("Username and Password found. Authorizing.")
                self.authorized = True
                openfile.close()
                self.recipefilename = self.username + '_recipe.txt'
                self.name = 'unknown'
                return self.authorized
        openfile.close()
        print("Username and Password not found.")
        return self.authorized

    def save_account(self):
        """Create or overwrite a file for a particular user's credentials and save their newest data"""
        openfile = open(self.passwordfilename, 'w')
        openfile.write(self.username + '\t' + self.password)
        openfile.close()
