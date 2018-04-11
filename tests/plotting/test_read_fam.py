from admixture_amigo.plotting import read_fam


def test_read_fam(test_file):
    fn = test_file('dataset.fam')
    result = read_fam(fn)
    assert list(result['FID']) == [1, 1, 1, 1, 1, 1, 1]
    assert sorted(result['IID']) == ['Sample-{}'.format(n)
                                     for n in range(1, 8)]
