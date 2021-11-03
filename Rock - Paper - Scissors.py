import random


user=0
computer=0
options=["rock","paper","scissor"]

while True:
    user_input=input("Rock Paper Scissor or 'q' to Quit: \n").lower()
    if user_input=="q":
        print("You Quited.")
        break
    
    if user_input not in options:
        print("Type only Rock Paper or Scissor")
        continue
    
    random_number=random.randint(0,3)
    computer_choose=options[random_number]
    print("computer chooses", computer_choose+".")
    
    if user_input=="rock" and computer_choose=="scissor":
        print("You Won!")
    
    elif user_input=="paper" and computer_choose=="rock":
        print("You Won!")
        
    elif user_input=="scissor" and computer_choose=="paper":
        print("You Won!")
    
    else:
        print("You Lost!") 
    

    

    