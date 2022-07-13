import random
random_number = random.randint(1,100)

guess=0

while guess != random_number:
    guess=int(input("Guess a number between 1 and 100: "))   # needs to be converted to integer as random_number is integer
    if isinstance(guess,int) != True or 1 <= guess <= 100:
        print("Enter a number between 1 and 100")
        guess=int(input("Guess a number between 1 and 100: "))
    if guess == random_number:
        print("That is the correct number")
    else:
        print("That is not correct")
        if guess < random_number:
            print("You are too low")
        else:
            print("You are too high")

