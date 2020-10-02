#!/usr/bin/python3
"""text_identation
"""


def text_indentation(text):
    """identation

    Args:
        text (string): text must be a string

    Raises:
        TypeError: text must be a string,
                    otherwise raise a TypeError
                    exception with the message
                    text must be a string
    """
    run = 0
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    for i, c in enumerate(text):
        if c in '.?:':
            print(text[run: i + 1].strip() + '\n')
            run = i + 1
    if run < len(text):
        print(text[run:].strip(), end="")
