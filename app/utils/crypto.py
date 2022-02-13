import hashlib
import hmac

class CryptoUtils:

    @staticmethod
    def get_hash_256(str):
        m = hashlib.sha256()
        m.update(str)
        return m.hexdigest()
    
    @staticmethod
    def get_hmac_512(str, key):
        h = hmac.new(key, msg=str, digestmod=hashlib.sha512)
        return h.hexdigest()