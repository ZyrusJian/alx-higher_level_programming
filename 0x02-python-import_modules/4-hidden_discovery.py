#!/usr/bin/python3
if __name__ == "__main__":
    import marshal

    with open("hidden_4.pyc") as file:
        code = marshal.load(file)

    names = [name for name in code.co_names if not name.startswith("__")]
    sorted_names = sorted(names)

    for name in sorted_names:
        print(name)
