#!/usr/bin/python3
import sys
count = len(sys.argv) - 1
if count == 0:
    print("0 arguments.")
elif count == 1:
    print(f"{count} argument:")
else:
    print(f"{count} arguments:")
for i in range(count):
    print(f"{i+1}: {sys.argv[i+1]}")
