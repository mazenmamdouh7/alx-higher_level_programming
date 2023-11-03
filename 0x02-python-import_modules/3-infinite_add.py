#!/usr/bin/python3
if __name__ == "__main__":

    import sys

    total_arguments = 0

    for num in range(len(sys.argv) - 1):
        total_arguments += int(sys.argv[num + 1])

    print("{}".format(total_arguments))
