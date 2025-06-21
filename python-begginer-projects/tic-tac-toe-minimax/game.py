from player import HumanPlayer, GeniusComputerPlayer
from tic_tac_toe import TicTacToe

def play(game, player_1, player_2, print_game=True):
    """
    The main game loop. Alternates between players until the game ends.
    
    Args:
        game (TicTacToe): The game instance.
        player_1 (Player): The first player.
        player_2 (Player): The second player.
        print_game (bool): If True, prints the board and status messages.

    Returns:
        str or None: The winner or None in case of a tie.
    """
    if print_game:
        game.print_board_nums()

    letter = player_1.get_letter()  # Starting player

    # Loop until there are no empty squares left
    while game.empty_squares():
        # Get the appropriate player
        current_player = player_1 if letter == player_1.get_letter() \
            else player_2

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
        letter = player_2.get_letter() if letter == player_1.get_letter() \
            else player_1.get_letter()

    if print_game:
        print("It's a tie!")

    return None


if __name__ == "__main__":
    game = TicTacToe()
    x_player = HumanPlayer('x')
    o_player = GeniusComputerPlayer('o', x_player.get_letter())
    print("tic-tac-toe game, human vs computer!")
    print("human - x")
    print("computer - o")
    play(game, x_player, o_player)