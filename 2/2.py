# Forward 1 - forward x
# Down X
# Up X
#Q1
import dataset

data = dataset.main()


hor = 0
ver = 0
#
#for item in data:
#    if item[0] == "forward":
#        hor += item[1]
#    if item[0] == "up":
#        ver -= item[1]
#    if item[0] == "down":
#        ver += item[1]
#ans = hor * ver
# ANS 1
#print(hor)
#print(ver)
#print(ans)


# Q2
aim = 0

subset = [
["forward", 5],
["down",5],
["forward",8],
["up",3],
["down",8],
["forward",2]
]


for item in data:
    if item[0] == "forward":
        hor += item[1]
        x = aim * item[1]
        ver += x
        print(f'{hor}x{ver}. aim {aim}')
    if item[0] == "up":
        aim -= item[1]
        print(f'{hor}x{ver}. aim {aim}')
    if item[0] == "down":
        aim += item[1]
        print(f'{hor}x{ver}. aim {aim}')

ans = hor * ver
print(f'Hor: {hor}  x vert {ver}')
print(ans)
