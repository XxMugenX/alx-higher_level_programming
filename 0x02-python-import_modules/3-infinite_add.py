#!/usr/bin/python3
import sys
sum = 0
count = sys.argv.__len__()
for i in range(count - 1):
    sum += int(sys.argv[i + 1])
print(f"{sum}")
