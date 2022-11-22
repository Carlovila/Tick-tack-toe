class ticktacktoe():
    def __init__(self):
        """define board"""
        self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    def gameboard(self):
        """display the board"""
        print(f"|{self.board[1]}| |{self.board[2]}| |{self.board[3]}|",
              f"|{self.board[4]}| |{self.board[5]}| |{self.board[6]}|",
              f"|{self.board[7]}| |{self.board[8]}| |{self.board[9]}|", sep="\n")
    def start_game(self, start=1):
        """start the game (1 starts, 0 stops, set default to 1)"""
        if start == 1:
            print("Tick Tack Toe!")
            self.gameboard()
            """x moves first"""
            return self.move_X()
        else:
            """stop if start == 0"""
            return
    def move_X(self):
        """checks if the board is full/it's a tie"""
        if self.tie_check() == False:
            cell = int(input("Player X, choose number 1-9: "))
            if cell not in range(1,10):
                print("Not a valid move")
                return self.move_X()
            player = "X"
            """check if cell is empty before moving"""
            if self.rule_1(cell) == True:
                """writes move"""
                self.board[cell] = "X"
                self.gameboard()
                """checks win condition"""
                if self.win_cond(player) == True:
                    print("Player X wins!")
                    """if yes reset the game"""
                    return self.reset()
                else:
                    """if not move to next player"""
                    return self.move_O()
            else:
                """if cell is not empty"""
                print("Not allowed")
                return self.move_O()
        else:
            print("It's a tie!")
            return self.reset()
    def move_O(self):
        if self.tie_check() == False:
            cell = int(input("Player O, choose number 1-9: "))
            if cell not in range(1,10):
                print("Not a valid move")
                return self.move_O()
            player = "O"
            if self.rule_1(cell) == True:
                self.board[cell] = "O"
                self.gameboard()
                if self.win_cond(player) == True:
                    print("Player O wins!")
                    return self.reset()
                else:
                    return self.move_X()
            else:
                print("Not allowed")
                return self.move_O()
        else:
            print("It's a tie!")
            return self.reset()
    def rule_1(self, cell):
        """checks if cell is empty"""
        if self.board[cell] == " ":
            return True
        else:
            return False
    def tie_check(self):
        """check for tie"""
        tiecheck = self.board[1:]
        if " " in tiecheck:
            return False
        else:
            return True
    def win_cond(self, player):
        """define win conditions"""
        if self.board[1] == player and self.board[2] == player and self.board[3] == player:
            return True
        if self.board[4] == player and self.board[5] == player and self.board[6] == player:
            return True
        if self.board[7] == player and self.board[8] == player and self.board[9] == player:
            return True
        if self.board[1] == player and self.board[4] == player and self.board[7] == player:
            return True
        if self.board[2] == player and self.board[5] == player and self.board[8] == player:
            return True
        if self.board[3] == player and self.board[6] == player and self.board[9] == player:
            return True
        if self.board[1] == player and self.board[5] == player and self.board[9] == player:
            return True
        if self.board[3] == player and self.board[5] == player and self.board[7] == player:
            return True
        else:
            return False
    def reset(self):
        """reset game"""
        reset = input("Play again? (Y/N): ").upper()
        if reset == "Y":
            self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
            return self.start_game()
        elif reset == "N":
            return self.start_game(0)
        else:
            return self.reset()

ticktacktoe().start_game()
print("Githubasd")