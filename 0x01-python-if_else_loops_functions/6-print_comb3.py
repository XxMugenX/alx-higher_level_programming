#!/usr/bin/python3
for x in range(0, 10):
    for y in range(0, 10):
        if y == 9 and x == 8:
            print(f"{x}{y}")
        elif y <= x:
            pass
        else:
            print(f"{x}{y}, ",end="")
