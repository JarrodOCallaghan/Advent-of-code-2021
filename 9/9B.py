import dataset
import datasetTest


class Map:
    def __init__(self):
        a = dataset.main()
        self.a = []
        for number in a:
            temp = []
            formatted = str(number)
            for char in formatted:
                temp.append([int(char), False])
            number = temp
            self.a.append(number)
        self.height = len(self.a)
        self.width = len(self.a[0])
        print(f"{self.height}x{self.width}")
        self.found_basin = []

    def get_basins(self, current=None):
        # Start at 0,0
        # Create a list which each item will be basin area
        # A basin is surrounded by 9's
        basins = []
        current = None
        for i in range(self.height):
            for j in range(self.width):
                current = self.a[i][j]
                if current[1] is False and current[0] < 9:
                    # we will give it the coords
                    # Only if we haven't visited it
                    if self.found_basin != []:
                        self.found_basin = []
                    self.traverse(i, j)
                    basins.append(self.found_basin)
        basins.sort(key=len, reverse=True)
        for basin in basins:
            print(f"Basin size: {len(basin)}")
        # Because i'm lazy:
        answer = len(basins[0]) * len(basins[1]) * len(basins[2])
        print(answer)

    def traverse(self, i, j):
        # Stealing I and J from the get_basins loop
        current = self.a[i][j]
        # print(current)
        # We have now been here
        current[1] = True
        # Get its neighbour nodes
        left = j - 1
        right = j + 1
        up = i - 1
        down = i + 1
        # Check that the next item is in list bounds
        # Then go to next item
        if left >= 0:
            # Only go to next if we haven't been there
            left_node = self.a[i][left]
            if left_node[1] is False and left_node[0] != 9:
                self.traverse(i, left)
        if right < self.width:
            right_node = self.a[i][right]
            if right_node[1] is False and right_node[0] != 9:
                self.traverse(i, right)
        if up >= 0:
            up_node = self.a[up][j]
            if up_node[1] is False and up_node[0] != 9:
                self.traverse(up, j)
        if down < self.height:
            down_node = self.a[down][j]
            if down_node[1] is False and down_node[0] != 9:
                self.traverse(down, j)
        # So we are now getting the correct data. lets append temp:
        self.found_basin.append(current)


def main():
    map = Map()
    map.get_basins()


main()
