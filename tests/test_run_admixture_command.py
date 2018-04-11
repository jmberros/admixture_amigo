from tempfile import gettempdir

import os
from os.path import dirname, join, isfile, getsize

from admixture_amigo import run_admixture_command


def test_run_admixture_command(root_dir, test_file):
    admixture_path = join(root_dir, 'admixture_linux-1.3.0/admixture')
    toy_dataset_basename = test_file('toy.bed')
    k_value = 1
    command = f'{admixture_path} {toy_dataset_basename} {k_value} -j1'
    out_dir = gettempdir()
    run_admixture_command(command, out_dir=out_dir)

    log_filepath = join(out_dir, 'toy.admixture.K1.log')
    p_filepath = join(out_dir, 'toy.1.P')
    q_filepath = join(out_dir, 'toy.1.Q')

    for filepath in [log_filepath, p_filepath, q_filepath]:
        assert isfile(filepath)

        if filepath == log_filepath:
            with open(filepath) as f:
                for line in f:
                    break
                assert 'ADMIXTURE Version 1.3.0' in line

        os.remove(filepath)
