def rows(letter):
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    index = alphabet.index(letter)
    slice2 = alphabet[:index+1]
    slice1 = slice2[::-1]
    letters = slice1 + slice2[1:]    

    row = ''
    first_rows = []
    for l in slice2:
        for e in letters:
            if l == e:
                row+=l
            else:
                row+=' '
        first_rows.append(row)
        row = ''
    
    last_rows = first_rows[:-1][::-1]
    return first_rows + last_rows
