import uuid
from cryptography.fernet import Fernet

class Crypto:
    def __init__(self, key):
        if key is None:
            self.key = Fernet.generate_key()
        else:
            self.key = key
        self.crypto = Fernet(self.key)

    def generate_text(self, item_id, owner_id):
        return bytes(item_id + '-' + owner_id + '-' + uuid.uuid4().hex)

    def encode(self, text, key):
        return self.crypto.encrypt(text)

    def decode(token):
        return self.crypto.decode(token)