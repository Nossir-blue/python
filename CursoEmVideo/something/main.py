def registration():
    username = input("\n\nEnter username: ")
    email = input("Enter email: ")
    password = input("Enter password: ")
    confirmPassword = input("Repeat the password: ")
    while confirmPassword != password:
        if confirmPassword != password:
            print("Password does not match the previous one")
            confirmPassword = input("Repeat the password: ")
        else:
            print("Ok")
    phoneNumber = int(input("Enter phone number: "))
    numberStr = str(phoneNumber)
    while len(numberStr) < 9:
        numberStr = str(phoneNumber)
        if len(numberStr) < 9:
            print("This is not an oficial phone number")
            phoneNumber = int(input("Enter phone number: "))
        elif len(numberStr) > 9:
            print("This is not an oficial phone number")
            phoneNumber = int(input("Enter phone number: "))
        else:
            print("Ok")
    print("Great, account created")
    main()

    

def login():
    registrationQuestion = input("\n\nDon't have an account?\nType 1 to create an account\nType 2 to login\nResponse: ")
    if registrationQuestion == 1:
        registration()
    else:
        loginForm = input("Enter Email/Phone Number/ Email: ")
        loginPassword = input("Enter password: ")

#def DashBoard:
     

def main():
    selectNumber = int(input("1 - Login\n2 - Registration\nResponse: "))
    if selectNumber == 1:
        login()
    elif selectNumber == 2:
        registration()

main()