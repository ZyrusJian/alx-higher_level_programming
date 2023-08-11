#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    num_args = len(args)

    print("{0} argument{1}{2}".format(num_args, 's' if num_args != 1 else '',
                                      '.' if num_args == 0 else ':'))
    if num_args != 0:
        for i, arg in enumerate(args, start=1):
            print("{0}: {1}".format(i, arg))
