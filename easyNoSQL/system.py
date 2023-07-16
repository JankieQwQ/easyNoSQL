
import json
import serror
import cryptos

VERSION = '0.1.0'
VERCHAR = 'Beta'
VERTEXT = VERSION + VERCHAR
salt    = 'salt' # You can use function: changeSalt.

t = """{}"""
flag = False

def openDatabase(filename,password='') -> bool:
    noPassword = False
    if password == '':
        noPassword = True
    with open(filename + '.json', 'r') as f:
        t = f.read()
    if not noPassword:
        t = cryptos.decode(password + salt,t)
    t = json.loads(t)
    flag = True
    return True

def checkFlag() -> bool:
    if t == """{}""" and flag == False:
        return False
    else:
        return True

def readValue(keyName) -> any:
    code = checkFlag()
    if code or t == None:
        raise serror.KVDataBaseError(401,"You do not have any databases open.")
    return t[keyName]

def writeValue(keyName,valueName) -> bool:
    code = checkFlag()
    if code or t == None:
        raise serror.KVDataBaseError(401,"You do not have any databases open.")
    t[keyName] = valueName
    if t[keyName] == valueName:
        return True
    else:
        raise serror.KVDataBaseError(402,"The data is not written.")
    
def changeSalt(newSalt) -> None:
    salt = newSalt

def saveDataBase(filename,password='') -> bool:
    noPassword = False
    if password == '':
        noPassword = True
    if noPassword:
        try:
            with open(filename + '.json', 'w') as f:
                f.write(json.dumps(t))
        except:
            raise serror.KVDataBaseError(403,"An error occurred manipulating the database file.")
        return True
    d = json.dumps(t)
    d = cryptos.encode(password + salt,d)
    try:
        with open(filename + '.json', 'w') as f:
            f.write(d)
    except:
        raise serror.KVDataBaseError(403,"An error occurred manipulating the database file.")
    
def version():
    print('easyNoSQL - KV Database, Version: ' + easyNoSQL.system.VERTEXT)
    