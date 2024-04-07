print("Welcome to my computer quiz!")

playing = input("Do you want to play?\nAnswer: ")

if playing.lower() != "yes":
    quit()

print("Okay! Let's play :)")
score = 0

answer = input("What does CPU stand for?\nAnswer: ")
if answer.lower() == "central processing unit":
    print('Correct!\n')
    score += 1
else:
    print("Incorrect!\n")

answer = input("What does gpu stand for?\nAnswer: ")
if answer.lower() == "graphics processing unit":
    print('Correct!\n')
    score += 1
else:
    print("Incorrect!\n")

answer = input("What does RAM stand for\nAnswer: ")
if answer.lower() == "random access memory":
    print('Correct!\n')
    score += 1
else:
    print("Incorrect!\n")

answer = input("What does PSU stand for?\nAnswer: ")
if answer.lower() == "power supply":
    print('Correct!\n')
    score += 1
else:
    print("Incorrect!\n")

print("You got",score,"question")
print("You got",int((score/4)*100),"%")
