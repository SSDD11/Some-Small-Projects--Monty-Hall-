'''
Created on Apr 5, 2016

@author: Administrator
'''
#Make a program that runs the Monty Hall problem
#1. Establish 3 doors, and one prize token
#2. Hide the token behind one randomly picked door
#3. Prompt for user input for choice
#4. Add user choice and another random door into new list.  new list must contain winner.
#5. Present user second choice between the two.  Answer stay or switch.
import random
from random import randint



doors = [1, 2, 3]

prize = "p"

second_doors = []
tries = 0
switches = 0
wins = 0

def choose_of_three():
    x = int(randint(0, 2))
    print "secret door %s" % str(x + 1)

    choice_one = int(raw_input("Which door do you choose? 1, 2, or 3?"))
    if choice_one > 3:
        print "Sorry.  Choose 1, 2, or 3."
        choose_of_three()
    elif choice_one < 1:
        print "Sorry.  Choose 1, 2, or 3."
        choose_of_three()
    else:
        place_one = choice_one - 1
        tries += 1
        print "Your choice is: %s" % doors[place_one]
        second_doors.append(doors[place_one])
        if place_one == x and x == 0:
            second_doors.append(doors[randint(1,2)])
        elif place_one == x and x == 1:
            second_doors.append(doors[random.choice([0, 2])])
        elif place_one == x and x == 2:
            second_doors.append(doors[randint(0, 1)])
        else:
            second_doors.append(doors[x])
    
        print "Let's eliminate one wrong answer.  Your choices are: %s" % second_doors
        print "Your options are now: %s" % second_doors
        print "You chose: %s" % choice_one
    choice_two = raw_input("Would you like to switch your answer?  y/n?")
    if choice_two == "y":
        final_choice = second_doors[1]
        switches += 1  
    else:
        final_choice = choice_one
    print "Your final choice is %s" % final_choice
    print "Let's see if your choice is correct."
    print "The correct door is %s" % (x + 1)
    if final_choice == (x + 1):
        print "Congratulations!"
        try_again = raw_input("One more time? y/n")
        if try_again == "y":
            del second_doors[:]
            wins += 1
            print "Tries: %s" % str(tries)
            print "switches: %s" % str(switches)
            print "wins: %s" % str(wins)
            choose_of_three()
        else:
            print "Tries: %s" % str(tries)
            print "Switches: %s" % str(switches)
            print "wins: %s" % str(wins)
    else:
        try_again = raw_input("Sorry!  Try again? y/n")
        if try_again == "y":
            del second_doors[:]
            print "Tries: %s" % str(tries)
            print "switches: %s" % str(switches)
            print "wins: %s" % str(wins)
            choose_of_three()
        else:
            print "Tries: %s" % str(tries)
            print "switches: %s" % str(switches)
            print "wins: %s" % str(wins)

choose_of_three()


    