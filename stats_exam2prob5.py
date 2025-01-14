import pandas as pd
import statistics as st


data = []
data = pd.read_csv('/Users/andrewtrepagnier/Documents/Temp_Scripts/data_ext', header=None)


total = 0
var = 0
values = []  
part_e = 0

for index, row in data.iterrows():
    if index >= 25:
        break
    row_sum = row.sum()
    total += row_sum
    values.append(row_sum)  
    
    print(f"Sum of line {index + 1}: {row_sum}")

        # PART E
    if row_sum < 5000:
            part_e += 1
# Calculate Mean
mean = total / 25

# Calculate variance 
var = 0
for value in values:
    var += (value - mean)**2
var = var / 24       
#Sorting algorithm is based on a script i once made with java converted over to python. 

n = len(values)
for j in range(n, 1, -1):
    for i in range(j - 1):
        if values[i] > values[i + 1]:
            tmp = values[i]
            values[i] = values[i + 1]
            values[i + 1] = tmp

#  median
if n % 2 == 0:
    median = (values[n//2 - 1] + values[n//2]) / 2
else:
    median = values[n//2]

# Print all statistics
print(f"\nPoint Estimate Mean: {mean}")
print(f"\nPoint Estimate Variance: {var}")
print(f"\nPoint Estimate STD: {var**(1/2)}")
print(f"\nStandard Error [s/sqrt(n)]: {var**(1/2) / (25)**(1/2)}")
print(f"\nMedian: {median}")
print(f"\nLess than 5000 points: {part_e}")
print(f"\nProportion less than 5000: {part_e / 25}")
print(f"\nTotal sum of all numbers: {total}")
