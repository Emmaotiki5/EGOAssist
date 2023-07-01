import random
def play():
    
    options = ["rock", "paper", "scissors"]
    user_input = input("Choose Rock, Paper or Scissors:  ")
    computer_output = random.choice(options)
    if user_input.lower() == computer_output:
        print(computer_output.upper())
        print("Draw")

    elif user_input.lower() == "rock" and computer_output == "paper":
        print(computer_output.upper())
        print("Lose")
        

    elif user_input.lower() == "paper" and computer_output == "scissors":
        print(computer_output.upper())
        print("Lose")

    elif user_input.lower() == "scissors" and computer_output == "rock":
        print(computer_output.upper())
        print("Lose")

    elif user_input.lower() == "scissors" and computer_output == "paper":
        print(computer_output.upper())
        print("Win")
    
    elif user_input.lower() == "rock" and computer_output == "scissors":
        print(computer_output.upper())
        print("Win")

    elif user_input.lower() == "paper" and computer_output == "rock":
        print(computer_output.upper())
        print("Win")


    else:
        print("Invalid input")
        


    cont = input("Do you want to try again: ")
    if cont.lower() == "yes" or cont.lower() == "" :
        ()


    elif cont.lower() == "no":
        print("Goodbye")
        quit()


    else: 
        print("Invalid Input")
        

def rps():
    while True:
        play()