import random
Rock='''
       ___________
---- --    ________)
          (_______)
          (_______)
          (______)
---- .____(____)

'''
Paper='''
      _________
-----     _____)______
               ________)
               ___________)
            ___________)
------ -______________)
     
'''

Scissors='''
    __________
-----     _____)_______
               ________)
               ___________)
            _____)
------ -_____)
     
'''
user=0
computer=0
while True:
    images=[Rock,Paper,Scissors]
    user_turn = int(input("Enter your choices: if Rock enter 0, Paper enter 1, Scissor enter 2 : "))
    if(user_turn<0) or (user_turn>=3):
        print("You entered Invalid number. Please enter valid number that is 0 or 1 or 2")
    else:
        print("User Choice")
        print(images[user_turn])
        computer_turn = random.randint(0, 2)
        print("Computer Choice")
        print(images[computer_turn])
        if computer_turn==user_turn:
            print("OH ITS DRAW!!")
        elif computer_turn>user_turn:
            print("Computer Wins!!")
            computer+=1
        elif user_turn>computer_turn:
            print("User(YOU) Wins!!")
            user+=1
        elif computer_turn==0 and user_turn==2:
            print("Computer Wins!!")
            computer+=1
        elif computer_turn==2 and user_turn==0:
            print("User(YOU) Wins!!")
            user+=1

        print("if you want to continue the game? enter YES or NO : ")
        continue_game=input()
        if(continue_game.lower()!='yes'):
            print("Your total score is :",user)
            print("Computer total score is :",computer)
            print("Good Bye ! Have a Nice Day")
            break





