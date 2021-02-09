def count_words(sentence):
    phrase = map(lambda c: c.lower() if c.isalpha() or c.isdigit() or (c == '\'') else ' ', sentence)

    phrase = ''.join(phrase)
   
    counts = {}
    for word in phrase.split():
        w = word.strip('\'')
        if w not in counts.keys():
            counts[w] = 1
        else:
            counts[w] += 1
    return counts
