import string
import random



characters = list(string.ascii_letters + string.digits + "!@#$%^&*")
passwords = []


def randomgeneratepassword():
    def generatepassword():


        ask = input("Do you want to generate a password: ")
        sky = ask

        if sky.lower() == "yes" or sky.lower() == "":
            lens = input ("Select length of the password: ")
            userName = input ("Enter UserName: ")
        
            length = int(lens)
            random.shuffle(characters)

            password = []

            for x in range (length):
                password.append(random.choice(characters))
            

            random.shuffle(password)

            password = "".join(password)
            
            
            cake = password
            arr = (userName + cake)
            print(arr)
            passwords.append(arr)
            
        elif sky.lower() == "no":
            print("Goodbye")
            quit()
        else:
            print("Invalid Input, please input yes or no")

    while True:
        generatepassword()
        print("Stored passwords", ":", passwords)
