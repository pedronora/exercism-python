def is_isogram(string):
    string = [l for l in string.lower() if l not in ' -']
    unique = set(string)
    if len(unique) == len(string):
        return True
    return False
