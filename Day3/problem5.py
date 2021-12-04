def main():
    with open('./input3.txt', 'r') as input:
        sgammaRate = '000000000000'
        sepsilonRate = '000000000000'
        gammaRate = list(sgammaRate)
        epsilonRate = list(sepsilonRate)
        data = input.readlines()
        # Inefficent algorithm, but quick to write
        for i in range(0, 12):
            onecounter = 0
            zerocounter = 0
            for line in data:
                if line[i] == '0':
                    zerocounter += 1
                else:
                    onecounter += 1
            if onecounter > zerocounter:
                gammaRate[i] = '1'
            else:
                gammaRate[i] = '0'

        for i in range(0, 12):
            if gammaRate[i] == '1':
                epsilonRate[i] = '0'
            else:
                epsilonRate[i] = '1'

        sgammaRate = ''.join(gammaRate)
        sepsilonRate = ''.join(epsilonRate)
        print(f'Gamma rate: {int(sgammaRate, 2)}, Epsilon rate: {int(sepsilonRate, 2)}, Multiplied: {int(sgammaRate, 2) * int(sepsilonRate, 2)}')

if __name__ == "__main__":
    main()