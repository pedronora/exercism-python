handshakes = {1000: 'jump',
              100: 'close your eyes',
              10: 'double blink',
              1: 'wink'}


def convert_to_binary(number):
    if number == 0:
        return 0
    
    binary = ''
    while number / 2 > 0:
        binary += str(number % 2)
        number = number // 2   
    return int(binary[::-1])


def commands(number):
    reversed = True
    n = convert_to_binary(number)
    if n >= 10000:
        n %= 10000
        reversed = False
    
    handshake = []
    for k in handshakes:
        if n >= k:
            handshake.append(handshakes[k])
        n %= k
    if reversed:
        return handshake[::-1]
    return handshake
