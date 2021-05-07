def distance(strand_a, strand_b):
    if len(strand_a) != len(strand_b): raise ValueError('Strands have different size')
    return len([i for i in range(len(strand_a)) if strand_a[i] != strand_b[i]])
