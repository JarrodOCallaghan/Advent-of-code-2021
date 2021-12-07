import dataset
import datasetTest

a = dataset.main()

coord_dict = {}

for path in a:
    start = path[0]
    end = path[1]
    # print(f'start: x:{start[0]}, y:{start[1]}')
    # print(f'end: x:{end[0]}, y:{end[1]}')
    # coord_str = "(" + str(start[0]) + ","+ str(start[1]) + ")>("+ str(end[0]) + ","+ str(end[1]) + ")"

    start_x = 0
    end_x = 0
    if start[0] > end[0]:
        start_x = end[0]
        end_x = start[0]
    else:
        start_x = start[0]
        end_x = end[0]

    start_y = 0
    end_y = 0
    if start[1] > end[1]:
        start_y = end[1]
        end_y = start[1]
    else:
        start_y = start[1]
        end_y = end[1]

    # print(f'{start_x}, {start_y}...{end_x},{end_y}')

    # To begin, only consider straight lines
    # E.g. start_x == end_x

    if start == end:
        print("NEW PATH:")
        coord_string = str(start_x) + "," + str(start_y)
        print(coord_string)
        try:
            coord_dict[coord_string] += 1
        except (KeyError):
            # Key doesn't exist, so we create one
            coord_dict[coord_string] = 1
    else:
        if start_x == end_x:
            print("NEW PATH:")
            # Adding one to range because range() is annoying and does end_y -1
            for y in range(start_y, end_y + 1):
                coord_string = str(start_x) + "," + str(y)
                print(coord_string)
                try:
                    coord_dict[coord_string] += 1
                except (KeyError):
                    # Key doesn't exist, so we create one
                    coord_dict[coord_string] = 1

        if start_y == end_y:
            print("NEW PATH:")
            for x in range(start_x, end_x + 1):
                coord_string = str(x) + "," + str(start_y)
                print(coord_string)
                try:
                    coord_dict[coord_string] += 1
                except (KeyError):
                    # Key doesn't exist, so we create one
                    coord_dict[coord_string] = 1
    print("\n")

counter = 0
for key in coord_dict:
    if coord_dict[key] > 1:
        counter += 1
        # print(key)
        # print(coord_dict[key])
print(counter)
