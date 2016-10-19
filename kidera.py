import pandas

kidera_factors = pandas.read_csv('kidera.csv', header=None, index_col=0)
symbol_lookup = { 'ALA': 'A', 'ARG': 'R',
                  'ASN': 'N', 'ASP': 'D',
                  'CYS': 'C', 'GLN': 'Q',
                  'GLU': 'E', 'GLY': 'G',
                  'HIS': 'H', 'ILE': 'I',
                  'LEU': 'L', 'LYS': 'K',
                  'MET': 'M', 'PHE': 'F',
                  'PRO': 'P', 'SER': 'S',
                  'THR': 'T', 'TRP': 'W',
                  'TYR': 'Y', 'VAL': 'V' }

kidera_factors.index = kidera_factors.index \
                                     .map(lambda x: symbol_lookup[x])

def positional_score(sequence):
    return kidera_factors.loc[list(sequence)]

def aggregate_score(sequence):
    return kidera_factors.loc[list(sequence)].sum() / 10