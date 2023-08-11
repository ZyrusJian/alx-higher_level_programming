#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    num_args = len(args)
    sum_args = 0

    if num_args != 0:
        for i in range(num_args):
            sum_args += int(args[i])
        print(sum_args)
    else:
        print("0")
