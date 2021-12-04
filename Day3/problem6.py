import copy

def main():
    with open('./input3.txt', 'r') as input:
        data = input.readlines()
        dataCopyOGR = copy.deepcopy(data)
        dataCopyCO2SR = copy.deepcopy(data)
        for i in range(0,12):
            dataCopyOGR = copy.deepcopy(dataCopyOGR)
            commonInt = str(findCommonInt(dataCopyOGR, i))
            for line in data:
                if line[i] != commonInt and line in dataCopyOGR:
                    dataCopyOGR.remove(line)
            if len(dataCopyOGR) == 1:
                break
        for i in range(0,12):
            dataCopyCO2SR = copy.deepcopy(dataCopyCO2SR)
            UCommonInt = '0' if findCommonInt(dataCopyCO2SR, i) == 1 else '1'
            for line in data:
                if line[i] != UCommonInt and line in dataCopyCO2SR:
                    dataCopyCO2SR.remove(line)
            if len(dataCopyCO2SR) == 1:
                break

        print(f'Oxygen Generator Rating: {dataCopyOGR[0]}, {int(dataCopyOGR[0], 2)}')
        print(f'CO2 Scrubber Rating: {dataCopyCO2SR[0]}, {int(dataCopyCO2SR[0], 2)}')
        print(f'Multiplied: {int(dataCopyCO2SR[0], 2) * int(dataCopyOGR[0], 2)}')
        

def findCommonInt(data, position):
    c0 = 0
    c1 = 0
    for line in data:
        if line[position] == '0':
            c0 += 1
        else:
            c1 += 1
    return 0 if c0 > c1 else 1

if __name__ == "__main__":
    main()