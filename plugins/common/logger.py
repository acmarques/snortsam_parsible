import logging, yaml


config = yaml.load(open('config/snortsam_parsible.yml')) 
logging.basicConfig(level=logging.INFO)
h = logging.FileHandler(config["output_log_file"])
formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
h.setFormatter(formatter)
logger = logging.getLogger('snortsam_parsible')
logger.addHandler(h)   


def get_logger():  
  return logger