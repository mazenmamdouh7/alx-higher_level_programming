#!/usr/bin/python3
if __name__ == "__main__":
    
    import sys
    
    counter = len(sys.argv)
    if  counter == 0:
        print("0  .")

    elif counter == 1:
        print("1 argument: ")

    else:
        print("{} arguments: ".format(counter))

    for num in range(counter):
        print("{}: {}".format(num+1,sys.argv[num+1]))
