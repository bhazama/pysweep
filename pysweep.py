#!/usr/bin/env python
import subprocess



def main():
    #print("I am main!!")
    ip_target = "192.168.200."
    ip_list = []
    
    for x in range(105,107):
        current_ip = ip_target + "{}".format(x)
        action = "fping -a -C 5 -q "+ current_ip
        try:
          results = subprocess.check_output(action,stderr=subprocess.STDOUT,shell=True)
          split_results = results.split(":")
          reaction_time = split_results[1]
          print("Host: {}".format(current_ip) + " is detected online. Response time(s) were: " + reaction_time)
        except subprocess.CalledProcessError as e:
          error = e.output
       
       
if __name__ == '__main__':
    main()
        
#print("Detected Hosts:\n ============= ")
        


