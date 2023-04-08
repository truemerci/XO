square = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for s in range(3):
    for k in range(3):
        square[s][k] = s * 3 + k + 1


def area():
    for i in range(3):
        for j in range(3):
            print(square[i][j], end=" ")
        print()


def replacement(symbol):
    try:
        while True:
            area()
            num = int(input(f"Enter {symbol}: "))
            if num < 1 or num > 9:
                raise ValueError
            for i in range(3):
                for j in range(3):
                    if square[i][j] == num and square[i][j] != "X" and square[i][j] != "O":
                        square[i][j] = symbol
                        return
            print("The cell is busy")
    except ValueError:
        print("Enter integer 1 to 9")
        replacement(symbol)


def winner():
    if square[0][0] == square[0][1] == square[0][2] or \
            square[1][0] == square[1][1] == square[1][2] or \
            square[2][0] == square[2][1] == square[2][2] or \
            square[0][0] == square[1][0] == square[2][0] or \
            square[0][1] == square[1][1] == square[2][1] or \
            square[0][2] == square[1][2] == square[2][2] or \
            square[0][0] == square[1][1] == square[2][2] or \
            square[0][2] == square[1][1] == square[2][0]:
        return True


def draw():
    for i in square:
        for j in i:
            if not isinstance(j, str):
                return False
    return True


if __name__ == "__main__":
    while True:
        replacement("X")
        if draw():
            area()
            print("Draw")
            break
        if winner():
            area()
            print("Winner X")
            break
        replacement("O")
        if draw():
            area()
            print("Draw")
            break
        if winner():
            area()
            print("Winner O")
            break
