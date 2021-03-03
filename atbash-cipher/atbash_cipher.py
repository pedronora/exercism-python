PLAIN = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
CIPHER = PLAIN[::-1]

def encode(plain_text):
    text = ''.join(filter(str.isalnum,plain_text)).lower()
    result = ''
    for n, c in enumerate(text):
        if n > 0 and n % 5 == 0:
            result += ' '
        
        if c.isdigit():
            result += c
        else:
            index = PLAIN.index(c)
            result += CIPHER[index]
    return result

def decode(ciphered_text):
    text = ciphered_text.replace(' ','').lower()
    result = ''
    for c in text:
        if c.isdigit():
            result += c
        else:
            index = CIPHER.index(c)
            result += PLAIN[index]
    return result
