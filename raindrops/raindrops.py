def convert(number):
    string_converted = ''
    if number % 3 == 0:
        string_converted += 'Pling'
    if number % 5 == 0:
        string_converted += 'Plang'
    if number % 7 == 0:
        string_converted += 'Plong'
    if string_converted == '':
        return str(number)
    return string_converted
