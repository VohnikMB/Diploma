from ui.imports_ui import *


def open_file_dialog():
    # Відкриття діалогу для вибору файлів
    files, _ = QtWidgets.QFileDialog.getOpenFileNames(
        None,
        "Виберіть файли",  # Заголовок діалогу
        "",  # Початкова директорія
        'All Files (*)'  # Фільтр файлів
    )

    # Ініціалізація змінної для зберігання вмісту файлів
    # file_content = b""  # Порожній байтовий об'єкт
    file_names = []
    if files:
        # Читання вмісту кожного файлу
        for file_path in files:
            file_names.append(file_path)
        return file_names, True
    else:
        return None, False
