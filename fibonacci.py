'''
Created on Apr 6, 2016

@author: Administrator
'''
#The Fibonacci sequence
#Each integer in the sequence is the sum of the previous two integers

#Example:  1, 1, 2, 3, 5, 8, 13, 21...

#What is a factorial
from math import factorial
def fact():
    n = int(raw_input("Feed me an integer:  "))
    if n == 1:
        return 1
    else:
        print n * factorial(n - 1)
#fact()

#The Fibonacci Sequence.  Enter how many iterations you want.
def fibb():
    f = [1, 1]
    x = len(f) - 1
    y = x - 1
    ui = int(raw_input("Where shall I stop?"))
    while len(f) < ui:
        f.append(f[x] + f[y])
        print f, len(f)
        x += 1
        y += 1
        
    return
#fibb()
    
#Apply the fibonacci function to two integers of your choice.
def fibonaccify():#f[n + 1] = f[n] + f[n - 1]
    ui_one = int(raw_input("Feed me an integer: "))
    ui_two = int(raw_input("Feed me a bigger one: "))
    if ui_two < ui_one:
        ui_two = int(raw_input("Bigger than %s" % ui_one))
        if ui_two < ui_one:
            ui_two = ui_one + 2
            print "Okay, let's say it's %s" % ui_two
            
    ui_length = int(raw_input("How long do you want it?"))
    f = [ui_one, ui_two]
    x = len(f) - 1
    y = x - 1
    while len(f) < ui_length:
        f.append(f[x] + f[y])
        print f, len(f)
        x += 1
        y += 1
    return

fibonaccify()



    