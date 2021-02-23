def append(list1, list2):
    if not list1:
        return list2
    return list1 + list2


def concat(lists):
    new_list = []
    for item in lists:
        new_list += item
    return new_list


def filter(function, list):
    return [i for i in list if function(i)]


def length(list):
    return sum(1 for _ in list)


def map(function, list):
    return [function(i) for i in list]


def foldl(function, list, initial):
    result = initial
    for i in range(length(list)):
        result = function(result, list[i])
    return result


def foldr(function, list, initial):
    result = initial
    for i in range(length(list)-1, -1, -1):
        result = function(list[i], result)
    return result


def reverse(list):
    return [list[i] for i in range(length(list)-1, -1, -1)]
