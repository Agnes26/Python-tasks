# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import math
import random

secret_number = 0
n = 0

# helper function to start and restart the game
def new_game():
    global secret_number
    secret_number = random.randrange(0, 100)
    
    # initialize global variables used in your code here

    # remove this when you add your code    
    pass


# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global secret_number
    secret_number = random.randrange(0, 100)
    global n
    n = 7

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global secret_number
    secret_number = random.randrange(0, 1000)
    global n
    n = 10
    
def input_guess(guess):
    # main game logic goes here	
    input_guess = int(guess)
    print "Guess was", input_guess
    if secret_number < input_guess:
        print "Lower"
    elif secret_number > input_guess:
        print "Higher"
    else:
        print "Correct"
    global n
    n = n - 1
    print "Number of remaining guesses is", n


    
# create frame
f = simplegui.create_frame("Guess the number",300,300)

# register event handlers for control elements and start frame
f.add_input("Guess", input_guess, 100)
f.add_button("Range is [0, 100]", range100, 200)
f.add_button("Range is [0, 1000]", range1000, 200)

# call new_game 
new_game()


# always remember to check your completed program against the grading rubric
