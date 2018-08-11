from pantry import Pantry

class Account():
#import a library or module that handles passwords, their storage, and command line entering of passwords being hidden, as well as encrypting and decrypting the data

    def __init__(self, mode):
        self.name = None
        self.username = None
        self.pantry = None
        self.favorite_recipe = None
        self.email = None
        self.password = None
        self.backup_authentication = None
        self.security_question = None
        self.pantry = None

        if mode == 'new':
            self.create_account()
        elif mode == 'load':
            self.load_account()
        elif mode == 'express':
            pass
        else:
            pass

    def create_account(self):
        """Function to create new user accounts"""
        print("Please enter your name.")
        self.name = input("> ")
        self.pantry = Pantry()


    def load_account(self):
        """Function to load a user account that is stored locally"""
        pass
