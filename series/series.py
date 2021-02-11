def slices(series, length):
    if (length > len(series)) or (length <= 0):
        raise ValueError('length must be less than series length and bigger than 0')
    
    list_series = []
    n = 0
    while (n+length) <= len(series):
        list_series.append(series[n:n+length])
        n+=1
    return list_series
