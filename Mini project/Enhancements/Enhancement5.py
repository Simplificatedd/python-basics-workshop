# Enhancement 5: Keep track and display the number of rounds played and saves the player's name

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
roundCount = 0
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
    
def display_stats(drawCount, winCount, lossCount, roundCount, playerName):
    print("\n-----Game Ended-----")
    print(f"Thanks for playing, {playerName}!")
    print("\nHere are your stats:\n")
    print(f"No. of Rounds:\t{roundCount}")
    print(f"Wins:\t\t{winCount}")
    print(f"Losses:\t\t{lossCount}")
    print(f"Draws:\t\t{drawCount}")

def get_player_name():
    playerName = input("Enter your name (leave blank for Guest): ")
    if playerName.strip() == "":
        playerName = "Guest"
    print(f"Welcome, {playerName}! Let's play Rock, Paper, Scissors.\n")
    return playerName
#endregion

#region ##### Main code #####
playerName = get_player_name()
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

    roundCount += 1

display_stats(drawCount, winCount, lossCount, roundCount, playerName)
#endregion