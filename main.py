class XO:
    def __init__(self):
        self.square = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for s in range(3):
            for k in range(3):
                self.square[s][k] = s * 3 + k + 1

    def area(self):
        for i in range(3):
            for j in range(3):
                print(self.square[i][j], end=" ")
            print()

    def replacement(self, symbol):
        try:
            while True:
                self.area()
                num = int(input(f"Enter {symbol}: "))
                if num < 1 or num > 9:
                    raise ValueError
                i = (num - 1) // 3
                j = (num - 1) % 3
                if isinstance(self.square[i][j], int):
                    self.square[i][j] = symbol
                    return
                else:
                    print("The cell is busy")
        except ValueError:
            print("Enter integer 1 to 9")
            self.replacement(symbol)

    def winner(self):
        if self.square[0][0] == self.square[0][1] == self.square[0][2] or \
                self.square[1][0] == self.square[1][1] == self.square[1][2] or \
                self.square[2][0] == self.square[2][1] == self.square[2][2] or \
                self.square[0][0] == self.square[1][0] == self.square[2][0] or \
                self.square[0][1] == self.square[1][1] == self.square[2][1] or \
                self.square[0][2] == self.square[1][2] == self.square[2][2] or \
                self.square[0][0] == self.square[1][1] == self.square[2][2] or \
                self.square[0][2] == self.square[1][1] == self.square[2][0]:
            return self.square[0][0]

    def draw(self):
        for i in self.square:
            for j in i:
                if not isinstance(j, str):
                    return False
        return True

    def check_game_end(self, symbol):
        if self.draw():
            self.area()
            print("Draw")
            return True
        if self.winner():
            self.area()
            print(f"Winner {symbol}")
            return True
        return False

    def play(self):
        while True:
            self.replacement("X")
            if self.check_game_end("X"):
                break
            self.replacement("O")
            if self.check_game_end("0"):
                break


if __name__ == '__main__':
    game = XO()
    game.play()
