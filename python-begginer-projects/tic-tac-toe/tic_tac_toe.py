class TicTacToe:
    """
    A class to represent the game logic for a classic 3x3 Tic Tac Toe game.
    Provides functionality to print the board, make moves, check available positions,
    and determine the winner.
    """

    # Constants to define board dimensions
    ROWS = 3
    COLS = 3
    TOTAL_CELLS = ROWS * COLS  # Total number of squares on the board

    def __init__(self):
        """
        Initializes the game board and sets the winner to None.
        The board is represented as a flat list of 9 strings.
        """
        self.board = [' ' for _ in range(self.TOTAL_CELLS)]  # 3x3 board initialized with empty spaces
        self.current_winner = None  # Will store the letter of the winner when the game ends

    def print_board(self):
        """
        Prints the current state of the game board in a human-readable format.
        Each row is sliced out of the flat board list using calculated indices.
        """
        for row_index in range(self.ROWS):
            start = row_index * self.COLS
            end = start + self.COLS
            row = self.board[start:end]
            print('| ' + ' | '.join(row) + ' |')

    @classmethod
    def print_board_nums(cls):
        """
        Prints the board with numbered positions (0-8) to help players reference available moves.
        Does not modify the actual board.
        """
        number_board = [
            [str(cell_index) for cell_index in range(row * cls.COLS, (row + 1) * cls.COLS)]
            for row in range(cls.ROWS)
        ]

        print("Board valid positions")
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        """
        Returns a list of indices where a player can make a move (i.e., empty squares).
        """
        return [i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        """
        Returns True if there are any empty squares on the board.
        Uses available_moves for logic reuse.
        """
        return bool(self.available_moves())

    def num_empty_squares(self):
        """
        Returns the number of empty squares remaining on the board.
        """
        return len(self.available_moves())

    def make_move(self, square, letter):
        """
        Places the player's letter on the board at the given square index.
        Also checks if the move results in a win.

        Args:
            square (int): The index on the board (0-8) where the move is made.
            letter (str): The player's symbol ('x' or 'o').

        Returns:
            bool: True if the move is valid and made successfully, False otherwise.
        """
        if square in self.available_moves():
            self.board[square] = letter
            if self.check_winner(square, letter):
                self.current_winner = letter
            return True
        return False

    def check_winner(self, square, letter):
        """
        Checks if placing the given letter on the square results in a win.

        A win is determined by checking:
        - The row containing the square
        - The column containing the square
        - Both diagonals (if applicable)

        Args:
            square (int): The index where the last move was made.
            letter (str): The player's letter to check for a winning line.

        Returns:
            bool: True if the player wins with this move, False otherwise.
        """
        # Check row
        row_index = square // self.ROWS
        row_start = row_index * self.ROWS
        row = self.board[row_start : row_start + self.ROWS]
        if all([spot == letter for spot in row]):
            return True

        # Check column
        col_index = square % self.COLS
        column = [self.board[col_index + i * self.COLS] for i in range(self.ROWS)]
        if all([spot == letter for spot in column]):
            return True

        # Check diagonals (only if the square is an even index)
        if square % 2 == 0:
            # Left-to-right diagonal
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True

            # Right-to-left diagonal
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        return False
