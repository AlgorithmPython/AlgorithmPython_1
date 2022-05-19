from pydoc import doc


def shellsort(a, n):
    h = 1
    while h<n:
        h = h * 3 + 1