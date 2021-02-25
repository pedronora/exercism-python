def rotate(text, key):
    alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 
             'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
             's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    cript = ''
    for l in text:
        if l.lower() in alpha:
            index = (alpha.index(l.lower()) + key) % 26
            if l.isupper():
                cript += alpha[index].upper()
            else:
                cript += alpha[index]
        else:
            cript += l
    return cript
