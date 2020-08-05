
class Login:
    def __init__(self, uuid: str, username: str, password: str, salt: str, md5: str, sha1: str, sha256: str):
        self.uuid = uuid
        self.username = username
        self.password = password
        self.salt = salt
        self.md5 = md5
        self.sha1 = sha1
        self.sha256 = sha256
