import random

class ticktacktoe():
    def __init__(self):
        """creates the game board"""
        self.board = [" "] * 10
        
    def gameboard(self):
        """display the board"""
        print("-----------")
        print(f"|{self.board[1]}| |{self.board[2]}| |{self.board[3]}|",
              f"|{self.board[4]}| |{self.board[5]}| |{self.board[6]}|",
              f"|{self.board[7]}| |{self.board[8]}| |{self.board[9]}|", sep="\n")
        print("-----------")
        
    def startgame(self, start=1, pc="N", turn=0, reset=0):
        """starts the game"""
        if start == 1:
            if reset == 0:
                pc = input("Play vs PC? (Y/N): ").upper()
                while pc not in ['Y','N']:
                    print("Not valid")
                    pc = input("Play vs PC? (Y/N): ").upper()
                print("Tick-tack-toe!")
                self.gameboard()
                if pc == "Y":
                    if turn == 0:
                        return self.move_player("X", pc=pc, turn=turn)
                    else:
                        return self.move_pc("X", pc=pc, turn=turn)
                else:
                    return self.move_player("X", pc=pc, turn=turn)
            else:
                print("Tick-tack-toe!")
                if pc == "Y":
                    if turn == 0:
                        return self.move_player("X", pc=pc, turn=turn)
                    else:
                        return self.move_pc("X", pc=pc, turn=turn)
                else:
                    turn = 0
                    return self.move_player("X", pc=pc, turn=turn)
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

    def win_con(self, player):
        b = self.board
        if [player] * 3 == [b[1], b[2], b[3]]:
            return True
        if [player] * 3 == [b[4], b[5], b[6]]:
            return True
        if [player] * 3 == [b[7], b[8], b[9]]:
            return True
        if [player] * 3 == [b[1], b[5], b[9]]:
            return True
        if [player] * 3 == [b[7], b[5], b[3]]:
            return True
        if [player] * 3 == [b[1], b[4], b[7]]:
            return True
        if [player] * 3 == [b[2], b[5], b[8]]:
            return True
        if [player] * 3 == [b[3], b[6], b[9]]:
            return True
        else:
            return False

    def reset(self, pc, turn):
        """reset game"""
        reset = input("Play again? (Y/N): ").upper()
        while reset not in ['Y', 'N']:
            print("Not valid")
            reset = input("Play again? (Y/N): ").upper()
        if reset == "Y":
            self.board = [" "] * 10
            turn = 1 - turn
            return self.startgame(start=1, pc=pc, turn=turn, reset=1)
        else:
            return self.startgame(start=0)

    def move_player(self, player, pc, turn):
        """check if it's tie"""
        if self.tie_check() == False:
            """enters move to be played"""
            try:
                cell = int(input(f"Player {player}, choose number 1-9: "))
                if cell not in range(1,10):
                    print("Not valid")
                    return self.move_player(player=player, pc=pc, turn=turn)
            except ValueError:
                print("Not valid")
                return self.move_player(player=player, pc=pc, turn=turn)
            """check if cell is already filled"""
            if self.rule_1(cell=cell) == True:
                """updates move"""
                self.board[cell] = player
                self.gameboard()
                """checks win conditions"""
                if self.win_con(player=player) == True:
                    print(f"Player {player} wins!")
                    return self.reset(pc=pc, turn=turn)
                else:
                    """moves to next player"""
                    if pc == "Y":
                        if player == "X":
                            return self.move_pc(player="O", pc=pc,turn=turn)
                        else:
                            return self.move_pc(player="X", pc=pc,turn=turn)
                    else:
                        if player == "X":
                            return self.move_player(player="O", pc=pc, turn=turn)
                        else:
                            return self.move_player(player="X", pc=pc, turn=turn)
            else:
                print("Not allowed")
                return self.move_player(player=player, pc=pc, turn=turn)
        else:
            print("It's a tie!")
            return self.reset(pc=pc, turn=turn)

    def move_pc(self, player, pc, turn):
        """pc moves"""
        playable_moves = []
        for i in range(1, len(self.board)):
            if self.board[i] == ' ':
                playable_moves.append(i)
        cell = random.choice(playable_moves)
        self.board[cell] = player
        self.gameboard()
        if self.win_con(player=player) == False:
            if self.tie_check() == False:
                if player == 'X':
                    return self.move_player(player="O", pc=pc, turn=turn)
                else:
                    return self.move_player(player="X", pc=pc, turn=turn)
            else:
                print("It's a tie!")
                return self.reset(pc=pc, turn=turn)
        else:
            print(f"Player {player} wins!")
            return self.reset(pc=pc, turn=turn)

"""run the game"""
ticktacktoe().startgame()
