import pandas as pd


def read_fam(filepath):
    """
    Read a PLINK .fam file into a pandas DataFrame.
    """
    fam_fields = 'FID IID father mother sex phenotype'.split(' ')
    fam = pd.read_table(filepath, names=fam_fields, sep='\s+')
    fam['sex'] = fam['sex'].map({1: 'M', 2: 'F', 0: 'U'})
    return fam
