import random

# insert the range
number = int(input("Insert a number for the guessing game\nNumber: "))

random_number =  random.randint(0,number)

tries = 0
while True:
    guess = int(input("Guess the number: "))
    tries += 1
    if guess != random_number:
        print("You got it wrong!")
        continue
    else:
        print("You got it right!")
        break

print("Number of tries:",tries)