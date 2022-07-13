import random

user_count=0
computer_count=0


while ((user_count <10) or (computer_count <10)):
    user_choice=input("Choose rock, paper or scissors: ")
    if user_choice == "rock" or "paper" or "scissors":
        print(f"You chose was {user_choice}")
        opponent_choice=random.choice(["rock","paper","scissors"])
        print(f"The computer chose {opponent_choice}")
        if opponent_choice == "scissors" and user_choice == "paper":
            print("You lose this round")
            computer_count=computer_count+1
        elif opponent_choice == "scissors" and user_choice == "rock":
            print("You win this round")
            user_count=user_count+1
        elif opponent_choice == "paper" and user_choice == "rock":
            print("You lose this round")
            computer_count=computer_count+1
        elif opponent_choice == "paper" and user_choice == "scissors":
            print("You win this round")
            user_count=user_count+1
        elif opponent_choice == "rock" and user_choice == "paper":
            print("You win this round")
            user_count=user_count+1
        elif opponent_choice == "rock" and user_choice == "scissors":
            print("You lose this round")
            computer_count=computer_count+1
        elif opponent_choice == user_choice:
            print("Tie")
        print(f"Current scores: Your score = {user_count} & computer score = {computer_count}")
    else:
        print("That is not a valid answer. Please try again")

if user_count == 10:
    print("Congratulations you won")
else:
    print("You lose, better luck next time!")

