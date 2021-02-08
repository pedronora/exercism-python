def transform(legacy_data):
    output = {}
    for k in legacy_data:
        for i in legacy_data[k]:
            output[i.lower()] = k
    return output
