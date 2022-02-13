'''Guessing game v1 
Troy Baker (14 Fe 2022)'''

#Import libraries and set variables
import random
n = random.randint(0,10)

#Gameplay
print("welcome to my guessing game")
number = int(input ("guess my number"))
if number == n:
  print("ez")
  