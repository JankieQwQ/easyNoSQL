class KVDataBaseError(Exception):
    def __init__(self, code, message):
        self.code = code
        self.message = message
    
    def __str__(self):
        return f"KVDataBaseError, Code: {self.code}, Message: {self.message}"
    