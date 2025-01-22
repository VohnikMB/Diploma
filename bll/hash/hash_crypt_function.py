import base64
import hashlib
from cryptography.fernet import Fernet

"""
Модуль для хешування та шифрування даних.

Функції:
    - _generate_fernet_key_from_password: Генерує ключ для шифрування з пароля, використовуючи BLAKE2b.
    - _get_key_from_password_sha512: Генерує ключ для шифрування з пароля, використовуючи SHA-512.
    - _hash_with_user_salt: Генерує ключ для шифрування з додаванням модифікатора(сіль).
    - encrypt_data: Шифрує дані за допомогою пароля та заданого методу хешування.
    - decrypt_data: Розшифровує дані за допомогою пароля та заданого методу хешування.

Залежності:
    - base64: Для кодування/декодування ключів.
    - hashlib: Для хешування паролів.
    - cryptography.fernet: Для шифрування та дешифрування даних.
"""


def _generate_fernet_key_from_password(password):
    key = hashlib.blake2b(password.encode(), digest_size=32).digest()
    return base64.urlsafe_b64encode(key)


def _get_key_from_password_sha512(password):
    key = hashlib.sha512(password.encode()).digest()
    return base64.urlsafe_b64encode(key[:32])


def _hash_with_user_salt(data, user_salt):
    # Перевірка, чи є пароль і сіль байтами, і якщо ні, то кодуємо їх
    salt_bytes = user_salt.encode() if isinstance(user_salt, str) else user_salt
    data_bytes = data.encode() if isinstance(data, str) else data

    # Хешуємо дані з сіллю
    salted_data = salt_bytes + data_bytes
    hash_object = hashlib.sha256(salted_data)
    return hash_object.digest()


def encrypt_data(data, password, hash_type, salt):
    # Вибір методу хешування
    match hash_type:
        case "sha512":
            key = _get_key_from_password_sha512(password)
        case "BLAKE2b":
            key = _generate_fernet_key_from_password(password)
        case _:
            key = _hash_with_user_salt(password, salt)
            key = base64.urlsafe_b64encode(hashlib.sha256(key).digest()[:32])

    # Шифрування даних
    cipher_suite = Fernet(key)
    encrypted_data = cipher_suite.encrypt(data)
    return encrypted_data


def decrypt_data(encrypted_data, password, hash_type, salt=''):
    # Вибір методу хешування
    match hash_type:
        case "sha512":
            key = _get_key_from_password_sha512(password)
        case "BLAKE2b":
            key = _generate_fernet_key_from_password(password)
        case _:
            key = _hash_with_user_salt(password, salt)
            key = base64.urlsafe_b64encode(hashlib.sha256(key).digest()[:32])

    # Розшифрування даних
    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    return decrypted_data
