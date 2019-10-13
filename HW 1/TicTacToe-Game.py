"""tictactoe game for 2 players"""

# Initializes the list for the positions of the player objects
choices = []

for x in range(1, 10):  # iterates through the range of 1 to 9
    choices.append(x)   # appends an element to the end of the list

playerOneTurn = True    # sets playerOneTurn to true for the first player to have the first move
winner = False          # sets winner to false


# printboard method sets up the tic-tac-toe board for the user
def printboard():
    print('\n -----')
    print('|', choices[0], '|', choices[1], '|', choices[2], '|')
    print(' -----')
    print('|', choices[3], '|', choices[4], '|', choices[5], '|')
    print(' -----')
    print('|', choices[6], '|', choices[7], '|', choices[8], '|')
    print(' -----\n')


#  iterates through the list to see if any of the conditions winner is true or not
while not winner:
    printboard()

    if playerOneTurn:                             # prints the which player's turn is it?
        print("Player 1:")
    else:
        print("Player 2:")

    try:
        choice = int(input(">> "))                # takes in the input from the players
    except:
        print("please enter a valid field")
        continue

    if choices[choice - 1] == 'X' or choices[choice - 1] == 'O':    # prevents illegal assignment of values
        print("illegal move, please try again")
        continue

    if playerOneTurn:
        choices[choice - 1] = 'X'           # Assigns the player one's choice to the corresponding index in the list
    else:
        choices[choice - 1] = 'O'           # Assigns the player two's choice to the corresponding index in the list

    playerOneTurn = not playerOneTurn       # changes the turn of the player

    # conditions for checking if a player has won the game with a 3 in a row
    for x in range(0, 3):
        y = x * 3
        if choices[y] == choices[(y + 1)] and choices[y] == choices[(y + 2)]:
            winner = True
            printboard()
        if choices[x] == choices[(x + 3)] and choices[x] == choices[(x + 6)]:
            winner = True
            printboard()

    if((choices[0] == choices[4] and choices[0] == choices[8]) or
       (choices[2] == choices[4] and choices[4] == choices[6])):
        winner = True
        printboard()

# the output statement stating which player has won based on which player had the last move
print("Player " + str(int(playerOneTurn + 1)) + " wins!\n")
