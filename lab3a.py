# Add comments before you do anything else.

#!/usr/bin/env python3
# Author: Pardip Rooprai
# Date: 10/02/2026
# Purpose: 
# Usage: ./lab3a.py
import random
numbers=[]
for i in range(20):
    number=random.randint(0, 99)
    numbers.append(number)
print("Random Sequence: ")
print(numbers)
numbers.sort()
print("Sorted Sequence: ")
print(numbers)
