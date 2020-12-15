import sys

try:
    if len(sys.argv) == 3:
        print("Sum\t = ", (int(sys.argv[1])) + (int(sys.argv[2])))
        print("Difference\t = ", (int(sys.argv[1])) - (int(sys.argv[2])))
        print("Product\t = ", (int(sys.argv[1])) * (int(sys.argv[2])))
        print("Quotient\t = ", (int(sys.argv[1])) / (int(sys.argv[2])))
        print("Remainder\t = ", (int(sys.argv[1])) % (int(sys.argv[2])))
    else:
        print("ERROR")
except:
    print("ERROR")
