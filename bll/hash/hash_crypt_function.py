import base64
import hashlib
from cryptography.fernet import Fernet

def _generate_fernet_key_from_password(password):
    # Створення хешу SHA-256 з паролю
    hash = hashlib.sha256(password.encode()).digest()
    # Використання перших 32 байт як ключ
    return base64.urlsafe_b64encode(hash)

def _get_key_from_password_sha512(password):
    # Хешуємо пароль за допомогою SHA-512
    key = hashlib.sha512(password.encode()).digest()
    # Конвертуємо перші 32 байти в base64
    return base64.urlsafe_b64encode(key[:32])

def _hash_with_user_salt(data, user_salt):
    # Хешуємо дані з сіллю за допомогою SHA-256
    salt = user_salt.encode('utf-8')
    data_bytes = data.encode('utf-8')
    salted_data = salt + data_bytes
    hash_object = hashlib.sha256(salted_data)
    return hash_object.digest()  # Повертаємо байти

def encrypt_data(data, password, type, salt):
    # Вибір методу хешування
    if type == "sha512":
        key = _get_key_from_password_sha512(password)
    elif type == "md5":
        key = _generate_fernet_key_from_password(password)
    else:  # Вважається, що тип є "salt"
        key = _hash_with_user_salt(password, salt)
        key = base64.urlsafe_b64encode(hashlib.sha256(key).digest()[:32])

    # Шифрування даних
    cipher_suite = Fernet(key)
    data_bytes = data.encode('utf-8')
    encrypted_data = cipher_suite.encrypt(data_bytes)
    return encrypted_data

def decrypt_data(encrypted_data, password, type, salt=''):
    # Вибір методу хешування
    if type == "sha512":
        key = _get_key_from_password_sha512(password)
    elif type == "md5":
        key = _generate_fernet_key_from_password(password)
    else:  # Вважається, що тип є "salt"
        key = _hash_with_user_salt(password, salt)
        key = base64.urlsafe_b64encode(hashlib.sha256(key).digest()[:32])

    # Дешифрування даних
    cipher_suite = Fernet(key)
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    return decrypted_data.decode('utf-8')
