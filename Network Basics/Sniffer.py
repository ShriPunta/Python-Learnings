import socket
import textwrap
import struct

#Need to unpack the ethernet frame
#The Struct converts the data to byte format
def ethe_frame(inc_data):
    #Writing a '!' in struct tells it that we are dealing with network info
    #Read Big Endian and Little Endian : How data is stored, where is MSB stored?
    #6S means 6 characters. see frame of ethernet for reference
    #H is small unsigned int
    dest_mac, src_mac, type_of = struct.unpack('! 6s 6s H', inc_data[:14])
    print(dest_mac," : ",src_mac)
    #Need to convert to a human readable form
    #Htons converts bytes and makes them compatible (big endian,small endian)
    return get_mac_addr(dest_mac), get_mac_addr(src_mac) , socket.htons(type_of), data[:14]

#Converts the address to a compatible form
def get_mac_addr(bytes_Add):
    #The map function takes an iterable and applies a function to each of them
    #IN this map, the function formats it 2 decimal places as the MAC address is
    # XX:XX:XX:XX:XX:XX
    bytes_str = map('{02x}'.format,bytes_Add)
    #the join function connects all the elements in iterable wid a string
    the_mac_addr = ':'.join(bytes_str).upper()
    return the_mac_addr




