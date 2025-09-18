# Enhancement 10: Final refactor and cleanup of code

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
moveHistory = {name : [] for name in ['Player', 'CPU']}
historyCommands = ['history', 'h']
winCount = lossCount = drawCount = roundCount = 0
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
    moveHistory['Player'].append(playerMove)
    moveHistory['CPU'].append(computerMove)
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
    for i in range(len(moveHistory['Player'])):
        print(f"{i+1}\t{moveHistory['Player'][i].capitalize()}\t{moveHistory['CPU'][i].capitalize()}")
    print("------------------------")

def gamemode3(playerName): # Default mode
    global drawCount, winCount, lossCount, roundCount
    playerMove = "placeholder"
    while(not check_exit(playerMove)):
        playerMove = get_player_move()
        if check_history(playerMove):
            playerMove = get_player_move()
            continue

        if validate_player_move(playerMove):
            main_game(playerMove)
        else:
            print("Invalid move. Please enter 'Rock', 'Paper', or 'Scissors'.")

        roundCount += 1

    display_stats(drawCount, winCount, lossCount, roundCount, playerName)

def gamemode1(playerName): # Best of n
    global drawCount, winCount, lossCount, roundCount
    n = validate_input("odd n")
    
    roundsToWin = n // 2 + 1

    while winCount < roundsToWin and lossCount < roundsToWin and roundCount < n:
        playerMove = get_player_move()
        if check_exit(playerMove):
            break
        if check_history(playerMove):
            continue

        if validate_player_move(playerMove):
            main_game(playerMove)
        else:
            print("Invalid move. Please enter 'Rock', 'Paper', or 'Scissors'.")
    if winCount > lossCount:
        print(f"\nCongratulations {playerName}, you won the best of {n}!")
    elif lossCount > winCount:
        print(f"\nSorry {playerName}, CPU won the best of {n}.")
    else:
        print(f"\nThe best of {n} series ended in a tie!")
    display_stats(drawCount, winCount, lossCount, roundCount, playerName, True)

def gamemode2(playerName): # First to n
    global drawCount, winCount, lossCount, roundCount
    n = validate_input("positive n")

    while winCount < n and lossCount < n:
        playerMove = get_player_move()
        if check_exit(playerMove):
            break
        if check_history(playerMove):
            continue

        if validate_player_move(playerMove):
            main_game(playerMove)
        else:
            print("Invalid move. Please enter 'Rock', 'Paper', or 'Scissors'.")
    if winCount == n:
        print(f"\nCongratulations {playerName}, you reached {n} wins first!")
    elif lossCount == n:
        print(f"\nSorry {playerName}, CPU reached {n} wins first.")
    display_stats(drawCount, winCount, lossCount, roundCount, playerName, True)

def validate_input(usecase):
    if usecase == "mode":
        return validate_mode()
    elif usecase == "positive n":
        return validate_positive_n()
    elif usecase == "odd n":
        return validate_odd_n()

def validate_mode():
    selection = input("Enter 1, 2, or 3: ")
    mode = int(selection) if selection.isdigit() else 3
    while mode not in [1, 2, 3]:
        print("Invalid selection. Please enter 1, 2, or 3.")
        selection = input("Enter 1, 2, or 3: ")
        mode = int(selection) if selection.isdigit() else 3
    return mode

def validate_positive_n():
    n = input("Enter a number for 'First to n': ")
    if n.isdigit():
        n = int(n)
    else:
        n = -1
    while n <= 0:
        print("Please enter a valid positive integer.")
        n = input("Enter a number for 'First to n': ")
        if n.isdigit():
            n = int(n)
        else:
            n = -1
    return n

def validate_odd_n():
    n = input("Enter an odd number for 'Best of n': ")
    if n.isdigit():
        n = int(n)
    else:
        n = 2
    while n % 2 == 0 and n > 0:
        print("Please enter a valid odd number.")
        n = input("Enter an odd number for 'Best of n': ")
        if n.isdigit():
            n = int(n)
        else:
            n = 2
    return n

def main_game(playerMove):
    global drawCount, winCount, lossCount, roundCount
    computerMove = get_computer_move()
    display_moves(playerMove, computerMove)
    outcome = decide_outcome(playerMove, computerMove)
    drawCount, winCount, lossCount = show_conclusion(outcome, drawCount, winCount, lossCount)
    roundCount += 1
    return
#endregion

#region ##### Main code #####
print("Select a game mode:")
print("1. Best of n")
print("2. First to n")
print("3. Play until \"exit\" or \"quit\" is mentioned (default)")
mode = validate_input("mode")
print(f"{mode} selected.")
if mode == 1:
    playerName = get_player_name()
    gamemode1(playerName)
elif mode == 2:
    playerName = get_player_name()
    gamemode2(playerName)
else:
    playerName = get_player_name()
    gamemode3(playerName)
#endregion