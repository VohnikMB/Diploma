from ui.imports_ui import *

select = True

def open_file_dialog():
    global select

    # Відкрити діалогове вікно для вибору файлу
    file_path, _ = QFileDialog.getOpenFileName(None, 'Обрати файл', '', 'Text Files (*.txt);;All Files (*)')

    # Якщо файл обрано
    if file_path:
        with open(file_path, 'r', encoding='utf-8') as file:
            file_content = file.read()
        select = True
        print(f"File selected, select: {select}")  # Додаємо перевірку
        return file_content
    else:
        select = False
        print(f"No file selected, select: {select}")  # Додаємо перевірку
        return "None"
