from player import HumanPlayer, RandomComputerPlayer
from tic_tac_toe import TicTacToe

def play(game, x_player, o_player, print_game=True):
    """
    The main game loop. Alternates between players until the game ends.
    
    Args:
        game (TicTacToe): The game instance.
        x_player (Player): The player using 'x'.
        o_player (Player): The player using 'o'.
        print_game (bool): If True, prints the board and status messages.

    Returns:
        str or None: The winner ('x' or 'o') or None in case of a tie.
    """
    if print_game:
        game.print_board_nums()

    letter = 'x'  # Starting player

    # Loop until there are no empty squares left
    while game.empty_squares():
        # Get the appropriate player
        current_player = x_player if letter == 'x' else o_player

        # Ask the player for their move
        square = current_player.get_move(game)

        # Make the move
        game.make_move(square, letter)

        if print_game:
            print(f"{letter.upper()} makes a move to square {square}")
            game.print_board()
            print('')  # spacing

        # Check if the game has been won
        if game.current_winner:
            if print_game:
                print(letter.upper() + " wins!")
            return letter  # End the game

        # Switch players
        letter = 'o' if letter == 'x' else 'x'

    if print_game:
        print("It's a tie!")

    return None


if __name__ == "__main__":
    game = TicTacToe()
    x_player = HumanPlayer()
    o_player = RandomComputerPlayer()
    print("tic-tac-toe game, human vs computer!")
    print("human - x")
    print("computer - o")
    play(game, x_player, o_player)