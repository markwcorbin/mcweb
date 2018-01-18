import os
import sys
import string
import re
import requests
import json

# A dynamic public IP is used for this website, therefore the assigned IP must be
# obtained each time the website is started.  Once obtained, the IP is added to
# the ASSIGNED_HOSTS variable in the mcweb/settings.py file.  Also, a notification
# email is sent with the new IP so that it can be used for requests to the website.

class McwebIP:
    public_IP = ""

    def get_public_IP(self):
        r = requests.get('https://api.ipify.org?format=json')
        print(r.text)
        r_native = json.loads(r.text)
        McwebIP.public_IP = r_native.get('ip')
        print(McwebIP.public_IP)
        self.set_public_IP_config()

    # Set the IP address in mcweb/settings.py
    def set_public_IP_config(self):
        settings_dir = 'mcweb'
        settings_filename = 'settings.py'
        settings_path = settings_dir + '/' + settings_filename
        temp_filename = 'temp.txt'
        temp_path = settings_dir + '/' + temp_filename

        allowed_hosts_label = "ALLOWED_HOSTS"
        allowed_hosts_line_re = r"ALLOWED_HOSTS.*"

        allowed_hosts_replacement = (allowed_hosts_label + " = " + 
                                    r"['" + McwebIP.public_IP + r"']")

        fin = open(settings_path, 'r') # in file
        fout = open(temp_path, 'w') # out file

        p = re.compile(allowed_hosts_line_re) # pattern

        for line in fin:
            # replace ALLOWED_HOSTS line
            newline = p.sub(allowed_hosts_replacement, line)
            print(newline)
            fout.write(newline)
        fin.close()
        fout.close()
        os.remove(settings_path)
        os.rename(temp_path, settings_path)





