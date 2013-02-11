import logging

logging.basicConfig(level=logging.INFO)
h = logging.FileHandler('log/snortsam_parsible.log')
formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
h.setFormatter(formatter)
logger = logging.getLogger('snortsam_parsible')
logger.addHandler(h)   


def get_logger():  
  return logger