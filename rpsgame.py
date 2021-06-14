import random
class Main:
    def __init__(self):
        self.playerInput()
        self.aiShit()
        self.check()
    def aiShit(self):
        self.aiChoice = random.choice(['rock', 'paper', 'scissor'])
        print(self.aiChoice)
    def playerInput(self):
        self.playerChoice = input("Please enter input:")
        if (self.playerChoice == 'rock' or self.playerChoice == 'paper' or self.playerChoice == 'scissor'):
            self.aiShit()
            self.check()
        else:
            print("Please choose either rock, paper or scissor")
            self.playerInput()

    def check(self):
        if (self.playerChoice == self.aiChoice):
            print("Draw")
            Main()
        if (self.playerChoice == 'rock'):
            if (self.aiChoice == 'paper'):
                print("you lost")
                Main()
            if (self.aiChoice == 'scissor'):
                print("you win")
                Main()
        if (self.playerChoice == 'paper'):
            if (self.aiChoice == 'rock'):
                print("you win")
                Main()
            if (self.aiChoice == 'scissor'):
                print("you lose")
                Main()      
        if (self.playerChoice == 'scissor'):
            if (self.aiChoice == 'rock'):
                print("you lose")
                Main()
            if (self.aiChoice == 'paper'):
                print("you win")
                Main()
Main()
