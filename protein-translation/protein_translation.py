def proteins(strand):
    aminoacids = {'Methionine': ['AUG'], 'Phenylalanine': ['UUU', 'UUC'], 'Leucine': ['UUA', 'UUG'], 'Serine': ['UCU', 'UCC', 'UCA', 'UCG'], 'Tyrosine': ['UAU', 'UAC'], 'Cysteine': ['UGU', 'UGC'], 'Tryptophan': ['UGG']}

    translations = []
    for i in range(3, len(strand) + 1, 3):
        codon = strand[i-3: i]
        if codon in ['UAA', 'UAG', 'UGA']:
            break
        for k in aminoacids:
            if codon in aminoacids[k]:
                translations.append(k)

    return translations
