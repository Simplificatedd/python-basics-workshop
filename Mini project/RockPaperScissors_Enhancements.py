import random

PossibleMoves = ['rock', 'paper', 'scissors']

playerMove = input("Your move? (Rock/Paper/Scissors): ").lower()
computerMove = random.choice(PossibleMoves)

if playerMove in PossibleMoves:
    print(f"You chose {playerMove}.")
    print(f"CPU chose {computerMove}.")
    
    if playerMove == computerMove:
        print("It is a draw.\n")
    elif (playerMove == "rock" and computerMove == "scissors") or (playerMove == "paper" and computerMove == "rock") or (playerMove == "scissors" and computerMove == "paper"):
        print("You won!\n")
    else:
        print("You lost!\n")
else:
    print("Invalid move. Please enter 'Rock', 'Paper', or 'Scissors'.")