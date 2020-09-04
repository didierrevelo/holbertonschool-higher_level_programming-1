#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = len(sys.argv) - 1
    args = sys.argv
    string = "arguments"
    point = "."
    if argv == 1:
        string = "argument"
    if argv != 0:
        point = ":"
    print("{} {}{}".format(argv, string, point))

    for iterar, arg in enumerate(args):
        if iterar > 0:
            print("{}: {}".format(iterar, arg))
