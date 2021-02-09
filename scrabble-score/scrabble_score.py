values = {1: 'AEIOULNRST', 
          2: 'DG',
          3: 'BCMP', 
          4: 'FHVWY',
          5: 'K',
          8: 'JX',
          10: 'QZ'}


def score(word):
    score = 0
    for char in word.upper():
        for k in values:
            if char in values[k]:
                score += k
    return score
