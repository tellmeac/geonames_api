import logging


# setups global logging configuration.
def setup_global_logger():
    logging.basicConfig(filename="messages.log",
                        level=logging.DEBUG,
                        format='%(asctime)s: '
                               '%(filename)s: '
                               '%(levelname)s: '
                               '%(funcName)s(): '
                               '%(lineno)d:\t'
                               '%(message)s')
