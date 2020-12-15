import sys

try:
    if len(sys.argv) == 2:
        if (int(sys.argv[1])) % 2 == 1:
            print("I'm Odd.")
        elif (int(sys.argv[1])) % 2 == 0:
            print("I'm Even.")
        elif (int(sys.argv[1])) == 0:
            print("I'm zero")
    else:
        print("ERROR")
except:
    print("ERROR")