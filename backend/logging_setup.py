import logging

def setup_logger(name,log_file='server.log',level=logging.DEBUG):
    log=logging.getLogger(name)
    log.setLevel(level)
    file_handler=logging.FileHandler(log_file)
    formatter = logging.Formatter('%(asctime)s - %(name)s -%(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    if not log.handlers:
        log.addHandler(file_handler)
    return log
