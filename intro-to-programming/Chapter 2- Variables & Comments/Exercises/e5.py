import math
#A = Budget
#B = Price per USB stick
#C = Number of USB stick
#D = Total amount of USB stick
#E = Left in hand

A=float (input("Please enter the Budget:"))
B=float (input("Please enter the price per USB:"))
C= (A//B)

print("Number of USB sticks:",C)

D=B*C

print("Total amount of USB in $:", D)

E=A-D

print("How much left in $:",E)