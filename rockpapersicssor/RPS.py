import random

user_wins = 0
computer_wins = 0

option = ["rock", "paper", "scissors"]


while True:
    user_input = input("Rock/paper/scissor or q to quit :").lower()

    if user_input == "q":
        break

    if user_input not in option:
        continue

    random_number = random.randint(0, 2)
    # rock 0 paper 1 sicssors 2
    computer_pick = option[random_number]
    print("computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("you won!!")
        user_wins += 1

    elif user_input == "paper" and computer_pick == "rock":
        print("you won!!")
        user_wins += 1

    elif user_input == "scissors" and computer_pick == "paper":
        print("you won!!")
        user_wins += 1

    else:
        print("you lost!!")
        computer_wins += 1

print("you won", user_wins, "times")
print("computer won", computer_wins, "times")
print("goodbye")
