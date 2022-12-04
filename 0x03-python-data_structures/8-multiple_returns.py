#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence != '':
        initial_char = sentence[0]
    else:
        initial_char = None
    return (len(sentence), initial_char)
