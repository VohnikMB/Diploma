from bll.bll_imports import *

"""
select_files.py. Файл, що містить функцію для вибору файлів.

Функція:
    - open_file_dialog: Відкриває діалогове вікно для вибору одного або кількох файлів, повертає список вибраних файлів.
"""


def open_file_dialog():
    files, _ = QtWidgets.QFileDialog.getOpenFileNames(
        None,
        "Виберіть файли",
        "",
        'All Files (*)'
    )
    file_names = []
    if files:
        for file_path in files:
            file_names.append(file_path)
        return file_names, True
    else:
        return None, False
