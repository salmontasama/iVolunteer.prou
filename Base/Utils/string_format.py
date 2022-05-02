from unicodedata import normalize

def string_normalize(string):
    return normalize('NFKD',string)
