# Enhancement 1: Refactor the code to use functions
# Enhancement 2: Allow user to keep playing until "quit" or "exit" is entered
# Enhancement 3: Allow user to input "r", "p", "s", "q" or "e" as shortcuts for moves and exit commands
# Enhancement 4: Keep track and display the number of wins, losses, and draws

#region ##### import #####
import random
#endregion

#region ##### Variables #####
PossibleMoves = ['rock', 'paper', 'scissors']
ExitCommands = ['quit', 'exit']
shortcutCommands = ['r', 'p', 's', 'q', 'e']
winCount = 0
lossCount = 0
drawCount = 0
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

def show_conclusion(outcome, drawCount, winCount, lossCount):
    if outcome == 1:
        print("It is a draw.\n")
        drawCount += 1
    elif outcome == 2:
        print("You won!\n")
        winCount += 1
    elif outcome == 3:
        print("You lost!\n")
        lossCount += 1
    return drawCount, winCount, lossCount

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
    
def display_stats(drawCount, winCount, lossCount):
    print("\n-----Game Ended-----")
    print("stats:\n")
    print(f"Wins: {winCount}")
    print(f"Losses: {lossCount}")
    print(f"Draws: {drawCount}")
#endregion

#region ##### Main code #####
playerMove = get_player_move()
while(not check_exit(playerMove)):

    if validate_player_move(playerMove):
        computerMove = get_computer_move()
        display_moves(playerMove, computerMove)
        outcome = decide_outcome(playerMove, computerMove)
        drawCount, winCount, lossCount = show_conclusion(outcome, drawCount, winCount, lossCount)
        playerMove = get_player_move()

    else:
        print("Invalid move. Please enter 'Rock', 'Paper', or 'Scissors'.")
        playerMove = get_player_move()

display_stats(drawCount, winCount, lossCount)
#endregion