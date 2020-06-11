import hashlib


def encrypt(s):
    binary_string = s.encode("ascii") 
    m = hashlib.sha256() 
    m.update(binary_string)
    return m.hexdigest()

    