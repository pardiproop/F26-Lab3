# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Pardip Rooprai
# Date: 10/02/2026
# Purpose: 
# Usage: ./lab3f.py

# Follow the specific instructions given in the README.md file
matrix = [
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]
]

element = matrix[1][2]  # Output: 6
print("The element in the second row and column is ",matrix[1][2])
for i in matrix:
    print(i)

element = matrix[1][1]  # Output: 5
print("The element in the second row and column is ",matrix[1][1])
for i in matrix:
    print(i)

element = matrix[0][1]  # Output: 2
print("The element in the first row and second column is ",matrix[0][1])
for i in matrix:
    print(i)

element = matrix[2][2]  # Output: 9
print("The element in the second row and second column is ",matrix[2][2])
for i in matrix:
    print(i)

for i in range(3):
    print(matrix[i])

print()

