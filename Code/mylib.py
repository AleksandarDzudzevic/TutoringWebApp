import sqlite3
from passlib.context import CryptContext

pwd_config = CryptContext(schemes = ["pbkdf2_sha256"],
                          default = "pbkdf2_sha256",
                          pbkdf2_sha256__default_rounds = 30000
                          )

# this function receives unsafe password and returns the hashed password

def encrypt_password(user_passowrd):
    return pwd_config.encrypt(user_passowrd)


def check_password(hashed_password, user_password):
    return pwd_config.verify(user_password, hashed_password)


class database_worker:
    def __init__(self, name):
        self.connection = sqlite3.connect("tutorflix.db")
        self.cursor = self.connection.cursor()

    def search(self, query):
        result = self.cursor.execute(query).fetchall()
        return result

    def run_save(self, query):
        self.cursor.execute(query)
        self.connection.commit()

    def close(self):
        self.connection.close()
