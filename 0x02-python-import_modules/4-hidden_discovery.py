#!/usr/bin/python3
if __name__ == "__main__":
    import pickle

    with open("hidden_4.pyc", "rb") as file:
        code = pickle.load(file)

    names = [name for name in code.co_names if not name.startswith("__")]
    sorted_names = sorted(names)

    for name in sorted_names:
        print(name)
