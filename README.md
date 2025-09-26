# Rock-Paper-Scissors Game ✊📄✂️

Welcome to the classic Rock-Paper-Scissors game reinvented for the command line! Challenge the computer to a fun, fast-paced battle of wits and luck with simple, clear feedback every step of the way.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [How to Play](#How-to-Play)
- [Code Structure](#code-structure)
- [Sample Gameplay](#sample-gameplay)
- [Behind the Scenes](#behind-the-scenes)
- [Contributing](#contributing)
- [License](#license)

## Overview

This Python-based CLI game pits you against the computer in rounds of Rock-Paper-Scissors. Play as many rounds as you like, see instant results, and try to outsmart the computer to become the ultimate champion! The game keeps score and declares an overall winner when you decide to quit.

## Features

### What Makes This Game Rock? 🎸
- **Simple, Clean UI**: Interactive text prompts guide you smoothly from one round to the next.
- **Unlimited Rounds**: Play endlessly until you choose to quit.
- **Real-Time Feedback**: Immediate results with clear victory, loss, or tie notifications.
- **Score Tracking**: Keep track of wins for both you and the computer.
- **Input Safety**: Robust input validation avoids confusion and mistakes.
- **Quick Exit**: Type 'Q' anytime to gracefully end the game.

## Installation

### Requirements
- Python 3.6 or above
- No external libraries required

### Setup
1. Download or clone the repository
2. Open your terminal and navigate to the project folder
3. Run the game with:
```text
python3 rock_paper_scissors.py
```

## How to play
1. When prompted, enter your choice: `rock`, `paper`, `scissors` or Q to quit.
2. The computer will simultaneously pick its option.
3. You'll see the result of the round displayed along with the updated score.
4. Repeat until you decide to quit by pressing Q.

### Input Tips
- Input is case-insensitive (Rock, rock, ROCK all work).
- Typing anything other than the valid options prompts a friendly retry message.

## Code Structure

### Main Game Loop
```python
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
```
Loops continuously prompting for input, validating, evaluating round outcome, and updating scores.

### Final Result
Displays total wins, declares the overall winner, or a tie, then exits gracefully.

### Sample Gameplay
```output
🎉 Welcome to Rock, Paper, Scissors! 🎉

Type Rock/Paper/Scissors or Q to quit: rock
Computer picked: rock
It's a draw! 🤝
Score: You 0 - 0 Computer

Type Rock/Paper/Scissors or Q to quit: paper
Computer picked: rock
You won this round! 🏆
Score: You 1 - 0 Computer

Type Rock/Paper/Scissors or Q to quit: scissors
Computer picked: paper
You won this round! 🏆
Score: You 2 - 0 Computer

Type Rock/Paper/Scissors or Q to quit: q

--- Final Score ---
You won 2 times.
The computer won 0 times.
Congratulations, you are the overall winner! ✨

Thanks for playing! Goodbye!
```

### Behind the Scenes
- Written in Python with standard `random` library for computer moves
- Command-line interface for universal accessibility
- Logic uses straightforward conditional checks to decide round winners
- Tracks user vs. computer wins dynamically
- Designed for clarity, robustness, and fun

## Contributing
Love the game? Improve it by:
- Adding advanced AI for the computer player
- Introducing new game variants (like Rock-Paper-Scissors-Lizard-Spock)
- Building a graphical interface
- Implementing multiplayer support
- Adding sound or animation (CLI-friendly)
Feel free to fork, modify, and submit pull requests!

## License

This project is open-source and free to use for educational or entertainment purposes.
---

*Last Updated: September 2025*
