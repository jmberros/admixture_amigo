from admixture_amigo.plotting import read_Q_file


def test_read_Q_file(test_file):
    fam_path = test_file('dataset.3.Q')
    result = read_Q_file(fam_path)
    assert result.shape == (7, 3)
    assert list(result.columns) == ['k3_cluster_1',
                                    'k3_cluster_2',
                                    'k3_cluster_3']
    assert result.loc[3, 'k3_cluster_2'] == 1.0
