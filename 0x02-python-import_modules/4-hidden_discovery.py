#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import hidden_4
    char = 0
    while char <= dir(hidden_4):
        if char[:2] != "__":
            print(char)
