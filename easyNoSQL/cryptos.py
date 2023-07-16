from Crypto.Cipher import AES

def encode(password,text) -> str:
    pass1 = password
    filet = text
    del password,text
    aes = AES.new(pass1,AES.MODE_ECB)
    encodeText = aes.encrypt(filt)
    return str(encodeText)

def decode(password,text) -> str:
    pass1 = password
    filet = text
    del password,text
    aes = AES.new(pass1,AES.MODE_ECB)
    encodeText = aes.decrypt(filt)
    return str(encodeText)