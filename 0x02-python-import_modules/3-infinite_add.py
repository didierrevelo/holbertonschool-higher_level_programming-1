#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    a = 0
    argv = len(sys.argv)
    args = sys.argv
    for b in range(1, argv):
        a = a + int(args[b])
    print(a)
