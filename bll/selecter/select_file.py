from bll.bll_imports import *


"""
select_file.py. Файл, що містить функцію для вибору файлу.

Функція:
    - open_file_dialog: Відкриває діалогове вікно для вибору файлу, повертає його ім'я і вміст(бітовий).
"""


def open_file_dialog():
    file_path, _ = QFileDialog.getOpenFileName(None, 'Обрати файл', '', 'All Files (*)')
    if file_path:
        with open(file_path, 'rb') as file:
            file_content = file.read()
        file_name = os.path.basename(file_path)
        return file_content, file_name, True
    else:
        return None, None, False
