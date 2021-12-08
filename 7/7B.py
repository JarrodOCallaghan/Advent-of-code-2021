import dataset
import datasetTest
import math

a = dataset.main()
a.sort()
# No need to sort anymore
length = len(a)

# We will brute force a solution
# num_sum += ((d*(d + 1))/2)
# print(f'')
min = a[0]
max = a[-1]
print(min)
print(max)
hor = None
total_fuel = None
print(f'Brute force between {min} and {max}')
for current in range(min, max+1):
    # print(f'\nAlign on: {current}')
    fuel = 0
    for pos in a:

        d = abs(current - pos)
        s = int((d*(d + 1))/2)
        fuel += s
        # print(f'Distance from {current} to {pos}: {d}. Spent: {s}')
        # print(f'Fuel Spent: {s}')

    # print(f'Fuel: {fuel}')
    if hor is None:
        hor = current
        total_fuel = fuel
    if fuel < total_fuel:
        hor = current
        total_fuel = fuel


print(f'pos: {hor}, fuel: {total_fuel}')
