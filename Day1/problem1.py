def main():
    counter = 0
    with open('./input1.txt', 'r') as input:
        data = input.readlines()
        for i in range(1, 2000):
            if int(data[i]) > int(data[i-1]):
                counter += 1
    print(f'There are {counter} measurements that are larger than the previous measurement.')
            

if __name__ == "__main__":
    main()