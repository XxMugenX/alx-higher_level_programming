#!/usr/bin/python3
if __name__ == "__main__":

    from add_0 import add

    """imports add function from file and sums up two numbers"""

    a = 1
    b = 2
    print("{0} + {1} = {2}".format(a, b, add(a, b)))
