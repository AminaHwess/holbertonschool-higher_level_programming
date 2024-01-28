#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    for idx in range(1, len(sys.argv)):
        sum += int(str(sys.argv[idx]))
    print("{}".format(sum))
