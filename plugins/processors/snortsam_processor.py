import time, datetime, logging
from plugins.outputs.mysql_output import output_insert_quarantine, output_extend_quarantine, output_remove_quarantine
from plugins.common.logger import get_logger

def process_quarantine(data):
  try:
    if not any(data): return
    
    created_at = time.mktime(datetime.datetime.strptime(data["date"] + "-" + data["time"], "%Y/%m/%d-%H:%M:%S").timetuple())
    
    if data["mode"] == "inbound":
      ip_src = data["host"]
      ip_dest = "0.0.0.0"
    elif data["mode"] == "outbound": 
      ip_src = "0.0.0.0"
      ip_dest = data["host"]
    elif data["mode"] == "connection":
      ip_src = data["host_src"]
      ip_dest = data["host_dest"]  
    
    if "sig_id" in data.keys(): 
      sig_id = int(data["sig_id"])    
    
    if "duration" in data.keys(): 
      duration = int(data["duration"])  
           
    port = 0  
    if "port" in data.keys(): 
      port = int(data["port"])
  
    if data["action"] == "block":
      output_insert_quarantine(sig_id, ip_src, ip_dest, port, duration, created_at)
    elif data["action"] == "extending":
      output_extend_quarantine(ip_src, ip_dest, port, duration, created_at)      
    else:
      output_remove_quarantine(ip_src, ip_dest, port)      
  except Exception, ex:
    get_logger().exception("Unexpected error:")
  
