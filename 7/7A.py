import dataset
import datasetTest

a = dataset.main()
a.sort()
length = len(a)
median_index = 0
if length % 2 != 0:
    # Potential for rounding issue
    median_index = int(length/2 - 0.5)
else:
    median_index = int(length/2)
print(a[median_index])
median = a[median_index]

fuel_count = 0

for number in a:
    print(f'Move from {number} to {median}: {abs(number-median)} fuel')
    fuel_count += abs(number - median)
print(length)
print(fuel_count)
