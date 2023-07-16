from Crypto.Cipher import AES
import easyNoSQL.system
import easyNoSQL.serror
import easyNoSQL.cryptos
import json

__all__ = ['pycryptodome','json']


openDatabase = easyNoSQL.system.openDatabase
readValue    = easyNoSQL.system.readValue
writeValue   = easyNoSQL.system.writeValue
version      = easyNoSQL.system.version

if __name__ == "__main__":
    version()
