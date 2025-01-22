from ui.imports_ui import *
from bll.save_files.divide_function import *
from bll.save_files.save_divide import save_file

"""
frag_location_page.py. Файл, що містить функцію для створення сторінки вибору місць збереження фрагментованих даних.

Елементи Qt:
    - QPushButton:
        - push_button_forward: Кнопка "Готово" для завершення вибору та переходу до стартової сторінки.
        - push_button_back: Кнопка "Назад" для повернення до попередньої сторінки.
    - QLineEdit:
        - location_field: Поля для введення або відображення шляху до файлу фрагменту.
    - ClickableLabel:
        - location_button: Іконки "папка" для виклику діалогу вибору шляху збереження.

Функції:
    - create_frag_location_page: Створює сторінку для налаштування місць збереження фрагментованих даних.
    - open_file_dialog: Викликає діалогове вікно для вибору місця збереження окремого фрагменту.
    - end_fun: Завершує процес збереження фрагментів, перевіряє шляхи та викликає функцію `save_file`.
    - re_read: Повертає список(масив) адрес із текстових полів.
"""


def create_frag_location_page(parent, slider, hash_type, data, file_name):
    page = QtWidgets.QWidget(parent)
    push_button_forward = QtWidgets.QPushButton(page)
    push_button_forward.setGeometry(QtCore.QRect(730, 560, 141, 51))
    push_button_forward.setObjectName("push_button_forward")
    push_button_forward.setText("Готово")
    push_button_forward.setStyleSheet(root.find(".//text[@id='style_push_button_start_frag']").text.strip())
    push_button_forward.clicked.connect(lambda: end_fun())

    push_button_back = QtWidgets.QPushButton(page)
    push_button_back.setGeometry(QtCore.QRect(130, 560, 141, 51))
    push_button_back.setObjectName("push_button_back")
    push_button_back.setText("Назад")
    push_button_back.clicked.connect(parent.show_frag_page)
    push_button_back.setStyleSheet(root.find(".//text[@id='style_push_button_main']").text.strip())

    data_divide = divide_data(data, slider)
    files_name = divide_files_name(slider, hash_type, file_name)
    location_fields = []
    for i in range(slider):
        location_field = QtWidgets.QLineEdit(page)
        location_field.setGeometry(QtCore.QRect(130, 40 + i * 60, 671, 41))
        location_field.setObjectName(f"locatio_{i}")
        location_field.setText(f"save/{files_name[i]}")
        location_fields.append(location_field)

    location_buttons = []
    for i in range(slider):
        def open_file_dialog(index):
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            file_path, _ = QFileDialog.getSaveFileName(
                page,
                "Виберіть місце для збереження фрагменту",
                f"save/{files_name[index]}",
                "All Files (*)",
                options=options,
            )
            if file_path:
                location_fields[index].setText(file_path)

        location_button = ClickableLabel(page)
        location_button.setGeometry(QtCore.QRect(820, 30 + i * 60, 71, 61))
        location_button.setStyleSheet("image: url(ui/images/folder.png);")
        location_button.setObjectName(f"folder_{i}")
        location_buttons.append(location_button)

        location_button.clicked.connect(partial(open_file_dialog, i))
        location_buttons.append(location_button)

    def end_fun():
        """Фінальна функція збереження."""
        files_location = re_read(range(slider))
        if all(files_location) and save_file(range(slider), data_divide, files_location):
            parent.show_start_page()

    def re_read(index_range):
        return [location_fields[index].text() for index in index_range]

    return page
