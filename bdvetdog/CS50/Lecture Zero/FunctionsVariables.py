'''#name=input("What's your name?\nAnswer: ").strip().title()#you can also do this

#name = name.strip()
#name = name.capitalize()
#name = name.title() # will capitalize all first letter  and not just one
#name = name.strip().title() #you can add multiple methods
name = input("My name is ").strip().title()
first, last = name.split(" ")

print(f"Hello, {first}")'''

def main():
    name = input("What's your name? ").lower().title()
    hello(name)
def hello(name="world"):
    print("Hello,",name)

main()