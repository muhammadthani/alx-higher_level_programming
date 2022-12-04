#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == '':
        sentence[0] = None
    elif sentence != '':
        initial_char = sentence[0]
    return (len(sentence), initial_char)
