'''
Created on Apr 6, 2016

@author: Administrator
'''
import math

def ack(x, y):
    if x == 0:
        return y + 1
    elif y == 0:
        return ack(x - 1, 1)
    else:
        return ack(x - 1, ack(x, y-1))

print "0, 0:", ack(0, 0) 
print "0, 2:",  ack(0, 2)
print "3, 0:",  ack(3, 0)
print "2, 2:", ack(2, 2)
print "3, 3:",  ack(3, 3)
print "2, 3:",  ack(2, 3)
print "3, 2:",  ack(3, 2)
print "2, 1:",  ack(2, 1)
print "1, 2:",  ack(1, 2)
print "3, 1:",  ack(3, 1)
print "1, 3:",  ack(1, 3)
print "4, 0:",  ack(4, 0)
print "0, 4:",  ack(0, 4)
print "3, 4:",  ack(3, 4)
print "Ackermann 4,3, max recursion"
print "end"