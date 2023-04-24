"""
In the last challenge, you saw how XOR worked at the level of bits. 
In this one, we're going to cover the properties of the XOR operation,
and then use them to undo a chain of operations that have encrypted a flag.
Gaining an intuition for how this works will help greatly when you come to attacking real cryptosystems later, 
especially in the block ciphers category.

There are four main properties we should consider when we solve challenges using the XOR operator

Commutative: A ⊕ B = B ⊕ A 
Associative: A ⊕ (B ⊕ C) = (A ⊕ B) ⊕ C
Identity: A ⊕ 0 = A
Self-Inverse: A ⊕ A = 0

Let's break this down. Commutative means that the order of the XOR operations is not important. 
Associative means that a chain of operations can be carried out without order (we do not need to worry about brackets). 
The identity is 0, so XOR with 0 "does nothing", and lastly something XOR'd with itself returns zero.

Let's put this into practice! Below is a series of outputs where three random keys have been XOR'd together and with the flag. Use the above properties to undo the encryption in the final line to obtain the flag.

KEY1 = a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
KEY2 ^ KEY1 = 37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e
KEY2 ^ KEY3 = c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
FLAG ^ KEY1 ^ KEY3 ^ KEY2 = 04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf

 Before you XOR these objects, be sure to decode from hex to bytes.
 NOTE
 AS per the above we get to see that the porperties that soughts the above keys is the cummutative ones 
 Let's apply it to get KEY2 from KEY1 and then do the same for the remaining KEYs. 
 Finally we get the flag in hex format, decoding it we get the flag
"""

def xor_to_str(k1,k2):
    if len(k1) != len(k2):
        raise "XOR EXCEPTION:Strings are not of equal length!"
    return ''.join(format(int(A,16)^ int(B,16),'x') # here we use the Commutative property 
                   for A,B in zip(k1,k2)) # this does the combination of the keys 

KEY1 = "a6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313"

KEY2 = xor_to_str("37dcb292030faa90d07eec17e3b1c6d8daf94c35d4c9191a5e1e",KEY1)
print("KEY2: {}".format(KEY2))

KEY3 = xor_to_str("c1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1",KEY2)
print("KEY3: {}".format(KEY3))

KEY4 = xor_to_str(xor_to_str(KEY1,KEY2),KEY3)
print("KEY4: {}\n".format(KEY4))

FLAG = xor_to_str("04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf",KEY4)
print("FLAG: {}".format(bytes.fromhex(FLAG)))