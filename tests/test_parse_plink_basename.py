import re

from admixture_amigo import parse_plink_basename


def test_parse_plink_basename():
    result = parse_plink_basename('~/foo/bar/..')

    assert '~' not in result
    assert re.search(r'^/home/.+/foo$', result)
