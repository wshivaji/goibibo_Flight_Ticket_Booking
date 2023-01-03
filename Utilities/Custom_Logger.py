import logging
from stat import filemode


class log_gen:

    @staticmethod
    def log():
        logging.basicConfig(filename="Logs\\automation.log", format="%(asctime)s - %(levelname)s - %(message)s")
        logger = logging.getLogger()
        logger.info("Test message")
        # Setting the threshold of logger to DEBUG
        logger.setLevel(logging.DEBUG)
        return logger


