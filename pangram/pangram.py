def is_pangram(sentence):
    sentence = list(map(lambda x: x.lower() if x.isalpha() else '', sentence))
    
    unique_letters = ''
    for i in sentence:
        if i not in unique_letters and i != '':
            unique_letters += i

    result = ''.join(sorted(unique_letters))

    if result == 'abcdefghijklmnopqrstuvwxyz':
        return True
    return False
