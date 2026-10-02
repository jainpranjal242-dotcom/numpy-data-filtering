import numpy as np

# NumPy Data Filtering - VEDA Technology, Level 1 Day 13

data = np.array([25, 40, 55, 60, 72, 85, 90, 45, 30, 65])

print("Original Data:", data)
print("Values above 50:", data[data > 50])
print("Values below 50:", data[data < 50])
print("Values equal to 60:", data[data == 60])
print("Values above 70:", data[data > 70])
print("Values >= 60:", data[data >= 60])
