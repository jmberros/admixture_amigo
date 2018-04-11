from os.path import join, dirname


def make_admixture_command(plink_basename, k_value, threads):
    """
    Build the command to run Admixture with the passed *plink_basename*,
    *k_value*, and *threads*. Returns a string.
    """
    admixture_path = join(dirname(dirname(__file__)),
                          'admixture_linux-1.3.0/admixture')

    if not plink_basename.endswith('.bed'):
        plink_basename += '.bed'

    return f'{admixture_path} {plink_basename} {k_value} -j{threads}'
