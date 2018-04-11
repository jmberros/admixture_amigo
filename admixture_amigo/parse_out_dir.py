from os import makedirs
from os.path import expanduser, abspath


def parse_out_dir_and_create_it(out_dir):
    """
    Parse *out_dir* to remove any relative and user bits in the path and
    create it in case it doesn't exist.
    """
    parsed_out_dir = abspath(expanduser(out_dir))
    makedirs(out_dir, exist_ok=True)
    return parsed_out_dir
