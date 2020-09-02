#!/usr/bin/python3
def uppercase(str):
    for i in str:
        h = ord(i)
        if ord(i) > ord('a') - 1 and ord(i) < ord('z') + 1:
            h = ord(i) - 32
        print("{}".format(chr(h)), end="")
    print()
