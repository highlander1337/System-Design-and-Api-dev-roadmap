import math
import random

class Player:
    """
    Abstract base class for players in a Tic Tac Toe game.
    
    All player subclasses should implement the `get_move` method
    to decide their next move based on the current game state.
    """
    def __init__(self):
        pass

    def get_move(self, game):
        """
        Determines the player's move.

        Args:
            game (TicTacToe): The current game instance.

        Returns:
            int: The index (0-8) of the player's chosen move.
        """
        pass


class RandomComputerPlayer(Player):
    """
    A simple AI player that chooses a move randomly from available positions.
    """
    def __init__(self):
        super().__init__()

    def get_move(self, game):
        """
        Randomly selects a valid move from the available empty squares.

        Args:
            game (TicTacToe): The current game instance.

        Returns:
            int: A randomly chosen valid move (0-8).
        """
        square = random.choice(game.available_moves())  # Random legal move
        return square


class HumanPlayer(Player):
    """
    A human player that interacts with the game via terminal input.
    """
    def __init__(self):
        super().__init__()

    def get_move(self, game):
        """
        Prompts the human player for input and validates it.
        Ensures the move is an integer within the valid range and that
        the square is not already occupied.

        Args:
            game (TicTacToe): The current game instance.

        Returns:
            int: A valid, user-selected move (0-8).
        """
        valid_square = False
        move = None
        while not valid_square:
            square = input('Your turn. Input move (0-8):\n')
            try:
                move = int(square)  # Try to parse the input
                if move not in game.available_moves():
                    raise ValueError  # Invalid if square is occupied or out of bounds
                valid_square = True  # Valid move
            except ValueError:
                print('Invalid or occupied square. Try again.')  # Ask again
        return move
