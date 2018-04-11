from os.path import expanduser, abspath


def parse_plink_basename(basename):
    """
    Parse a string that points to a PLINK dataset.
    It might have a "~" that needs to be expanded or be a relative path.
    """
    return abspath(expanduser(basename))
