# Using loop
def find(search_list, value):
    length = len(search_list)

    start = 0
    end = length - 1

    while start <= end:
        middle = (start + end) // 2
        if search_list[middle] == value:
            return middle
        elif search_list[middle] > value:
            end = middle - 1
        else:
            start = middle + 1

    else:
        raise ValueError("Value not found!")

# Using recursion
def find(search_list, value, start=0, end=None):
    if end is None:
        end = len(search_list) - 1
    
    if start <= end:
        middle = (start + end) // 2

        if search_list[middle] == value:
            return middle
        elif search_list[middle] > value:
            return find(search_list, value, start, middle - 1)
        else:
            return find(search_list, value, middle + 1, end)

    raise ValueError('Value not found!')
