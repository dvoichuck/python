import sys


def swap_str_and_case(argv):
    return ' '.join(argv[1:len(argv)]).swapcase()[::-1]


print(swap_str_and_case(sys.argv))
