"""Admixture Amigo.

Usage:
  admixture_amigo.py (-i BASENAME) (-k KVALUES) [-o OUTDIR] [--threads N]

Options:
  -i BASENAME, --plink BASENAME    Basename of the {.bed, .bim, .fam} files.
  -k KVALUES, --k-values KVALUES   Comma-separated K values to run Admixture
                                   with. E.g.: "3,4,5,7"
  -o OUTDIR, --out-dir OUTDIR      Directory to put the output. [default: .]
  -t N --threads N                 Number of threads to use. [default: 1]

"""

import logging
import sys

from docopt import docopt

from admixture_amigo import (
    parse_k_values,
    parse_plink_basename,
    parse_out_dir_and_create_it,
    make_admixture_command,
    run_admixture_command,
)

logging.basicConfig(
    stream=sys.stdout,
    level=logging.DEBUG,
    format='[%(asctime)s] %(message)s',
    datefmt="%Y-%m-%d %H:%M:%S"
)
logger = logging.getLogger()

def main():
    arguments = docopt(__doc__, version='Admixture Amigo 0.1')
    k_values = parse_k_values(arguments['--k-values'])
    plink_basename = parse_plink_basename(arguments['--plink'])
    out_dir = parse_out_dir_and_create_it(arguments['--out-dir'])
    threads = (int(arguments['--threads']))

    logger.info('Received the following arguments:')
    logger.info('K Values = {}'.format(k_values))
    logger.info('Plink dataset basename = {}'.format(plink_basename))
    logger.info('Output Dir = {}'.format(out_dir))

    for k in k_values:
        command = make_admixture_command(plink_basename, k, threads=threads)
        run_admixture_command(command, out_dir)

    logger.info('Done! Check results in: {}'.format(out_dir))

if __name__ == '__main__':
    main()