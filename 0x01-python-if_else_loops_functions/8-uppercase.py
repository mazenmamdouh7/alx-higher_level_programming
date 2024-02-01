#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord(char) >= 65 and ord(char) <= 90:
            char = chr(ord(char))
            print("{}".format(chr(ord(char))), end="")
    print(" ")
