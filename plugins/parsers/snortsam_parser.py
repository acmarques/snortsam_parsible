import re
from plugins.common.logger import get_logger

def parse_event(line):  
  try:
    regex_block_in_out = re.compile("(?P<date>\S*),\s(?P<time>\S*),\s\S*,\s\S*,\ssnortsam,\sBlocking\shost\s(?P<host>\S*)\s(?P<mode>\S*)\sfor\s(?P<duration>\S*)\sseconds\s\(Sig_ID\:\s(?P<sig_id>\S*)\)")
    r = regex_block_in_out.search(line)
    if r:
      return _build_result_set(r, "block", "in_out")
  
    regex_block_connection = re.compile("(?P<date>\S*),\s(?P<time>\S*),\s\S*,\s\S*,\ssnortsam,\sBlocking\shost\s\S*\sin\s(?P<mode>\S*)\s(?P<host_src>\S*)->(?P<host_dest>\S*)\:(?P<port>\S*)\s\S*\sfor\s(?P<duration>\S*)\sseconds\s\(Sig_ID\:\s(?P<sig_id>\S*)\)")
    r = regex_block_connection.search(line)
    if r:
      return _build_result_set(r, "block", "connection")

    regex_extending_in_out = re.compile("(?P<date>\S*),\s(?P<time>\S*),\s\S*,\s\S*,\ssnortsam,\sExtending\sblock\sfor\shost\s(?P<host>\S*)\s(?P<mode>\S*)\sfor\s(?P<duration>\S*)\sseconds\s\(Sig_ID\:\s(?P<sig_id>\S*)\)")
    r = regex_extending_in_out.search(line)
    if r:
      return _build_result_set(r, "extending", "in_out")    
  
    regex_extending_connection = re.compile("(?P<date>\S*),\s(?P<time>\S*),\s\S*,\s\S*,\ssnortsam,\sExtending\sblock\sfor\shost\s\S*\sin\s(?P<mode>\S*)\s(?P<host_src>\S*)->(?P<host_dest>\S*)\:(?P<port>\S*)\s\S*\sfor\s(?P<duration>\S*)\sseconds\s\(Sig_ID\:\s(?P<sig_id>\S*)\)")
    r = regex_extending_connection.search(line)
    if r:
      return _build_result_set(r, "extending", "connection")    
         
    regex_unblock_in_out = re.compile("(?P<date>\S*),\s(?P<time>\S*),\s\S*,\s\S*,\ssnortsam,\sRemoving\s\S*\ssec\s(?P<mode>\S*)\sblock.*\sfor\shost\s(?P<host>\S*).")
    r = regex_unblock_in_out.search(line)
    if r:
      return _build_result_set(r, "unblock", "in_out")      
  
    regex_unblock_connection = re.compile("(?P<date>\S*),\s(?P<time>\S*),\s\S*,\s\S*,\ssnortsam,\sRemoving.*for\shost\s\S*\sin\s(?P<mode>\S*)\s(?P<host_src>\S*)->(?P<host_dest>\S*):(?P<port>\S*)\s\S*")
    r = regex_unblock_connection.search(line)
    if r:
      return _build_result_set(r, "unblock", "connection")         
                 
    return {}
  except Exception, ex:
    get_logger().exception("Unexpected error:")


def _build_result_set(r, event_action, event_type):
    result_set = {}
    items = r.groupdict()
    
    result_set["time"] = items["time"]
    result_set["date"] = items["date"]  
    result_set["mode"] = items["mode"]  
    result_set["action"] = event_action
    if event_type == "in_out":
      result_set["host"] = items["host"]
    elif event_type == "connection":
      result_set["host_src"] = items["host_src"]
      result_set["host_dest"] = items["host_dest"]
      result_set["port"] = items["port"]    
    if event_action == "block" or event_action == "extending":
      result_set["sig_id"] = items["sig_id"]
      result_set["duration"] = items["duration"]
            
    get_logger().info(result_set)     
    return(result_set)


