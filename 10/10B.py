import dataset
import datasetTest

a = dataset.main()
score = {")": 1, "]": 2, "}": 3, ">": 4}
calc = {")": 0, "]": 0, "}": 0, ">": 0}

scores = []
for line in a:
    sub_calc = {")": 0, "]": 0, "}": 0, ">": 0}
    is_corrupted = False
    char_queue = ""

    for char in line:
        is_close = False
        if char == "}":
            if char_queue[-1] == "{":
                char_queue = char_queue[:-1]
                is_close = True
            else:
                # print(f'Syntax error {char}')
                # print(char_queue[-1])
                calc["}"] += 1
                is_corrupted = True

        elif char == ")":
            if char_queue[-1] == "(":
                is_close = True
                char_queue = char_queue[:-1]
            else:
                # print(f'Syntax error {char}')
                # print(char_queue[-1])
                calc[")"] += 1
                is_corrupted = True

        elif char == ">":
            if char_queue[-1] == "<":
                is_close = True
                char_queue = char_queue[:-1]
            else:
                # print(f'Syntax error {char}')
                # print(char_queue[-1])
                calc[">"] += 1
                is_corrupted = True

        elif char == "]":
            if char_queue[-1] == "[":
                is_close = True
                char_queue = char_queue[:-1]
            else:
                # print(f'Syntax error {char}')
                # print(char_queue[-1])
                calc["]"] += 1
                is_corrupted = True

        if is_close is False:
            char_queue += char
    if is_corrupted is False:
        reversed = char_queue[::-1]
        sum = 0
        # Char queue now contains open strings
        for char in reversed:
            if char == "(":
                sum = sum * 5 + 1
                sub_calc[")"] += 1
            if char == "[":
                sum = sum * 5 + 2
                sub_calc["]"] += 1
            if char == "{":
                sum = sum * 5 + 3
                sub_calc["}"] += 1
            if char == "<":
                sum = sum * 5 + 4
                sub_calc[">"] += 1
        scores.append(sum)
        print(f"{reversed} - {sum} total points.")
scores.sort()
mid = len(scores)
mid = mid / 2 - 0.5
print(scores[int(mid)])

# print(char_queue)
# sum = 0
# print(f'() {calc[")"]}')
# print(f'[] {calc["]"]}')
# print("{}", f'{calc["}"]}')
# print(f'<> {calc[">"]}')


# print(f'')
# sum += calc[")"] * score[")"]
# sum += calc[">"] * score[">"]
# sum += calc["}"] * score["}"]
# sum += calc["]"] * score["]"]
# print(sum)
# We could use recursion to work out the first one that breaks
