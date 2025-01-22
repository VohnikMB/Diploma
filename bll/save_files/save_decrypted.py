from ui.imports_ui import *


def encrypted_file_content(data):
    file_content = b""
    for file_path in data:
        with open(file_path, 'rb') as file:
            part = file.read()
            print(f"Read {len(part)} bytes from {file_path}")
            file_content += part
    print(f"Total encrypted content length: {len(file_content)}")
    return file_content


def save_decrypted_file(page, content, file_name):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    file_path, _ = QFileDialog.getSaveFileName(
        page,
        "Оберіть місце для збереження файлу",
        file_name,  # Початкова назва файлу
        "All Files (*)",  # Фільтр файлів
        options=options,
    )
    print("save_decrypted_file DONE")
    if file_path:  # Якщо користувач обрав файл
        with open(file_path, 'wb') as file:  # Відкриваємо файл на запис
            file.write(content)
        print("file_path DONE")
        return True
