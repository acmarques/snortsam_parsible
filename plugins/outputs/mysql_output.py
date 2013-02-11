import MySQLdb as mysql
import sys

from plugins.common.logger import get_logger
from plugins.common.config import get_config

sensor = get_config()["hostname"]

mysql_host = get_config()["mysql"]["host"]
mysql_user = get_config()["mysql"]["username"]
mysql_pass = get_config()["mysql"]["password"]
mysql_database = get_config()["mysql"]["database"]


def output_insert_quarantine(sig_id, ip_src, ip_dest, port, duration, created_at):    
  sql = "insert into quarantines (sig_id, ip_src, ip_dst, sensor, port, duration, created_at) \
  values (%d, '%s', '%s', '%s', %d, %d, %d )" % \
  (sig_id, ip_src, ip_dest, sensor, port, duration, created_at)

  _execute_command(sql)  

def output_extend_quarantine(ip_src, ip_dest, port, duration, created_at):  
  sql = "update quarantines set duration=%d, created_at=%d where ip_src='%s' and ip_dst='%s' and sensor='%s' and port=%d" %  \
  (duration, created_at, ip_src, ip_dest, sensor, port)
  
  _execute_command(sql)

def output_remove_quarantine(ip_src, ip_dest, port):    
  sql = "delete from quarantines where ip_src='%s' and ip_dst='%s' and sensor='%s' and port=%d" % \
  (ip_src, ip_dest, sensor, port)
  
  _execute_command(sql)
  
  
def _execute_command(sql):
  db = mysql.connect(mysql_host, mysql_user, mysql_pass, mysql_database)
  cursor = db.cursor()
  try:
    cursor.execute(sql)
    db.commit()
  except Exception, ex:
    get_logger().exception("Unexpected error on command: '%s'" % (sql))
    db.rollback()   
  db.close()

  

