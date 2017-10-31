#Learn struct = it turns number/letters/strings and converts it to bytes format

from struct import *
import string

#2 integers and float
packed_data = pack('iif', 6,12,4.83)
print(packed_data)
# b'\x06\x00\x00\x00\x0c\x00\x00\x00\\\x8f\x9a@'
print(calcsize('iif'))

#To find which letters are acceptable as valid inputs
'''for i in range(0,26):
    try:
        print(' Letter : ',string.ascii_lowercase[i],' --> ',calcsize(string.ascii_lowercase[i]))
    except:
        print("Not this one : ",string.ascii_lowercase[i])'''

original_data = unpack('iif',packed_data)
print(original_data)
original_data = unpack('iif',b'\x06\x00\x00\x00\x0c\x00\x00\x00\\\x8f\x9a@')
print(original_data)


# -----------------------------------------------------------------------------------------
#              BITWISE OPERATORS
# -----------------------------------------------------------------------------------------

# -----------BITWISE-AND-----------------------------------------------------------
a = 50    #110010
b = 60    #111100
c = a & b #110000
print(c)

# -----------BITWISE-RIGHT SHIFT-----------------------------------------------------------
x=240      #11110000
y = x >> 2 #00111100

print(y)