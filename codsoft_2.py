board = [" " for _ in range(9)]
def print_board():
    print()
    for i in range(0, 9, 3):
        print(" ", board[i], " | ", board[i+1], " | ", board[i+2])
        if i < 6:
            print("-----|-----|-----")
    print()

def check_winner(player):
    win_positions = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for pos in win_positions:
        if board[pos[0]] == board[pos[1]] == board[pos[2]] == player:
            return True
    return False

def is_board_full():
    return " " not in board

def player_move():
    while True:
        try:
            move = int(input("Your move (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == " ":
                board[move] = "X"
                break
            print("Oops, that's not a valid move. Give it another shot.")
        except ValueError:
            print("Just enter a number between 1 and 9, please.")

def ai_move():
    print("AI is thinking...")
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            break

def game():
    print("Let's play Tic-Tac-Toe!")
    print("You're X. The AI is O.")
    while True:
        print_board()
        player_move()
        if check_winner("X"):
            print_board()
            print("You win! Nice job.")
            break
        if is_board_full():
            print_board()
            print("Looks like it's a draw.")
            break
        ai_move()
        if check_winner("O"):
            print_board()
            print("AI wins! Maybe next time.")
            break
        if is_board_full():
            print_board()
            print("Looks like it's a draw.")
            break

game()
