#Objective of class is to manage a while loop and have functions defined later be able to modify whether or not the loop should continue or end immediately
class ProgramStatus():
    #constructor function. Set member variable running to True
    def __init__(self):
        self.running = True
        self.account_mode = True
        self.recipe_mode = ""
        self.grant_access = False
        self.account_access = ""

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
#End of ProgramStatus class
