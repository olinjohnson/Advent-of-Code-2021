import json

def main():
    board = generateBoard(1000)

    with open('./input5.json') as file:
        data = json.load(file)
        for i in data:
            x1 = i[0]
            x2 = i[2]
            y1 = i[1]
            y2 = i[3]
            if x1 == x2:
                bignum = y1 if y1 > y2 else y2
                smallnum = y2 if y1 > y2 else y1
                # Potential error bignum + 1
                for z in range(smallnum, bignum + 1):
                    if board[z][x1] == 0:
                        board[z][x1] = 1
                    elif board[z][x1] == 1:
                        board[z][x1] = 2
            elif y1 == y2:
                bignum = x1 if x1 > x2 else x2
                smallnum = x2 if x1 > x2 else x1
                # Potential error bignum + 1
                for z in range(smallnum, bignum + 1):
                    if board[y1][z] == 0:
                        board[y1][z] = 1
                    elif board[y1][z] == 1:
                        board[y1][z] = 2
    
    twoCounter = 0
    for g in board:
        for h in g:
            if h == 2:
                twoCounter += 1
    
    print(f'TwoCounter: {twoCounter}')

def generateBoard(size):
    b = []
    for i in range(0, size):
        row = []
        for x in range(0, size):
            row.append(0)
        b.append(row)
    
    return b


if __name__ == "__main__":
    main()