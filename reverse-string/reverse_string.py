def reverse(text):
    text_list = list(text)
    size = len(text_list)
    for c in range(size//2):
        text_list[c], text_list[size-1 - c] = text_list[size-1 -c], text_list[c]
    return ''.join(text_list)
