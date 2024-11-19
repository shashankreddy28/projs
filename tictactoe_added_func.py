class TicTacToe:
    def __init__(self):
        self.board = [' '] * 9  # Represent the board as a list of 9 spaces
        self.current_player = 'X'  # X always starts

    def display_template(self):
        print("\nHere is the template for reference:")
        print("\t 1 | 2 | 3 ")
        print("\t---|---|---")
        print("\t 4 | 5 | 6 ")
        print("\t---|---|---")
        print("\t 7 | 8 | 9 ")

    def display_board(self):
        print("\nCurrent Board:")
        print(f"\t {self.board[0]} | {self.board[1]} | {self.board[2]} ")
        print("\t---|---|---")
        print(f"\t {self.board[3]} | {self.board[4]} | {self.board[5]} ")
        print("\t---|---|---")
        print(f"\t {self.board[6]} | {self.board[7]} | {self.board[8]} ")

    def is_winner(self):
        # Define win conditions: rows, columns, diagonals
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]              # diagonals
        ]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != ' ':
                return self.board[condition[0]]
        return None

    def is_full(self):
        return ' ' not in self.board

    def make_move(self, position):
        if self.board[position - 1] == ' ':  # Convert 1-based to 0-based index
            self.board[position - 1] = self.current_player
            return True
        return False

    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'

    def minimax(self, is_maximizing):
        winner = self.is_winner()
        if winner =='X':
            return -1
        if winner == 'O':
            return 1
        if self.is_full():
            return 0
        
        if is_maximizing:
            best_score = -19683 # magic number: this is the number of possible tic tac toe board scenarios = 3^9
            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i] = 'O'
                    score = self.minimax(False)
                    self.board[i] = ' '
                    best_score = max(best_score,score)
            return best_score
        else:
            best_score = 19683 # magic number look at comment above
            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i] = 'X'
                    score = self.minimax(True)
                    self.board[i] = ' '
                    best_score = min(score, best_score)
            return best_score

    def cpu_move(self):
        best_score = -19683
        best_move = None
        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = 'O'
                score = self.minimax(False)
                self.board[i] = ' '
                if score > best_score:
                    best_score = score
                    best_move = i
        self.board[best_move] = 'O'

    def play(self):
        self.display_template()
        while True:
            self.display_board()
            if self.current_player == 'X':
                print(f"Player {self.current_player}'s turn.")
                try:
                    move = int(input("Enter the position (1-9): "))
                    if move < 1 or move > 9:
                        raise ValueError
                    if not self.make_move(move):
                        print("Position already taken. Try again.")
                        continue
                except ValueError:
                    print("Invalid input. Enter a number between 1 and 9.")
                    continue
            else:
                print("CPU's turn:")
                self.cpu_move()

            winner = self.is_winner()
            if winner:
                self.display_board()
                print(f"Player {winner} wins!")
                break

            if self.is_full():
                self.display_board()
                print("It's a tie!")
                break

            self.switch_player()


if __name__ == "__main__":
    play_again = "y"
    while play_again == "y":
        game = TicTacToe()
        game.play()
        play_again = input("Would you like to play again? ('y': Yes, anything else: No): ")
