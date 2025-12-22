import random

print("Scissors: s\n Rock: r\n Paper:p\n")
computer = random.choice([0, 1, -1])
user_str = input("Enter your choice: ")
user_dict = {"p": 1, "s": 0, "r": -1}
reverse_dict = {1: "p", 0: "s", -1: "r"}
user = user_dict[user_str]
print(f'You choose {reverse_dict[user]} and computer choose {reverse_dict[computer]}')

if computer == user:
    print("It's a draw.")
else:
    if computer == 1 and user == 0:
        print("You win!")
    elif computer == 0 and user == 1:
        print("You lose!")
    elif computer == -1 and user == 0:
        print("You loose!")
    elif computer == 0 and user == -1:
        print("You win!")
    elif computer == -1 and user == 1:
        print("You lose!")
    elif computer == 1 and user == -1:
        print("You win!")
    else:

        print("Something went wrong!!")
