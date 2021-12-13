import dataset
import datasetTest

a = dataset.main()

mapping = {
    "0": [True, True, True, True, True, True, False],
    "1": [False, True, True, False, False, False, False],
    "2": [True, True, False, True, True, False, True],
    "3": [True, True, True, True, False, False, True],
    "4": [False, True, True, False, False, True, True],
    "5": [False, True, False, True, True, False, True, True],
    "6": [False, True, False, True, True, True, True, True],
    "7": [False, True, True, True, False, False, False, False],
    "8": [False, True, True, True, True, True, True, True],
    "9": [False, True, True, True, True, False, True, True],
}
# We can guess these ones
# 1:2 - Done
# 7:3 - Done
# 4:4 - Done
# 8:7 - Done
# They will all share the right side

# We need to work out these based on guesses
# 2:5 -
# 3:5 - Done
# 5:5
# 0:6
# 6:6
# 9:6 - Done

# Can deduce 9 from 8, will reveal E
# Can deduce 3 from 9, will reveal F
# May be able to deduce 2 from 9 and 8, could find C


#    AAA
#   F   B
#   F   B
#    GGG
#   E   C
#   E   C
#    DDD
sum = 0
for combination in a:
    # Here we need to decode each output before pushing to the next:
    encoding = {
        "A": None,
        "B": None,
        "C": None,
        "D": None,
        "E": None,
        "F": None,
        "G": None,
    }
    found_numbers = {
        "0": None,
        "1": None,
        "2": None,
        "3": None,
        "4": None,
        "5": None,
        "6": None,
        "7": None,
        "8": None,
        "9": None,
    }
    found = False
    while not found:
        # Once we find all encoding we are good
        for signal_pattern in combination[0]:
            signal_pattern
            if len(signal_pattern) == 2 and found_numbers["1"] is None:
                found_numbers["1"] = signal_pattern
                print(f"Found: 1 : {sorted(signal_pattern)}")
            if len(signal_pattern) == 4 and found_numbers["4"] is None:
                found_numbers["4"] = signal_pattern
                print(f"Found: 4 : {sorted(signal_pattern)}")
            if len(signal_pattern) == 3 and found_numbers["7"] is None:
                found_numbers["7"] = signal_pattern
                print(f"Found: 7 : {sorted(signal_pattern)}")
            if len(signal_pattern) == 7 and found_numbers["8"] is None:
                found_numbers["8"] = signal_pattern
                print(f"Found: 8 : {sorted(signal_pattern)}")

            if len(signal_pattern) == 5:
                if found_numbers["1"] is not None and found_numbers["3"] is None:
                    contains = True
                    for char in found_numbers["1"]:
                        if char not in signal_pattern:
                            contains = False
                    if contains is True:
                        found_numbers["3"] = signal_pattern
                        print(f"Found: 3 : {sorted(signal_pattern)}")

                if found_numbers["6"] is not None and found_numbers["3"] is not None:
                    contains = True
                    if signal_pattern != found_numbers["3"]:
                        for char in signal_pattern:
                            if char not in found_numbers["6"]:
                                contains = False
                        if contains is True and found_numbers["5"] is None:
                            found_numbers["5"] = signal_pattern
                            print(f"Found: 5 : {sorted(signal_pattern)}")
                        if contains is False and found_numbers["2"] is None:
                            found_numbers["2"] = signal_pattern
                            print(f"Found: 2 : {sorted(signal_pattern)}")

            if len(signal_pattern) == 6:
                if found_numbers["4"] is not None:
                    # 9:6
                    four_in_number = True
                    for char in found_numbers["4"]:
                        if char not in signal_pattern:
                            four_in_number = False
                    if four_in_number is True and found_numbers["9"] is None:
                        found_numbers["9"] = signal_pattern
                        print(f"Found: 9 : {sorted(signal_pattern)}")
                if (
                    found_numbers["9"] is not None
                    and found_numbers["1"] is not None
                    and signal_pattern != found_numbers["9"]
                ):
                    # 0:6
                    contains_number = True
                    for char in found_numbers["1"]:
                        if char not in signal_pattern:
                            contains_number = False
                    if contains_number is True and found_numbers["0"] is None:
                        found_numbers["0"] = signal_pattern
                        print(f"Found: 0 : {sorted(signal_pattern)}")
                    if contains_number is False and found_numbers["6"] is None:
                        # 6:6
                        found_numbers["6"] = signal_pattern
                        print(f"Found: 6 : {sorted(signal_pattern)}")
        counter = 0
        for key in found_numbers:
            if found_numbers[key] is not None:
                counter += 1
        if counter == 10:
            found = True
    decoded_numbers = []

    for signal_pattern in combination[1]:
        int_str = ""
        signal_pattern = sorted(signal_pattern)
        for decoded_number in found_numbers:
            match_string = sorted(found_numbers[decoded_number])
            # print(f'Comparing: {signal_pattern} to {match_string}')
            if signal_pattern == match_string:
                decoded_numbers.append(decoded_number)
    print(decoded_numbers)
    for number in decoded_numbers:
        int_str += str(number)
    print(f'Formatted number {int_str}')
    sum += int(int_str)

print(f'Total: {sum}')
