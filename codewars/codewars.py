def DNA_strand(dna):
    translation = str.maketrans('ATCG', 'TAGC')
    mod_dna = dna.translate(translation)
    print(mod_dna)

DNA_strand('AAAA')