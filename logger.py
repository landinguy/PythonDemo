import logging.config

#
# log_path = './log/log-info.log'
#
#
# def get_logger(name=None):
#     logger = logging.getLogger(name)
#     logger.setLevel(logging.INFO)
#
#     formatter = logging.Formatter(
#         '%(asctime)s %(levelname)s [%(threadName)s] [%(name)s:%(filename)s:%(lineno)d] - %(message)s')
#
#     console = logging.StreamHandler()
#     console.setFormatter(formatter)
#
#     # file_logger = logging.FileHandler(filename=log_path, mode='a', encoding='utf8')
#     # file_logger.setFormatter(formatter)
#     logger.removeHandler()
#     logger.addHandler(console)
#     # logger.addHandler(file_logger)
#     return logger
#
# #
# # if __name__ == '__main__':
# #     log = get_logger("test")
# #     log.info("test python logging")
logging.config.fileConfig('log.conf')


def get(): return logging.getLogger('info')
