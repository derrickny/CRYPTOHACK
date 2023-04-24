
"""
#instructions
ASCII is a 7-bit encoding standard which allows the representation of text using the integers 0-127.

Using the below integer array, convert the numbers to their corresponding ASCII characters to obtain a flag.
NOTE
the chr() function can be used to convert an ASCII ordinal number to a character 
(the ord() function does the opposite).
"""

#Convert each integer to character to get the flag
ascii = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

#flag to hold the asii ordinal number
flag = ''

#for loop to traverse the array as it does the conversion 
for a in ascii:
    flag += chr(a)

print(flag)