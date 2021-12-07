import json
import copy

def main():
    with open('./input6.json') as file:
        data = json.load(file)
        dayCount = 256
        fishNums = [0,0,0,0,0,0,0,0,0]
        for val in data:
            fishNums[int(val)] += 1
        newFishNums = copy.deepcopy(fishNums)
        for day in range(0, dayCount):
            currentFishNums = [0,0,0,0,0,0,0,0,0]
            for i in range(0, 9):
                if i == 0:
                    currentFishNums[8] += int(newFishNums[0])
                    currentFishNums[6] += int(newFishNums[0])
                else:
                    try:
                        currentFishNums[i-1] += int(newFishNums[i])
                    except:
                        pass
            newFishNums = copy.deepcopy(currentFishNums)

        print(sum(newFishNums))
if __name__ == "__main__":
    main()