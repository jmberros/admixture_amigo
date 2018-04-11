import os
from tempfile import gettempdir

from admixture_amigo import parse_out_dir_and_create_it


def test_parse_out_dir():
    out_dir = os.path.join(gettempdir(), 'foo/bar/baz/..')
    result = parse_out_dir_and_create_it(out_dir)
    assert result == '/tmp/foo/bar'
    assert os.path.isdir('/tmp/foo/bar')

    # Shouldn't break if the directory already exists:
    parse_out_dir_and_create_it(out_dir)
