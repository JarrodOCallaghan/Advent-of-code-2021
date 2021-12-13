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
# 1:2
# 7:3
# 4:4
# 8:7

# We need to work out these based on guesses
# 2:5
# 3:5
# 5:5
# 0:6
# 6:6
# 9:6

# For part A, we won't need to crack anything, we can just get len(item)
# In the output string
counter = 0
# print(a)
for combination in a:
    for item in combination[1]:
        print(len(item))
        if len(item) == 2:
            counter += 1
        if len(item) == 3:
            counter += 1
        if len(item) == 4:
            counter += 1
        if len(item) == 7:
            counter += 1

print(counter)
# for item in a:
#    # Each item consists of item[0] as encoding and item[1] as output
#    # TODO: Work out the encoding and decode the output
#    print(f'encoding: {item[0]}\noutput" {item[1]}')
#    encoding = [[0,""],[1,""]]
