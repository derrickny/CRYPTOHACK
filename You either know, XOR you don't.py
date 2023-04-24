"""
I've encrypted the flag with my secret key, you'll never be able to guess it. 

Remember the flag format and how it might help you in this challenge!


0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104
"""
from binascii import unhexlify

def brute(ciphertext, key):
    if len(ciphertext) != len(key):
        return "Failed!"
    return bytes([a ^ b for a, b in zip(ciphertext, key)]).decode(errors="replace")

ciphertext = unhexlify("0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104")
print("[-] CIPHER: {}".format(ciphertext))

# First Step
partial_key = brute(ciphertext[:7], b"crypto{")
print("[-] PARTIAL KEY FOUND: {}".format(partial_key))

# Second Step
key = (partial_key + "y").encode() * (len(ciphertext) // len(key)) + (partial_key + "y").encode()[:len(ciphertext) % len(key)]
print("[-] Decoding using KEY: {}".format(key.decode()))

# Final Step
flag = brute(ciphertext, key)
print("\n[*] FLAG: {}".format(flag))



