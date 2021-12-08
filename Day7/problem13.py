import json

def main():
    with open('./input7.json') as file:
        data = json.load(file)
        lowestSum = None
        for i in range(min(data), max(data) + 1):
            sum = 0
            for p in data:
                sum += p - i if p > i else i - p
            if not lowestSum or sum < lowestSum:
                lowestSum = sum
        print(lowestSum) 



if __name__ == "__main__":
    main()