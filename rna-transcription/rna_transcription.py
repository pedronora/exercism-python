def to_rna(dna_strand):
    dna_to_rna = {'G': 'C', 'C': 'G', 
                  'T': 'A', 'A': 'U'}

    return ''.join(dna_to_rna[d] for d in dna_strand)
