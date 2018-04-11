from os.path import expanduser, abspath, join, basename
import os
from subprocess import run, PIPE
import logging


logger = logging.getLogger()


def run_admixture_command(command, out_dir):
    """
    Run an admixture *command*. Deal with directory creation and logging.
    Put the resulting P and Q files and the logs in the *out_dir*.
    """

    # Admixture puts its output in the directory where its run.
    # So we need to change to that directory.

    original_dir = os.getcwd()
    try:
        os.chdir(abspath(expanduser(out_dir)))
        args = _, plink_bed, k, _ = command.split(' ')
        plink_basename_without_path = basename(plink_bed.replace('.bed', ''))
        # Admixture writes its logging to STDOUT and nothing to STDERR
        logger.info('Running this command = "{}"'.format(command))
        completed_process = run(args, stdout=PIPE, check=True)
        log_filename = ('{}.admixture.K{}.log'
                        .format(plink_basename_without_path, k))
        log_filepath = join(out_dir, log_filename)
        with open(log_filepath, 'wb') as f:
            f.write(completed_process.stdout)
    finally:
        os.chdir(original_dir)

