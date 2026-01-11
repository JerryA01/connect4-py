

ROWS = 6
COLS = 7


def create_board():
    """Creates and returns an empty board."""
    return [[" " for _ in range(COLS)] for _ in range(ROWS)]


def print_board(board):
    """Prints the current board state."""
    print("\n")
    for row in board:
        print("|" + "|".join(row) + "|")
    print(" " + " ".join(str(i) for i in range(COLS)))
    print("\n")


def apply_gravity(board):
    """Apply gravity to the board so that all counters fall to the bottom of their column."""
    for col in range(COLS):
        stack = []
        for row in range(ROWS):
            if board[row][col] != " ":
                stack.append(board[row][col])

        for row in range(ROWS - 1, -1, -1):
            board[row][col] = stack.pop() if stack else " "


def drop_counter(board, col, player):
    """Drop a counter for `player` into column `col` if possible."""
    if col < 0 or col >= COLS:
        return False
    for row in range(ROWS - 1, -1, -1):
        if board[row][col] == " ":
            board[row][col] = player
            return True
    return False


def remove_row(board, row):
    """
    Remove the specified row from the board and shift all rows above down.

    Args:
        board: 2D list representing the board.
        row: Row index to remove.

    Returns:
        True if the row was successfully removed, False otherwise.
    """
    if row < 0 or row >= ROWS:
        print("Invalid row.")
        return False

    if all(cell == " " for cell in board[row]):
        print("That row is empty. You can't remove an empty row.")
        return False

    del board[row]
    board.insert(0, [" " for _ in range(COLS)])
    return True


def remove_counter(board, row, col):
    """
    Remove a counter at a specific position and apply gravity.

    Args:
        board: 2D list representing the board.
        row: Row index.
        col: Column index.

    Returns:
        True if a counter was removed, False otherwise.
    """
    if row < 0 or row >= ROWS or col < 0 or col >= COLS:
        print("Invalid position.")
        return False

    if board[row][col] == " ":
        print("You can't remove an empty counter.")
        return False

    board[row][col] = " "
    apply_gravity(board)
    return True



def check_win(board):
    """
    Check if any player has won the game.

    Returns:
        True if there is a winner, False otherwise.
    """
    # Horizontal, Vertical, Diagonal
    for r in range(ROWS):
        for c in range(COLS - 3):
            if board[r][c] != " " and all(board[r][c + i] == board[r][c] for i in range(4)):
                return True

    for c in range(COLS):
        for r in range(ROWS - 3):
            if board[r][c] != " " and all(board[r + i][c] == board[r][c] for i in range(4)):
                return True

    for r in range(ROWS - 3):
        for c in range(COLS - 3):
            if board[r][c] != " " and all(board[r + i][c + i] == board[r][c] for i in range(4)):
                return True

    for r in range(3, ROWS):
        for c in range(COLS - 3):
            if board[r][c] != " " and all(board[r - i][c + i] == board[r][c] for i in range(4)):
                return True

    return False


def get_int(prompt):
    """
    Prompt the user for an integer input.

    Re-prompts until a valid integer is entered.

    Args:
        prompt: String to display to the user.

    Returns:
        The integer entered by the user.
    """
    """Get an integer input from the user."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid number.")


def main():
    """Run the main game loop for Connect 4."""
    board = create_board()
    current_player = "X"

    abilities = {
        "X": {"row": False, "counter": False},
        "O": {"row": False, "counter": False},
    }

    while True:
        print_board(board)
        print(f"Player {current_player}'s turn")
        print("1: Drop Counter")
        print("2: Remove Row (once)")
        print("3: Remove Counter (once)")

        choice = input("Choose action: ")
        success = False

        if choice == "1":
            col = get_int("Enter column: ")
            success = drop_counter(board, col, current_player)

        elif choice == "2":
            if abilities[current_player]["row"]:
                print("You can't remove a row again. You can only do this once.")
                continue

            row = get_int("Enter row to remove: ")
            success = remove_row(board, row)

            if success:
                abilities[current_player]["row"] = True
            else:
                continue  # player goes again

        elif choice == "3":
            if abilities[current_player]["counter"]:
                print("You can't remove a counter again. You can only do this once.")
                continue

            row = get_int("Row: ")
            col = get_int("Column: ")
            success = remove_counter(board, row, col)

            if success:
                abilities[current_player]["counter"] = True
            else:
                continue  # player goes again

        else:
            print("Invalid choice.")
            continue

        if not success:
            print("Move failed.")
            continue

        if check_win(board):
            print_board(board)
            print(f"Player {current_player} wins!")
            break

        current_player = "O" if current_player == "X" else "X"



main()
