from bll.bll_imports import *


"""
Файл що містить функції для об'єднання вмісту і збереження файлів.

Функції:
    - encrypted_file_content: Об'єднує вміст зашифрованих файлів в один байтовий ряд.
    - save_decrypted_file: Зберігає розшифрований вміст у файл.
"""


def encrypted_file_content(data):
    file_content = b""
    for file_path in data:
        with open(file_path, 'rb') as file:
            part = file.read()
            file_content += part
    return file_content


def save_decrypted_file(page, content, file_name):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    file_path, _ = QFileDialog.getSaveFileName(
        page,
        "Оберіть місце для збереження файлу",
        file_name,
        "All Files (*)",
        options=options,
    )
    if file_path:
        with open(file_path, 'wb') as file:
            file.write(content)
        return True
