import yaml

from plugins.common.logger import get_logger

try:
  config = yaml.load(open('config/snortsam_parsible.yml')) 
except Exception, ex:
  get_logger().exception("Config file error...")


def get_config():
  return config