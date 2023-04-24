"""
I've encrypted the flag with my secret key, you'll never be able to guess it. 

Remember the flag format and how it might help you in this challenge!


0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104
"""
from pwn import xor
flag = bytes.fromhex('0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104')
print(xor(flag, 'crypto{'.encode())) # oh, it says 'myXORke+y...'
print(xor(flag, 'myXORkey'.encode())) # try this? yay, it works! sometimes simpler is better


