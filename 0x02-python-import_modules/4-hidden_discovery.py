#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    for a in dir(hidden_4):
        if "__" not in a:
            print(a)
