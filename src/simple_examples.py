# a very basic function meant to
def is_ascii(c: str):
    """
    A very simple function that determines if a character is ASCII
    N.B. for demonstrative purposes, this function is intentionally written
    to crash if a string of length something other than 1 is passed in
    :param c: string
    :return: boolean. true if c is an ASCII character, false if c is not an ASCII character
    """
    return ord(c) < 128
