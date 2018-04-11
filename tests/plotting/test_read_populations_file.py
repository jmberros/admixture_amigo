from admixture_amigo.plotting import read_populations_file


def test_read_populations_file(test_file):
    path = test_file('dataset.populations')
    result = read_populations_file(path)
    assert list(result['IID']) == ['Sample-1', 'Sample-2', 'Sample-3',
                                   'Sample-4', 'Sample-5', 'Sample-6',
                                   'Sample-7']
    assert list(result['population']) == ['POP1', 'POP2', 'POP1', 'POP2',
                                          'POP2', 'POP3', 'POP3']
