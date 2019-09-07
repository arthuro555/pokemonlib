import base64
import os

from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet

from pokemonlib.misc import Settings


def getkey(password_provided):
    """
    You don't need this, It's automatically called by the encryption functions. It creates the encryption key from the
    salt and password in misc.Settings.

    :param password_provided:
    :return:
    """

    password = password_provided.encode()  # Convert to type bytes
    salt = Settings.SALT.encode()  # CHANGE THIS - recommend using a key from os.urandom(16), must be of type bytes
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))  # Can only use kdf once
    return key


def encrypt(message, password):
    """
    You can use this for protecting player files. The user then enters the password to be passed. This isn't useful if
    the user doesn't/can't enter a password at some time.

    :param message:
    :param password:
    :return:
    """

    message = message.encode()

    f = Fernet(getkey(password))
    encrypted = f.encrypt(message)
    return encrypted


def encrypt_default_password(message):
    """
    You Can Use this for internal data (Aka Non-User controlled data) that needs to be encrypted.

    :param message:
    :return:
    """

    message = message.encode()

    f = Fernet(getkey(Settings.ENCRYPTION_PASSWORD))
    encrypted = f.encrypt(message)
    return encrypted


def decrypt(message, password):
    """
    You can use this for reading protected player files. The user then enters the password to be passed. This isn't
    useful if the user doesn't/can't enter a password at some time.

    :param message:
    :param password:
    :return:
    """

    if type(message) == bytes:
        f = Fernet(getkey(Settings.ENCRYPTION_PASSWORD))
        decrypted = f.decrypt(message)
    else:
        raise TypeError("Passed a string object to a function accepting only bytes objects as input.")


def decrypt_default_password(message):
    """
    You Can Use this for internal data (Aka Non-User controlled data) that needs to be encrypted.

    :param message:
    :return:
    """

    if type(message) == bytes:
        f = Fernet(getkey(Settings.ENCRYPTION_PASSWORD))
        decrypted = f.decrypt(message)
        return decrypted
    else:
        raise TypeError("Passed a string object to a function accepting only bytes objects as input.")
