import dataset
import datasetTest

a = dataset.main()
# need to format the array here
b = []
for number in a:
    temp = []
    # formatted = str(number)
    for char in formatted:
        temp.append(char)
    number = temp
    b.append(number)

# We will work with the list b in this challenge
height = len(b)
# Assuming that all lines are same length
width = len(b[0])
print(f"h: {height}, w: {width}")
sum = 0
for i in range(height):
    for j in range(width):
        # Scan the array. not very fast tho :(
        # X goes
        current = int(b[i][j])
        is_lower = True
        left = j - 1
        right = j + 1
        up = i - 1
        down = i + 1
        if left >= 0:
            if current >= int(b[i][left]):
                is_lower = False
        if right < width:
            if current >= int(b[i][right]):
                is_lower = False
        if up >= 0:
            if current >= int(b[up][j]):
                is_lower = False
        if down < height:
            if current >= int(b[down][j]):
                is_lower = False
        if is_lower:
            sum += current + 1
print(sum)
