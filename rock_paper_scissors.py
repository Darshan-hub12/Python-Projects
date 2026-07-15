import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

print("=== Rock Paper Scissors ===")

while True:
    user = input("\nEnter rock, paper, or scissors: ").lower()

    if user not in choices:
        print("Invalid choice. Please try again.")
        continue

    computer = random.choice(choices)

    print("You chose:", user)
    print("Computer chose:", computer)

    if user == computer:
        print("It's a tie!")

    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You win!")
        user_score += 1

    else:
        print("Computer wins!")
        computer_score += 1

    print(f"Score - You: {user_score} | Computer: {computer_score}")

    play_again = input("Play again? (yes/no): ").lower()

    if play_again != "yes":
        break

print("\nFinal Score")
print("You:", user_score)
print("Computer:", computer_score)
print("Thanks for playing!")
