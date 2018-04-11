import re

from admixture_amigo import make_admixture_command


def test_make_admixture_command():
    result = make_admixture_command('/foo/bar', 4, 5)
    pattern = (r'/home/(.+?/)+admixture_amigo/admixture_linux-1.3.0/admixture '
               r'/foo/bar.bed 4 -j5')
    assert re.search(pattern, result)
