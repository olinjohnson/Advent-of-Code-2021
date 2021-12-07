import json
import copy

# Really inefficient algorithm, but it works!
def main():
    with open('./input6.json') as file:
        data = json.load(file)
        dayCount = 256
        newData = copy.deepcopy(data)
        for day in range(0, dayCount):
            print(day)
            newData = simulateFish(newData)
        print(len(newData))

def simulateFish(fish):
    newFish = copy.deepcopy(fish)
    for i in range(0, len(fish)):
        if int(fish[i]) == 0:
            newFish[i] = 6
            newFish.append(8)
        else:
            newFish[i] = int(fish[i]) - 1
    
    return newFish


if __name__ == "__main__":
    main()