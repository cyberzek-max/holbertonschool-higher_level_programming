#!/usr/bin/python3
def multiple_returns(sentence):
    """Return the length of a string and its first character.
    If the string is empty, the first character is None.
    """
    first_char = sentence[0] if sentence else None
    return (len(sentence), first_char)
