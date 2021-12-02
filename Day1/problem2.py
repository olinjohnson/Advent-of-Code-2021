def main():
    counter = 0
    lastSum = 0
    with open('./input1.txt', 'r') as input:
        data = input.readlines()
        for i in range(0, 1998):
            currentSum = int(data[i]) + int(data[i+1]) + int(data[i+2])
            if currentSum > lastSum:
                counter += 1
            lastSum = currentSum
    print(f'There are {counter} sums that are larger than the previous sum.')

if __name__ == "__main__":
    main()