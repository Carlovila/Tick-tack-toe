class ticktacktoe():
    def __init__(self):
        """creates the game board"""
        self.board = [" "] * 10
    def gameboard(self):
        """display the board"""
        print(f"|{self.board[1]}| |{self.board[2]}| |{self.board[3]}|",
              f"|{self.board[4]}| |{self.board[5]}| |{self.board[6]}|",
              f"|{self.board[7]}| |{self.board[8]}| |{self.board[9]}|", sep="\n")
    def startgame(self, start=1):
        """starts the game with player X"""
        if start == 1:
            print("Tick-tack-toe!")
            self.gameboard()
            return self.move("X")
        else:
            return
    def tie_check(self):
        """checks for tie"""
        tiecheck = self.board[1:]
        if " " in tiecheck:
            return False
        else:
            return True
    def rule_1(self, cell):
        """checks if cell is empty"""
        if self.board[cell] == " ":
            return True
        else:
            return False
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
        try:
            reset = input("Play again? (Y/N): ").upper()
        except ValueError:
            print("not valid")
            return self.reset()
        if reset == "Y":
            self.board = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
            return self.startgame()
        elif reset == "N":
            return self.startgame(0)
        else:
            print("Not valid")
            return self.reset()
    def move(self, player):
        self.player = player
        """check if it's tie"""
        if self.tie_check() == False:
            """enters move to be played"""
            try:
                cell = int(input(f"Player {player}, choose number 1-9: "))
            except ValueError:
                print("Not valid")
                return self.move(player)
            if cell not in range(1,10):
                print("Not valid")
                return self.move(player)
            """check if cell is already filled"""
            if self.rule_1(cell) == True:
                """updates move"""
                self.board[cell] = player
                self.gameboard()
                """checks win conditions"""
                if self.win_cond(player) == True:
                    print(f"Player {player} wins!")
                    return self.reset()
                else:
                    """moves to next player"""
                    if player == "X":
                        return self.move("O")
                    else:
                        return self.move("X")
            else:
                print("Not allowed")
                return self.move(player)
        else:
            print("It's a tie!")
            return self.reset()

"""run the game"""
ticktacktoe().startgame()
