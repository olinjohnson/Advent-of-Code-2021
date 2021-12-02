def main():
    depth = 0
    hPos = 0
    aim = 0
    with open('./input2.txt', 'r') as input:
        data = input.readlines()
        for line in data:
            command = line.split(' ')
            if command[0] == 'forward':
                hPos += int(command[1])
                depth += aim * int(command[1])
            elif command[0] == 'up':
                aim -= int(command[1])
            elif command[0] == 'down':
                aim += int(command[1])
        
    print(f'Depth: {depth}, Horizontal position: {hPos}, Aim: {aim}, Multiplied: {hPos * depth}')

if __name__ == "__main__":
    main()