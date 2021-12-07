import dataset
import datasetTest

a = dataset.main()

coord_dict = {}

for path in a:
    start = path[0]
    end = path[1]

    x1 = start[0]
    y1 = start[1]

    x2 = end[0]
    y2 = end[1]

    # Single point:
    if x1 == x2 and y1 == y2:
        coord_string = str(x1) + "," + str(y1)
        try:
            coord_dict[coord_string] += 1
        except (KeyError):
            coord_dict[coord_string] = 1
    # Diagonal case
    if x1 != x2 and y1 != y2:
        x = x1
        y = y1
        while x != x2 and y != y2:
            coord_string = str(x) + "," + str(y)
            try:
                coord_dict[coord_string] += 1
            except (KeyError):
                # Key doesn't exist, so we create one
                coord_dict[coord_string] = 1
            if x < x2:
                x += 1
            elif x > x2:
                x -= 1
            if y < y2:
                y += 1
            elif y > y2:
                y -= 1
        # Need to run through once more
        coord_string = str(x) + "," + str(y)
        try:
            coord_dict[coord_string] += 1
        except (KeyError):
            # Key doesn't exist, so we create one
            coord_dict[coord_string] = 1

    # Linear case

    if start[0] > end[0]:
        start_x = end[0]
        end_x = start[0]
    else:
        start_x = start[0]
        end_x = end[0]

    if start[1] > end[1]:
        start_y = end[1]
        end_y = start[1]
    else:
        start_y = start[1]
        end_y = end[1]
    if start_x == end_x and start_y != end_y:
        # print("NEW PATH:")
        # Adding one to range because range() is annoying and does end_y -1
        for y in range(start_y, end_y + 1):
            coord_string = str(start_x) + "," + str(y)
            # print(coord_string)
            try:
                coord_dict[coord_string] += 1
            except (KeyError):
                # Key doesn't exist, so we create one
                coord_dict[coord_string] = 1

    if start_x != end_x and start_y == end_y:
        # print("NEW PATH:")
        for x in range(start_x, end_x + 1):
            coord_string = str(x) + "," + str(start_y)
            # print(coord_string)
            try:
                coord_dict[coord_string] += 1
            except (KeyError):
                # Key doesn't exist, so we create one
                coord_dict[coord_string] = 1


counter = 0
for key in coord_dict:
    if coord_dict[key] > 1:
        counter += 1
        print(f"{key}: {coord_dict[key]}")
print(counter)
