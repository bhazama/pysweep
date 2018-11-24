#!/usr/bin/env python
import subprocess
import time


def main():
    ip_target = "192.168.1."
    ip_list = []
    start = time.time()
    
    for x in range(0,256):
        current_ip = ip_target + "{}".format(x)
        action = "fping -a -C 5 -q "+ current_ip
        try:
          results = subprocess.check_output(action,stderr=subprocess.STDOUT,shell=True)
          split_results = results.split(":")
          reaction_time = split_results[1]
          print("Host: {}".format(current_ip) + " is detected online. Response time(s) were:" + reaction_time)
          ip_list.append(current_ip)
        except subprocess.CalledProcessError as e:
          error = e.output
        
    print("The following hosts were found to be online and responding to ping requests: \n\nDetected Hosts:\n==============")
    for ip in ip_list:
      print(ip)
    
    scan_time = format((time.time() - start) * 1000,".2f")
    print("\nTotal time to scan took: " + str(scan_time) + " ms")
        

if __name__ == '__main__':
    main()
