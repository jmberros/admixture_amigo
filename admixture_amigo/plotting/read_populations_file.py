import pandas as pd


def read_populations_file(path):
    """
    Read a file at +path+ with two columns separated by whitespace:
    IID (individual ID) and population.
    """
    return pd.read_table(path, sep='\s+', header=None,
                         names=['IID', 'population'])
