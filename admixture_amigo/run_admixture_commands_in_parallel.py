import logging
from concurrent.futures import ProcessPoolExecutor, as_completed

from admixture_amigo import run_admixture_command


logger = logging.getLogger()


def run_admixture_commands_in_parallel(commands, out_dir, max_workers):
    """
    Run a list of admixture *commands* in parallel processes.
    """
    with ProcessPoolExecutor(max_workers=max_workers) as pool:
        futures_to_commands = {}

        for command in commands:
            future = pool.submit(run_admixture_command, command, out_dir)
            futures_to_commands[future] = command

        for future in as_completed(futures_to_commands):
            command = futures_to_commands[future]
            # future.result() # FIXME: Is this necessary?
            logger.info('Finished this command = "{}"'
                        .format(command))
