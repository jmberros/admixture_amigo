from admixture_amigo.plotting import merge_Q_values_and_populations


def test_merge_Q_values_and_populations(test_file):
    result = merge_Q_values_and_populations(
        q_path=test_file('dataset.3.Q'),
        fam_path=test_file('dataset.fam'),
        populations_path=test_file('dataset.populations'),
        regions_path=test_file('dataset.regions'),
    )

    assert result.loc['Sample-6', 'population'] == 'POP3'
    assert result.loc['Sample-6', 'region'] == 'REG3'
    assert result.loc['Sample-6', 'k3_cluster_3'] == 0.4
