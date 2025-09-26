import random

def play_game():
    user_wins = 0
    computer_wins = 0
    options = ["rock", "paper", "scissors"]

    print("🎉 Welcome to Rock, Paper, Scissors! 🎉")

    while True:
        user_pick = input("\nType Rock/Paper/Scissors or Q to quit: ").lower()
        if user_pick == "q":
            break
        
        if user_pick not in options:
            print("Invalid option. Please try again.")
            continue
        
        computer_pick = random.choice(options)
        print(f"Computer picked: {computer_pick}")
        
        if user_pick == computer_pick:
            print("It's a draw! 🤝")
        elif (user_pick == "rock" and computer_pick == "scissors") or \
             (user_pick == "scissors" and computer_pick == "paper") or \
             (user_pick == "paper" and computer_pick == "rock"):
            print("You won this round! 🏆")
            user_wins += 1
        else:
            print("You lost this round. Computer wins! 🖥️")
            computer_wins += 1
            
        print(f"Score: You {user_wins} - {computer_wins} Computer")

    print("\n--- Final Score ---")
    print(f"You won {user_wins} times.")
    print(f"The computer won {computer_wins} times.")
    
    if user_wins > computer_wins:
        print("Congratulations, you are the overall winner! ✨")
    elif computer_wins > user_wins:
        print("The computer was the overall winner. Better luck next time!")
    else:
        print("It was an overall tie!")
        
    print("\nThanks for playing! Goodbye!")

# This makes sure the game runs only when the script is executed directly
if __name__ == "__main__":
    play_game()