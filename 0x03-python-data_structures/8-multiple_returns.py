#!/usr/bin/python3
def multiple_returns(sentence):
    # If sentence is empty the first char is None
    if len(sentence) == 0:
        return (len(sentence), None)
    # If sentence isn't empty return length and first char
    if len(sentence) > 0:
        return (len(sentence), sentence[:1])
