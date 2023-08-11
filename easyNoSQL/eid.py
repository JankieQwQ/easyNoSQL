import random
import hashlib

def getID(text) -> int:
  obj = hashlib.md5()
  salt = random.randint(1000000,99999999)
  salt = str(salt)
  inp  = text + salt
  del text,salt
  inp  = inp.encode("utf-8")
  obj.update(inp)
  del inp
  res  = obj.hexdigest()
  return res
  
