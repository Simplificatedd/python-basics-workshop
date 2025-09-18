# Enhancement 1: Refactor the code to use functions
# Enhancement 2: Allow user to keep playing until "quit" or "exit" is entered
# Enhancement 3: Allow user to input "r", "p", "s", "q" or "e" as shortcuts for moves and exit commands
# Enhancement 4: Keep track and display the number of wins, losses, and draws
# Enhancement 5: Keep track and display the number of rounds played and saves the player's name
# Enhancement 6: Refactor winning logic to use a dictionary
# Enhancement 7: Add randomized winner and loser messages, capitalize names and moves
# Enhancement 8: Add move history (type 'history' or 'h' to view)
# Enhancement 9: Add 2 new gamemodes - "Best of n" and "First to n"

#region ##### import #####
import random
#endregion

#region ##### Variables #####
PossibleMoves = ['rock', 'paper', 'scissors']
ExitCommands = ['quit', 'exit']
shortcutCommands = ['r', 'p', 's', 'q', 'e']
winningDictionary = {
    'rock': 'scissors',
    'paper': 'rock',
    'scissors': 'paper'
}
winMessage = ["Great job!", "Well played!", "You're on fire!", "Keep it up!", "Fantastic!"]
loseMessage = ["Don't give up!", "Keep trying!", "You'll win the next round!", "Stay positive!", "Chin up!"]
drawMessage = ["You think like CPU!", "So close!", "Stalemate!", "Close one!", "Held you off!"]
computerMoveHistory = []
playerMoveHistory = []
historyCommands = ['history', 'h']
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
    playerMove = playerMove.capitalize()
    computerMove = computerMove.capitalize()
    playerMoveHistory.append(playerMove)
    computerMoveHistory.append(computerMove)
    print(f"You chose {playerMove}.")
    print(f"CPU chose {computerMove}.")

def decide_outcome(playerMove, computerMove):
    if playerMove == computerMove:
        return 1
    elif winningDictionary[playerMove] == computerMove:
        return 2
    return 3

def show_conclusion(outcome, drawCount, winCount, lossCount):
    if outcome == 1:
        print("\nIt is a draw.")
        display_random_message(drawMessage)
        drawCount += 1
    elif outcome == 2:
        print("\nYou won!")
        display_random_message(winMessage)
        winCount += 1
    elif outcome == 3:
        print("\nYou lost!")
        display_random_message(loseMessage)
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
    
def display_stats(drawCount, winCount, lossCount, roundCount, playerName, displayAsCPU=False):
    if displayAsCPU:
        print("\n-----Game Ended-----")
        print(f"Thanks for playing, {playerName}!")
        print("\nHere are your stats:\n")
        print(f"No. of Rounds:\t{roundCount}")
        print(f"Your Wins:\t{winCount}")
        print(f"CPU Wins:\t{lossCount}")
        print(f"Draws:\t\t{drawCount}")
    else:
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
    return playerName.capitalize()

def display_random_message(messageList):
    print(random.choice(messageList))

def check_history(playerMove):
    if playerMove in historyCommands:
        display_history()
        return True
    return False

def display_history():
    print("\n-----Move History-----")
    print("Round\tPlayer\tCPU")
    for i in range(len(playerMoveHistory)):
        print(f"{i+1}\t{playerMoveHistory[i].capitalize()}\t{computerMoveHistory[i].capitalize()}")
    print("------------------------")

def gamemode3(): # Default mode
    playerName = get_player_name()
    winCount = 0
    lossCount = 0
    drawCount = 0
    roundCount = 0
    playerMove = get_player_move()
    while(not check_exit(playerMove)):
        if check_history(playerMove):
            playerMove = get_player_move()
            continue

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

def gamemode1(): # Best of n
    playerName = get_player_name()
    winCount = 0
    lossCount = 0
    drawCount = 0
    roundCount = 0
    n = input("Enter an odd number for 'Best of n': ")
    if n.isdigit():
        n = int(n)
    else:
        n = 2
    while n % 2 == 0 and n < 0:
        print("Please enter a valid odd number.")
        n = input("Enter an odd number for 'Best of n': ")
        if n.isdigit():
            n = int(n)
        else:
            n = 2
    
    roundsToWin = n // 2 + 1

    while winCount < roundsToWin and lossCount < roundsToWin and roundCount < n:
        playerMove = get_player_move()
        if check_exit(playerMove):
            break
        if check_history(playerMove):
            continue

        if validate_player_move(playerMove):
            computerMove = get_computer_move()
            display_moves(playerMove, computerMove)
            outcome = decide_outcome(playerMove, computerMove)
            drawCount, winCount, lossCount = show_conclusion(outcome, drawCount, winCount, lossCount)
            roundCount += 1
        else:
            print("Invalid move. Please enter 'Rock', 'Paper', or 'Scissors'.")
    if winCount > lossCount:
        print(f"\nCongratulations {playerName}, you won the best of {n}!")
    elif lossCount > winCount:
        print(f"\nSorry {playerName}, CPU won the best of {n}.")
    else:
        print(f"\nThe best of {n} series ended in a tie!")
    display_stats(drawCount, winCount, lossCount, roundCount, playerName, True)

def gamemode2(): # First to n
    playerName = get_player_name()
    winCount = 0
    lossCount = 0
    drawCount = 0
    roundCount = 0
    while True:
        n = input("Enter a number for 'First to n': ")
        if n.isdigit():
            n = int(n)
        else:
            n = -1
        if n > 0:
            break
        print("Please enter a valid positive integer.")

    while winCount < n and lossCount < n:
        playerMove = get_player_move()
        if check_exit(playerMove):
            break
        if check_history(playerMove):
            continue

        if validate_player_move(playerMove):
            computerMove = get_computer_move()
            display_moves(playerMove, computerMove)
            outcome = decide_outcome(playerMove, computerMove)
            drawCount, winCount, lossCount = show_conclusion(outcome, drawCount, winCount, lossCount)
            roundCount += 1
        else:
            print("Invalid move. Please enter 'Rock', 'Paper', or 'Scissors'.")
    if winCount == n:
        print(f"\nCongratulations {playerName}, you reached {n} wins first!")
    elif lossCount == n:
        print(f"\nSorry {playerName}, CPU reached {n} wins first.")
    display_stats(drawCount, winCount, lossCount, roundCount, playerName, True)
#endregion

#region ##### Main code #####
print("Select a game mode:")
print("1. Best of n")
print("2. First to n")
print("3. Play until \"exit\" or \"quit\" is mentioned (default)")
selection = input("Enter 1, 2, or 3: ")
mode = int(selection) if selection.isdigit() else 3
while mode not in [1, 2, 3]:
    print("Invalid selection. Please enter 1, 2, or 3.")
    selection = input("Enter 1, 2, or 3: ")
    mode = int(selection) if selection.isdigit() else 3
print(f"{mode} selected.")
if mode == 1:
    gamemode1()
elif mode == 2:
    gamemode2()
else:
    gamemode3()
#endregion