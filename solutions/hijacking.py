import base64
import os
import socket
ip = 'picoctf.org'
response = os.system("ping -n 1 18.164.217.61") # this is a way to ping server using python
#saving ping details to a variable
print(response);
host_info = socket.gethostbyaddr(ip) 
#getting IP from a domaine
print(host_info);
host_info_to_str = str(host_info[2])
host_info = base64.b64encode(host_info_to_str.encode('ascii'))
print("Hello, this is a part of information gathering",'Host: ', host_info)  