import os
import shutil
from tempfile import gettempdir

from admixture_amigo import parse_out_dir_and_create_it


def test_parse_out_dir_and_create_it():
    out_dir = os.path.join(gettempdir(), 'foo-1234/bar/baz/..')
    result = parse_out_dir_and_create_it(out_dir)
    expected_parsed_dir = '/tmp/foo-1234/bar'
    assert result == expected_parsed_dir
    assert os.path.isdir(expected_parsed_dir)

    # Shouldn't break if the directory already exists:
    parse_out_dir_and_create_it(out_dir)

    # Cleanup
    shutil.rmtree(expected_parsed_dir)
    assert not os.path.isdir(expected_parsed_dir)
