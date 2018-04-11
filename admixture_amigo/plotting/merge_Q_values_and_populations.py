from admixture_amigo.plotting import (read_Q_file,
                                      read_fam,
                                      read_populations_file)


def merge_Q_values_and_populations(q_path, fam_path,
                                   populations_path=None, regions_path=None):
    """
    Given a +q_path+ to an admixture Q file, a +fam_path+ to its corresponding
    plink FAM file, and optionals +populations_path+ and +regions_path+ to
    the populations and regions that the samples in the FAM file belong to,
    this function merges all that data into a single pandas DataFrame.
    """
    q_values = read_Q_file(q_path)
    samples = list(read_fam(fam_path)['IID'])
    q_values['IID'] = samples

    if populations_path:
        populations = read_populations_file(populations_path)
        populations = populations.set_index('IID').loc[samples]['population']
        q_values['population'] = populations.values

    if regions_path:
        regions = read_populations_file(regions_path)
        regions = regions.set_index('IID').loc[samples]['population']
        q_values['region'] = regions.values

    return q_values.set_index('IID')

