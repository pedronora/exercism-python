def flatten(iterable):
    flat_list = []
    for i in iterable:
        if isinstance(i, list):
            flat_list.extend(flatten(i))
        elif i != None:
            flat_list.append(i)
    return flat_list
