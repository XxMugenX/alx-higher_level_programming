#!/usr/bin/python3
for i in range(97, 123):
    if chr(i) == "q" or chr(i) == "e":
        print(end="")
    else:
        print("{0}".format(chr(i)), end="")
