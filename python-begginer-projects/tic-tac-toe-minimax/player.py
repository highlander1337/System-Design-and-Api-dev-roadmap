import math
import random

class Player:
    """
    Abstract base class for players in a Tic Tac Toe game.
    
    All player subclasses should implement the `get_move` method
    to decide their next move based on the current game state.
    """
    def __init__(self, letter):
        self.letter = letter
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
    
    def get_letter(self):
        return self.letter
        """
        Determines the player's letter.
        
        Args:
            None.
        
        Returns:
            str: The player letter assigned at declaration.
        """

class RandomComputerPlayer(Player):
    """
    A simple AI player that chooses a move randomly from available positions.
    """
    def __init__(self, letter):
        super().__init__(letter)

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
    def __init__(self, letter):
        super().__init__(letter)
        

    def get_move(self, game):
        """
        Prompts the human player for input and validates it.
        Ensures the move is an integer within the valid range and that
        the square is not already occupied.

        Args:
            game (TicTacToe): The current game instance.

        Returns:
            int: A valid, user-selected move.
        """
        valid_square = False
        move = None
        while not valid_square:
            square = input(f'Your turn. Input move (0-{game.get_rows()*game.get_cols()-1}):\n')
            try:
                move = int(square)  # Try to parse the input
                if move not in game.available_moves():
                    raise ValueError  # Invalid if square is occupied or out of bounds
                valid_square = True  # Valid move
            except ValueError:
                print('Invalid or occupied square. Try again.')  # Ask again
        return move
    
class GeniusComputerPlayer(Player):
    """
    An intelligent computer player that uses the Minimax algorithm
    to choose the optimal move in a game of Tic Tac Toe.

    Attributes:
        letter (str): The letter assigned to this player ('x' or 'o').
        adversary (str): The letter representing the opponent player.
    """

    def __init__(self, letter, adversary):
        """
        Initializes the GeniusComputerPlayer with its letter and adversary's letter.

        Args:
            letter (str): The player’s letter ('x' or 'o').
            adversary (str): The opposing player’s letter.
        """
        self.adversary = adversary
        super().__init__(letter)

    def get_move(self, game):
        """
        Determines the best move using the Minimax algorithm.

        If it's the first move of the game (i.e., the board is empty), a random
        move is selected to add unpredictability. Otherwise, the algorithm is used.

        Args:
            game (TicTacToe): The current game state.

        Returns:
            int: The index of the best move (0-based).
        """
        if game.num_empty_squares() == game.get_rows() * game.get_cols():
            # Random move if board is completely empty (opening move)
            square = random.choice(game.available_moves())
        else:
            # Use minimax to determine the best possible move
            square = self.minimax(game, self.letter)['position']
        return square

    def minimax(self, game, player):
        """
        Recursive implementation of the Minimax algorithm to evaluate all possible
        future game states and choose the optimal move.

        Args:
            game (TicTacToe): The current game state.
            player (str): The player making the move in this recursion ('x' or 'o').

        Returns:
            dict: A dictionary with:
                  - 'position' (int): The best move index.
                  - 'score' (int): The evaluated score for the move.
        """
        me = self.letter
        adversary = self.adversary if player == me else me

        # Base case: check for terminal states
        if game.current_winner == adversary:
            # Losing state for the current player
            return {
                'position': None,
                'score': 1 * (game.num_empty_squares() + 1) if adversary == me
                        else -1 * (game.num_empty_squares() + 1)
            }
        elif not game.empty_squares():
            # Draw state
            return {'position': None, 'score': 0}

        # Initialize best score based on whether we're maximizing or minimizing
        if player == me:
            best = {'position': None, 'score': -math.inf}  # Try to maximize
        else:
            best = {'position': None, 'score': math.inf}   # Try to minimize

        # Try all possible moves
        for possible_move in game.available_moves():
            # Simulate the move
            game.make_move(possible_move, player)

            # Recurse into the game after the simulated move
            sim_score = self.minimax(game, adversary)

            # Undo the move (backtracking)
            game.board[possible_move] = ' '
            game.current_winner = None
            sim_score['position'] = possible_move

            # Update the best move based on the player's goal (max or min)
            if player == me:
                if sim_score['score'] > best['score']:
                    best = sim_score
            else:
                if sim_score['score'] < best['score']:
                    best = sim_score

        return best
