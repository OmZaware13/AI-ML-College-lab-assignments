board = [" "] * 9
def show_board():
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("--+---+--")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("--+---+--")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print()

def check_winner(symbol):
    winning_positions = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for position in winning_positions:
        if (board[position[0]] == symbol and
            board[position[1]] == symbol and
            board[position[2]] == symbol):
            return True

    return False
def ai_move():
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"

            if check_winner("O"):
                return

            board[i] = " "

    for i in range(9):
        if board[i] == " ":
            board[i] = "X"

            if check_winner("X"):
                board[i] = "O"
                return

            board[i] = " "

    if board[4] == " ":
        board[4] = "O"
        return
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            return
print("TIC TAC TOE")
print("Player = X")
print("AI = O")

print("\nPositions:")
print("1 | 2 | 3")
print("--+---+--")
print("4 | 5 | 6")
print("--+---+--")
print("7 | 8 | 9")

while True:
    position = int(input("\nEnter position (1-9): "))
    position = position - 1

    if position < 0 or position > 8:
        print("Invalid position!")
        continue

    if board[position] != " ":
        print("Position already occupied!")
        continue

    board[position] = "X"

    show_board()
    if check_winner("X"):
        print("You win!")
        break
    if " " not in board:
        print("Draw!")
        break
    print("AI's turn...")
    ai_move()

    show_board()
    if check_winner("O"):
        print("AI wins!")
        break
    if " " not in board:
        print("Draw!")
        break