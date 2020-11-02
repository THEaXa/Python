import random

def randomNo():
    print(random.randrange(1,7))

print("Hello! Welcome to the dice simulator!!")
num = int(input("Key in any number to roll the dice"))
randomNo()

repeat = input("Would you like to role the dice again? (Y/N")

while repeat == "Y" or repeat == "y":
    randomNo()
    repeat = input("Would you like to role the dice again? (Y/N")

print("see you next time")
exit()
