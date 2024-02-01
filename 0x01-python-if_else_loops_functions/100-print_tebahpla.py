#!/usr/bin/python3
x = 0
for char in range(ord("z"), ord("a")-1, -1):
    if char % 2 == 0:
        print("{}".format(chr(char)), end="")
    else:
        print("{}".format(chr(char - x)), end="")
    x = 32
