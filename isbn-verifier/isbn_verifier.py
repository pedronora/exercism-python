def is_valid(isbn):
    isbn = isbn.replace('-', '')
    if all(map(str.isdigit, isbn[:9])) and len(isbn) == 10:
        if isbn[9].isdigit() or isbn[9] == 'X':
            x = [int(x.replace('X', '10')) for x in isbn]
            if sum(x[0]*x[1] for x in list(zip(x, range(10, 0, -1)))) % 11 == 0:
                return True
    return False
