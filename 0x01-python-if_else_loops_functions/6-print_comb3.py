#!/usr/bin/python3
for x in range(0, 10):
    for y in range(0, 10):
        if y <= x:
            pass
        else:
            print(f"{x}{y}, ",end="")
