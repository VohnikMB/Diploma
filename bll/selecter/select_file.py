from ui.imports_ui import *


def open_file_dialog():
    file_path, _ = QFileDialog.getOpenFileName(None, 'Обрати файл', '', 'All Files (*)')
    if file_path:
        # Отримуємо вміст файлу
        with open(file_path, 'rb') as file:
            file_content = file.read()
        file_name = os.path.basename(file_path)
        return file_content, file_name, True
    else:
        return None, None, False
