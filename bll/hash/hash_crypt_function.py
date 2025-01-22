import base64
import hashlib
from hashlib import scrypt
from cryptography.fernet import Fernet


def _generate_fernet_key_from_password(password):
    # Хешуємо пароль за допомогою BLAKE2b
    hash = hashlib.blake2b(password.encode(), digest_size=32).digest()
    # Кодуємо ключ у base64
    key_base64 = base64.urlsafe_b64encode(hash)
    return key_base64


def _get_key_from_password_sha512(password):
    # Хешуємо пароль за допомогою SHA-512
    key = hashlib.sha512(password.encode()).digest()
    # Конвертуємо перші 32 байти в base64
    return base64.urlsafe_b64encode(key[:32])


def _hash_with_user_salt(data, user_salt):
    # Перевірка, чи є сіль байтами, і якщо ні, то кодуємо її
    salt_bytes = user_salt.encode() if isinstance(user_salt, str) else user_salt
    # Перевірка, чи є дані байтами, і якщо ні, то кодуємо їх
    data_bytes = data.encode() if isinstance(data, str) else data

    # Хешуємо дані з сіллю
    salted_data = salt_bytes + data_bytes
    hash_object = hashlib.sha256(salted_data)
    return hash_object.digest()  # Повертаємо байти


def encrypt_data(data, password, type, salt):
    # Вибір методу хешування
    if type == "sha512":
        key = _get_key_from_password_sha512(password)
    elif type == "BLAKE2b":
        key = _generate_fernet_key_from_password(password)
    else:  # Вважається, що тип є "salt"
        key = _hash_with_user_salt(password, salt)
        key = base64.urlsafe_b64encode(hashlib.sha256(key).digest()[:32])

    # Шифрування даних
    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data)
    return encrypted_data


def decrypt_data(encrypted_data, password, type, salt=''):
    # Вибір методу хешування
    if type == "sha512":
        key = _get_key_from_password_sha512(password)
    elif type == "BLAKE2b":
        key = _generate_fernet_key_from_password(password)
    else:  # Вважається, що тип є "salt"
        key = _hash_with_user_salt(password, salt)
        key = base64.urlsafe_b64encode(hashlib.sha256(key).digest()[:32])

    # Дешифрування даних
    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    return decrypted_data
