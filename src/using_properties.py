# this script contains various implementation of the Levenshtein string distance function
# as a way to illustrate the utility of property based testing

def levenshtein_stub(a: str, b: str):
    """
    intentionally stubbed implementation to illustrate test case failure
    :param a: string
    :param b: string
    :return: always returns a static value of zero
    """
    return 0

# or this one: there's an off by one error that's captured by the unit tests
def levenshtein_off_by_one(a: str, b: str):
    """
    intentionally mis-written implementation of Levenshtein function
    with an off-by-one error
    :param a: string
    :param b: string
    :return: no return value but shoud raise an IndexError
    """
    array_width = len(b) + 1
    array_height = len(a) + 1
    memoized_computations = [
        list(range(array_width))
    ] + [
        [n] + [None for _ in range(len(b))] for n in range(1, array_height)
    ]
    for m in range(1, array_width):
        for n in range(1, array_height):
            b_char = b[m-1]
            a_char = a[n-1]
            if a_char == b_char:
                new_val = memoized_computations[n-1][m-1]
            else:
                new_val = 1 + min(
                    memoized_computations[n-1][m],
                    memoized_computations[n][m-1],
                    memoized_computations[n-1][m-1]
                )
            memoized_computations[n][m] = new_val
    # off by one
    return memoized_computations[array_width][array_height]

def levenshtein(a: str, b: str):
    """
    Implementation of the Wagner-Fischer algorithm for Levenshtein distance.
    There are more efficient algorithms, but this is just for demonstrative purposes.
    For production code, find someone else's levenshtein library and then use it instead of rolling your own like this.
    :param a: string
    :param b: string
    :return: the computed Levenshtein string edit distance between a and b
    """
    array_width = len(b) + 1
    array_height = len(a) + 1
    memoized_computations = [
        list(range(array_width))
    ] + [
        [n] + [None for _ in range(len(b))] for n in range(1, array_height)
    ]
    for m in range(1, array_width):
        for n in range(1, array_height):
            b_char = b[m-1]
            a_char = a[n-1]
            if a_char == b_char:
                new_val = memoized_computations[n-1][m-1]
            else:
                new_val = 1 + min(
                    memoized_computations[n-1][m],
                    memoized_computations[n][m-1],
                    memoized_computations[n-1][m-1]
                )
            memoized_computations[n][m] = new_val
    return memoized_computations[len(a)][len(b)]
