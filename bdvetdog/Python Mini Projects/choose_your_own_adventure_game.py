name = input("Type your name\nAnswer: ")
print("\nWelcome "+name+" to this adventure")

answer = input("\nYou are on a dirt road, it has come to an end and you can go left or right. Which way would you have to go?\nAnswer: ").lower()

if answer == "left":
    answer = input("\nYou come to a river, you can walk around it or swim accross. Type 'walk' to walk around and 'swim' to swim accross\nAnswer: ").lower()
    if answer == "swim":
        print("\nYou swam accross and were eaten by an alligator")
    elif answer == "walk":
        print("\nYou walked for many miles, ran out of water and you lost the game")
    else:
        print("\nNot a valid option. You lose")
elif answer == "right":
    answer = input("\nYou ome to a bridge, it looks wobbly, do you want to 'cross' it or head 'back'?\nAnswer: ").lower()
    if answer == "back":
        print("\nYou go back and lose")
    elif answer == "cross":
        answer = input("\nYou crossed the bridged and meet a stranger. do you talk to them?(Yes/No)\nAnswer: ").lower()
        if answer == "yes":
            print("\nYou talk to the stranger and they give you gold. You win!")
        elif answer == "no":
            print("\nYou ignored the stranger and they are offended. You lose!")
        else:
            print("\nNot a valid option. You lose")
    else:
        print("\nNot a valid option. You lose")
else:
    print("\nNot a valid option, you lose.")

print("Thank you for trying",name)