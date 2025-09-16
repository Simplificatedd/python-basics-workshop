# Enhancement 3: Allow user to input "r", "p", "s", "q" or "e" as shortcuts for moves and exit commands

#region ##### import #####
import random
#endregion

#region ##### Variables #####
PossibleMoves = ['rock', 'paper', 'scissors']
ExitCommands = ['quit', 'exit']
shortcutCommands = ['r', 'p', 's', 'q', 'e']
#endregion

#region ##### Functions #####
def get_player_move():
    playerMove = input("Your move? (Rock/Paper/Scissors): ").lower()
    playerMove = map_shortcuts(playerMove)
    return playerMove

def check_exit(playerMove):
    if playerMove in ExitCommands:
        return True
    return False

def validate_player_move(playerMove):
    if playerMove in PossibleMoves:
        return True
    return False

def get_computer_move():
    computerMove = random.choice(PossibleMoves)
    return computerMove

def display_moves(playerMove, computerMove):
    print(f"You chose {playerMove}.")
    print(f"CPU chose {computerMove}.")

def decide_outcome(playerMove, computerMove):
    if playerMove == computerMove:
        return 1
    elif (playerMove == "rock" and computerMove == "scissors") or (playerMove == "paper" and computerMove == "rock") or (playerMove == "scissors" and computerMove == "paper"):
        return 2
    return 3

def show_conclusion(outcome):
    if outcome == 1:
        print("It is a draw.\n")
    elif outcome == 2:
        print("You won!\n")
    elif outcome == 3:
        print("You lost!\n")

def map_shortcuts(playerMove):
    if playerMove == 'r':
        return 'rock'
    elif playerMove == 'p':
        return 'paper'
    elif playerMove == 's':
        return 'scissors'
    elif playerMove == 'e':
        return 'exit'
    elif playerMove == 'q':
        return 'quit'
    else:
        return playerMove
#endregion

#region ##### Main code #####
playerMove = get_player_move()
while(not check_exit(playerMove)):

    if validate_player_move(playerMove):
        computerMove = get_computer_move()
        display_moves(playerMove, computerMove)
        outcome = decide_outcome(playerMove, computerMove)
        show_conclusion(outcome)
        playerMove = get_player_move()
    else:
        print("Invalid move. Please enter 'Rock', 'Paper', or 'Scissors'.")
        playerMove = get_player_move()
        
print("\n-----Game Ended-----")
#endregion