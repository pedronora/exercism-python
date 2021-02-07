def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b):
        raise ValueError("The strand length are different.")

    distance = 0
    for n, x in enumerate(strand_a):
        if x != strand_b[n]:
            distance += 1
    
    return distance
