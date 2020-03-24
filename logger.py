import logging

log_path = './log/log-info.log'


def get_logger():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s %(levelname)s [%(threadName)s] [%(filename)s:%(lineno)d] - %(message)s')

    console = logging.StreamHandler()
    console.setFormatter(formatter)

    file_logger = logging.FileHandler(filename=log_path, mode='a', encoding='utf8')
    file_logger.setFormatter(formatter)

    logger.addHandler(console)
    logger.addHandler(file_logger)
    return logger


if __name__ == '__main__':
    log = get_logger()
    log.info("测试~~~")
