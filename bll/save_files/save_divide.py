"""
Файл що містить функцію для збереження розділених файлів.

Функція:
    - save_file: Зберігає зашифрованні дані у розділенні файли.
"""


def save_file(index_range, decrypted_data, files_location):
    for i in index_range:
        with open(files_location[i], 'wb') as decrypted_file:
            decrypted_file.write(decrypted_data[i])
    return True
