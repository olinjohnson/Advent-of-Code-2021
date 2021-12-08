import json

# Inefficient Algorithm, really slow - but it works
def main():
    with open('./input7.json') as file:
        data = json.load(file)
        lowestSum = None
        for i in range(min(data), max(data) + 1):
            sum = 0
            for p in data:
                sum += calcFuelCost(i, p) if p > i else calcFuelCost(p, i)
            if not lowestSum or sum < lowestSum:
                lowestSum = sum
        print(lowestSum) 

def calcFuelCost(low, high):
    cost = 0
    for i in range(low, high + 1):
        cost += i - low
    return cost

if __name__ == "__main__":
    main()