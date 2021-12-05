import dataset

a = dataset.main()
power = 0
test_subset = [
    "00100",
    "11110",
    "10110",
    "10111",
    "10101",
    "01111",
    "00111",
    "11100",
    "10000",
    "11001",
    "00010",
    "01010",
]

# GAmma is worked out by common bit of each index of input
# Epsilon rate is least common bit, or opposite of gamma
def PartA():
    arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    print(arr[1])
    for item in a:
        for i, char in enumerate(item):

            if char is "1":
                arr[i] = arr[i] + 1
            else:
                arr[i] -= 1

    gamma = ""
    for num in arr:
        if num > 0:
            gamma = gamma + "1"
        elif num < 0:
            gamma = gamma + "0"

    epsilon = ""
    for item in gamma:
        if item is "1":
            epsilon += "0"
        else:
            epsilon += "1"

    print(gamma)
    print(epsilon)
    power = int(gamma, 2) * int(epsilon, 2)
    print(power)


# PART 2
def PartB():
    life_sup = 0
    # Making These strings as we manipulate the binary
    # Only keep numbers matching and stop when we have 1 left
    #oxygen = a
    #co2 = a
    oxygen = a
    co2 = a
    # For each bit array in list
    # Shortcut, we are assuming all binary numbers are same length

    oxygen = FindOxygen(oxygen)
    co2 = FindCO2(co2)
    print(f'Oxygen: {oxygen}, CO2: {co2}')
    life_sup = int(oxygen[0], 2) * int(co2[0], 2)
    print(life_sup)


def FindOxygen(oxygen):
    # TODO: FIX THIS RANGE
    for i in range(len(oxygen[0])):
        counter = 0
        temp = []
        for item in oxygen:
            counter += CommonBit(item[i])
        for item in oxygen:
            if counter > 0 and item[i] == "1":
                temp.append(item)
            elif counter == 0 and item[i] == "1":
                temp.append(item)
            elif counter < 0 and item[i] == "0":
                temp.append(item)
        oxygen = temp
    return oxygen


def FindCO2(co2):
    for i in range(len(co2[0])):
        # While we have more than 1 item in co2
        print("\n")
        print(f'Iteration {i + 1}')
        print(f'List: {co2}')
        counter = 0
        temp = []
        print(f'Length of co2: {len(co2)}')
        for item in co2:
            counter += CommonBit(item[i])
            # Lets inverse the counter
            # This now shows least common bit
        counter = counter * -1
        print(f'Least common bit: {counter}')
        for item in co2:
            if counter < 0 and item[i] == "0":
                temp.append(item)
            elif counter > 0 and item[i] == "1":
                temp.append(item)
            elif counter == 0 and item[i] == "0":
                print("HERE?")
                temp.append(item)
        print(temp)
        if len(co2) > 1:
            co2 = temp
    return co2


def FindMostCommonBitArr(arr):
    # Return a number to represent common bit
    # x > 0, 1 is commmon
    # x = 0, Even 1 and 0
    # x < 0, 0 is common bit
    counter = 0
    for item in arr:
        if item == "1":
            counter += 1
        else:
            counter -= 1


def CommonBit(int):
    if int == "1":
        print(1)
        return 1
    else:
        print(-1)
        return -1


# FindMostCommonBit(["1", "1", "0"])
PartB()
