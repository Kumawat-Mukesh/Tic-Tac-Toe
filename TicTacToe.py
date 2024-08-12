# Tic Tac Toe using python
# Create a Python console-based Tic Tac Toe game where two players can compete against each other. Players take turns marking spaces on a 3x3 grid  with their respective symbols (X or O), aiming to form a row, column, or diagonal of their symbols. The game detects and announces the winner or a draw, and allows players to play again if desired. Ensure the game handles invalid inputs and provides clear instructions for players.


class TicTacToe:
    def __init__(self):
        # Create a 3x3 grid represented as a list of 9 empty strings
        self.board = [" "] * 9
        # Set the starting player to "X"
        self.current_player = "X"

    def display_board(self):
        # Display the current state of the board
        # Each row of the 3x3 grid is printed with separators
        print(f" {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("---|---|---")
        print(f" {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("---|---|---")
        print(f" {self.board[6]} | {self.board[7]} | {self.board[8]} ")

    def take_move(self, position):
        # Print the symbol on the board if the postion is empty
        if self.board[position] == " ":
            self.board[position] = self.current_player
            return True
        else:
            # Return false if the position is already occupied
            return False

    def change_player(self):
        # Switch the current player from "X" to "O" or vice versa
        self.current_player = "O" if self.current_player == "X" else "X"

    def chek_winner(self):
        # Define all the posibble winning combinations
        winning_combination = [
            (0, 1, 2),
            (3, 4, 5),
            (6, 7, 8),  # Horizontal
            (0, 3, 6),
            (1, 4, 7),
            (2, 5, 8),  # Vertical
            (0, 4, 8),
            (2, 4, 6),  # Diagnoal
        ]

        # Check if any winning combination is match to the current player
        for combination in winning_combination:
            # Check the winning combination is not empty
            if (
                self.board[combination[0]]
                == self.board[combination[1]]
                == self.board[combination[2]]
                != " "
            ):
                return True
        return False

    def board_full(self):
        # Check if the board is full (No any empty spaces left in the board)
        return " " not in self.board


def main():
    game = TicTacToe()
    while True:
        # Display the board
        game.display_board()

        try:
            # Input the current player to choose pa position on the board
            position = (
                int(input(f"Player {game.current_player}, choose a position (1-9) : "))
                - 1
            )

            # Check if the input is valid or not
            if position not in range(9):
                print("Invalid Input ! Please choose a position between 1 to 9")
                continue

            # If the position is occupied in the board , choose another position
            if not game.take_move(position):
                print("This postion is already occupied. Try another one.")
                continue

        except ValueError:
            print("Invalid Input")
            continue
        
        # Check winner
        if game.chek_winner():
            game.display_board()
            print(f"Player {game.current_player} wins!")
            break
        # Check board is fullor not
        if game.board_full():
            game.display_board()
            print("It's a draw!")
            break
        
        # This method change the player from "X" to "O" or vice versa
        game.change_player()

    # If user want to play again 
    if input("Do you want to play again? (y/n)").lower() == "y":
        main()
    else:
        print("Thanks for playing")


if __name__ == "__main__":
    main()
