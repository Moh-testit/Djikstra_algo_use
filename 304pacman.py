#!/usr/bin/python3

from sys import *
from tupac import *

def     main():
    if len(argv) !=  4:
        print("Usage: ./304tupac map c1 c2\n")
        exit(84)
    if len(argv) == 4:
        if len(argv[2]) != 1 or len(argv[3]) != 1:
            print("Usage: ./304tupac map c1 c2\n")
            exit(84)
        else:
            obj = tupac(argv)
            obj.computeValue()
            obj.printValue()

if __name__ == "__main__":
    try:
        main()
    except BaseException as error:
        print("\tfile\tfile describing the board, using the following characters:")
        print("\t\t'0' for an empty square,\n\t\t '1' for a wall,")
        print("\t\t 'F' for the ghost’s position,\n\t\t 'P' for tupac’s position.")
        print("\tc1\tcharacter to display for a wall\n\tc2\tcharacter to display for an empty space.")
        exit(84)