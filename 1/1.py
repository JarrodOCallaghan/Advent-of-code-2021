import dataset

a = dataset.main()
prev = None
count = 0
for item in a:
    if prev is not None:
        if item > prev:
            count = count + 1
    prev = item

# print(count)


# Three sum window imp
b = []
for index in range(len(a)):
    c = a[index]
    try:
        c += a[index + 1]
        c += a[index + 2]
        b.append(c)
    except:
        # If we run out of data for 3 sum window
        pass

prev = None
count = 0
for item in b:
    if prev is not None:
        if item > prev:
            count = count + 1
    prev = item

print(count)
