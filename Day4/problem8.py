import json
import copy
# Deobfuscated board data into JSON file

def main():
    order = [46,79,77,45,57,34,44,13,32,88,86,82,91,97,89,1,48,31,18,10,55,74,24,11,80,78,28,37,47,17,21,61,26,85,99,96,23,70,3,54,5,41,50,63,14,64,42,36,95,52,76,68,29,9,98,35,84,83,71,49,73,58,56,66,92,30,51,20,81,69,65,15,6,16,39,43,67,7,59,40,60,4,90,72,22,0,93,94,38,53,87,27,12,2,25,19,8,62,33,75]
    with open("./input4boards.json") as file:
        data = json.load(file)
        
        fastestWinArr = None
        fastestWinTime = None

        for x in range(0, len(data)):
            board = data[x]
            CBoard = copy.deepcopy(board)
            for i in range(0, len(order)):
                if order[i] in board:
                    CBoard[CBoard.index(order[i])] = -1
                    if checkForWin(CBoard) == True:
                        if fastestWinTime == None or i > fastestWinTime:
                            fastestWinTime = i
                            fastestWinArr = copy.deepcopy(CBoard)
                        break


        s = 0
        for n in fastestWinArr:
            if n != -1:
                s += n

        print('Sum: ', s)
        print('Multiplied: ', s * order[fastestWinTime])
        


def checkForWin(board):
    #Check rows
    for x in range(0, 5):
        if board[x*5] == -1 and board[x*5 +1] == -1 and board[x*5 +2] == -1 and board[x*5 +3] == -1 and board[x*5 +4] == -1:
            return True

    for x in range(0, 5):
        if board[x] == -1 and board[x + 5] == -1 and board[x + 10] == -1 and board[x + 15] == -1 and board[x + 20] == -1:
            return True

    return False

if __name__ == "__main__":
    main()
