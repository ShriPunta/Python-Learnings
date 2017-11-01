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

    #Need to convert to a human readable form
    return get_mac_addr(dest_mac),
