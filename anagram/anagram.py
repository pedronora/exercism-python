def count_char(word):
    counting = {}
    for char in word.lower():
        if char in counting.keys():
            counting[char] += 1
        else:
            counting[char] = 1
    return {k.capitalize(): counting[k] for k in sorted(counting.keys())}

def find_anagrams(word, candidates):
    not_equal = [x for x in candidates if x.lower() != word.lower()]
    return [candidate for candidate in not_equal if count_char(word) == count_char(candidate)]
