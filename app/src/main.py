import os
import sys
import hashlib
# import torch
# import pytorch_lightning
# import models
from sqlite3 import connect, Error
import logging

"""
TODO: login own module, encrypt username?, refactor
      logger make into config/own module
"""


def create_connection(func):
    """sqlite3 database wrapper"""
    def _db_connect(user_db='src/data/users/users.db', *args, **kwargs):
        result = None
        try:
            with connect(user_db) as connection:
                curs = connection.cursor()
                result = func(curs, *args, **kwargs)
                connection.commit()
        except Error as e:
            logger.warning("Failed to read data from sqlite table from %s \n %s", user_db, e)
        return result

    return _db_connect


@create_connection
def init_users(curs):
    """Create table if it doesnt exist."""
    curs.execute("""
        CREATE TABLE IF NOT EXISTS People(
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL)
            """)
    return "Users database initiated..."


def encrypt_pw(password: str, salt=None) -> bytes:
    """
    Encrypt password.
    Using: 32 byte salt and 100_000 SHA-256 iterations
    dklen = 128  # 128 byte key.
    # full key length 32 + 128 = 160
    """
    if not salt:
        salt = os.urandom(32)
    privkey = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100_000, dklen=128)
    full_key = salt + privkey
    return full_key


def check_pw(login_info):
    """ Compare database password to user input """
    salt, real_pw = login_info[2][:32], login_info[2][32:]
    counter = 0
    while counter < 3:
        password = input("Enter password: ")
        if not password:
            break
        encrypted_password = encrypt_pw(password, salt)[32:]
        if encrypted_password == real_pw:
            logger.info("Authentication successful.")
            return True
        else:
            counter += 1
            logger.info("Wrong password entered... %s times", counter)
    return False


def get_username():
    """ Get username """
    counter = 0
    user_name = ""
    while counter < 3:
        user_name = input("Enter username: ")
        if len(user_name) < 3:
            logger.info("Incorrect username %s", user_name)
            logger.info("Username must be at least 3 characters")
        else:
            break
        counter += 1
    if len(user_name) < 3:
        return 'npc'
    return user_name


@create_connection
def login(curs):
    """
    Check if user exists.
    Return username and True if yes.
    """
    user_name = get_username()
    login_info = curs.execute(f"SELECT * FROM People WHERE username = ?", (user_name,)).fetchone()
    login_success = False

    if login_info:
        login_success = check_pw(login_info)
    else:
        logger.info("Account not found for %s", user_name)
        logger.info("Creating account a new account.")
        new_password = input("Enter password for new account or press enter to quit: ")
        if new_password:
            encrypted_pw = encrypt_pw(new_password)
            params = (user_name, encrypted_pw)
            curs.execute("INSERT INTO People VALUES (NULL, ?, ?)", params)
            login_success = True
    return user_name, login_success


def main():
    """ 
    0. Activate PySide GUI
    1. Login user
    2. Load sys stats
    """
    # torch.cuda.is_available()
    logger.info(init_users())
    user, connection_made = login()
    if connection_made:
        logger.info("Welcome back %s!", user)
    else:
        logger.info("Failed authentication %s!\nExiting...", user)
        sys.exit()


if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    stream_logs = logging.StreamHandler(sys.stdout)
    file_logs = logging.FileHandler('src/logs/main_errors.log')
    formatter = logging.Formatter('%(asctime)s - %(message)s')
    for logtype in [stream_logs, file_logs]:
        logtype.setFormatter(formatter)
        logger.addHandler(logtype)
    logger.setLevel(logging.INFO)
    sys.exit(main())
