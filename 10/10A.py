import dataset
import datasetTest

a = dataset.main()
score = {")": 3, "]": 57, "}": 1197, ">": 25137}
calc = {")": 0, "]": 0, "}": 0, ">": 0}
for line in a:
    char_queue = ""

    for char in line:
        is_close = False
        if char == "}":
            if char_queue[-1] == "{":
                char_queue = char_queue[:-1]
                is_close = True
            else:
                print(f"Syntax error {char}")
                print(char_queue[-1])
                calc["}"] += 1
                break
        elif char == ")":
            if char_queue[-1] == "(":
                is_close = True
                char_queue = char_queue[:-1]
            else:
                print(f"Syntax error {char}")
                print(char_queue[-1])
                calc[")"] += 1
                break

        elif char == ">":
            if char_queue[-1] == "<":
                is_close = True
                char_queue = char_queue[:-1]
            else:
                print(f"Syntax error {char}")
                print(char_queue[-1])
                calc[">"] += 1
                break
        elif char == "]":
            if char_queue[-1] == "[":
                is_close = True
                char_queue = char_queue[:-1]
            else:
                print(f"Syntax error {char}")
                print(char_queue[-1])
                calc["]"] += 1
                break
        if is_close is False:
            char_queue += char

        # print(char_queue)
sum = 0
print(f'() {calc[")"]}')
print(f'[] {calc["]"]}')
print("{}", f'{calc["}"]}')
print(f'<> {calc[">"]}')


print(f"")
sum += calc[")"] * score[")"]
sum += calc[">"] * score[">"]
sum += calc["}"] * score["}"]
sum += calc["]"] * score["]"]
print(sum)
# We could use recursion to work out the first one that breaks
