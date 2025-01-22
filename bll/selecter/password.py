from bll.bll_imports import *


"""
password.py. Файл, що містить функцію для вибору паролю з файлового носія.

Функція:
    - select_pass_file: Відкриває діалогове вікно для вибору файлу-ключа(відповідного формату), повертає його вміст.
"""


def select_pass_file():

    file_path, _ = QFileDialog.getOpenFileName(None, 'Обрати файл', ''
                                               , 'Password Files (*.txt; *.key; *.secrets);;All Files (*)')
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()
        return file_content, True
    else:
        return None, False
