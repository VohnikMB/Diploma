from ui.imports_ui import *
from ui.password_salt_form import open_password_salt_form
from bll.save_files.save_decrypted import *
from bll.hash.hash_crypt_function import decrypt_data

"""
create_de_frag_page.py. Файл, що містить функції для створення сторінки дешифрування.

Елементи Qt:
    - QPushButton:
        - push_button_forward: Кнопка "Далі", активується за умови заповнення щонайменше двох полів.
        - push_button_back: Кнопка "Назад", повертає на початкову сторінку.
    - QLineEdit:
        - location_fields: Поля для введення шляхів до шифрованих файлів (до 8 полів).
    - QRadioButton:
        - salt_radio_button: Радіокнопка для вибору алгоритму sha256+salt.
        - blake_radio_button: Радіокнопка для вибору алгоритму BLAKE2b.
        - sha521_radio_button: Радіокнопка для вибору алгоритму sha512.
    - ClickableLabel:
        - location_buttons: Кнопки з іконкою папки для відкриття діалогів вибору файлів.
Функції:
    - create_de_frag_page: Головна функція, що включає інтерфейс для введення шляхів до файлів, вибір алгоритмів хешування, тощо.
    - update_push_button_state: Відповідає за активацію/деактивацію кнопки "Далі".
    - open_file_dialog: Відкриває менеджер для вибору шифрованого файлу.
    - radio_button_click: Змінює вибраний алгоритм хешування.
    - start_decryption: Запускає процес дешифрування з урахуванням введеного пароля, солі та вибраного алгоритму.
"""


def create_de_frag_page(parent, files_name):
    page = QtWidgets.QWidget(parent)
    type_hash = "BLAKE2b"

    push_button_forward = QtWidgets.QPushButton(page)
    push_button_forward.setGeometry(QtCore.QRect(730, 560, 141, 51))
    push_button_forward.setObjectName("push_button_forward")
    push_button_forward.setText("Далі")
    push_button_forward.setStyleSheet(root.find(".//text[@id='style_push_button_start_frag_NA']").text.strip())
    push_button_forward.setEnabled(False)

    push_button_back = QtWidgets.QPushButton(page)
    push_button_back.setGeometry(QtCore.QRect(120, 560, 141, 51))
    push_button_back.setObjectName("push_button_back")
    push_button_back.setText("Назад")
    push_button_back.setStyleSheet(root.find(".//text[@id='style_push_button_main']").text.strip())
    push_button_back.clicked.connect(parent.show_start_page)

    location_fields = []

    for i in range(8):
        location_field = QtWidgets.QLineEdit(page)
        location_field.setGeometry(QtCore.QRect(160, 40 + i * 60, 671, 41))
        location_field.setObjectName(f"locatio_{i}")
        if files_name is not None and i < len(files_name):
            location_field.setText(str(files_name[i]))
        location_fields.append(location_field)

    def update_push_button_state():
        filled_fields = sum(1 for field in location_fields if field.text().strip())
        if filled_fields >= 2:
            push_button_forward.setStyleSheet(root.find(".//text[@id='style_push_button_start_frag']").text.strip())
            push_button_forward.setEnabled(True)
        else:
            push_button_forward.setStyleSheet(root.find(".//text[@id='style_push_button_start_frag_NA']").text.strip())
            push_button_forward.setEnabled(False)

    for field in location_fields:
        field.textChanged.connect(update_push_button_state)

    location_buttons = []
    for i in range(8):
        def open_file_dialog(index):
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            file_path, _ = QFileDialog.getOpenFileName(
                page,
                "Виберіть файл для фрагменту",
                "",
                "All Files (*)",
                options=options,
            )
            if file_path:
                location_fields[index].setText(file_path)
            else:
                pass

        location_button = ClickableLabel(page)
        location_button.setGeometry(QtCore.QRect(850, 30 + i * 60, 71, 61))
        location_button.setStyleSheet("image: url(ui/images/folder.png);")
        location_button.setObjectName(f"folder_{i}")
        location_button.clicked.connect(partial(open_file_dialog, i))
        location_buttons.append(location_button)

    font = QtGui.QFont()
    font.setFamily("Arial Black")
    font.setPointSize(8)
    font.setBold(True)
    font.setUnderline(False)
    font.setWeight(75)
    font.setStrikeOut(False)

    label = QtWidgets.QLabel(page)
    label.setGeometry(QtCore.QRect(0, 510, 961, 31))
    label.setFont(font)
    label.setAutoFillBackground(False)
    label.setObjectName("label")

    label_2 = QtWidgets.QLabel(page)
    label_2.setGeometry(QtCore.QRect(20, 530, 951, 31))
    label_2.setFont(font)
    label_2.setAutoFillBackground(False)
    label_2.setObjectName("label_2")

    label.setText(root.find(".//text[@id='red_txt1']").text.strip())
    label_2.setText(root.find(".//text[@id='red_txt2']").text.strip())

    # Додаємо радіо-кнопки
    salt_radio_button = QtWidgets.QRadioButton(page)
    salt_radio_button.setGeometry(QtCore.QRect(40, 300, 141, 17))
    salt_radio_button.setFont(QtGui.QFont('', 11))
    salt_radio_button.setText("sha256+salt")
    salt_radio_button.setStyleSheet(root.find(".//text[@id='style_radio_button']").text.strip())
    salt_radio_button.setObjectName("salt")

    blake_radio_button = QtWidgets.QRadioButton(page)
    blake_radio_button.setGeometry(QtCore.QRect(40, 220, 141, 17))
    blake_radio_button.setFont(QtGui.QFont('', 11))
    blake_radio_button.setText("BLAKE2b")
    blake_radio_button.setChecked(True)
    blake_radio_button.setObjectName("BLAKE2b")
    blake_radio_button.setStyleSheet(root.find(".//text[@id='style_radio_button']").text.strip())

    sha521_radio_button = QtWidgets.QRadioButton(page)
    sha521_radio_button.setGeometry(QtCore.QRect(40, 260, 141, 17))
    sha521_radio_button.setFont(QtGui.QFont('', 11))
    sha521_radio_button.setText("sha512")
    sha521_radio_button.setObjectName("sha512")
    sha521_radio_button.setStyleSheet(root.find(".//text[@id='style_radio_button']").text.strip())

    sha521_radio_button.toggled.connect(lambda: radio_button_click("sha512", sha521_radio_button.isChecked()))
    blake_radio_button.toggled.connect(lambda: radio_button_click("BLAKE2b", blake_radio_button.isChecked()))
    salt_radio_button.toggled.connect(lambda: radio_button_click("salt", salt_radio_button.isChecked()))

    def radio_button_click(selected_type, is_checked):
        nonlocal type_hash
        if is_checked:
            type_hash = selected_type

    match os.path.basename(location_fields[0].text())[:2]:
        case "sh":
            sha521_radio_button.setChecked(True)
        case "b2":
            blake_radio_button.setChecked(True)
        case "ss":
            salt_radio_button.setChecked(True)
        case _:
            pass

    def start_decryption(password, salt):
        location_field_txt = []
        for file in location_fields:
            field_text = file.text().strip()
            if field_text:
                location_field_txt.append(field_text)
        file_name = os.path.basename(location_field_txt[0])
        if file_name[:2] in ["ss", "b2", "sh"]:
            file_name = file_name[4:-1]

        decrypted_content = decrypt_data(encrypted_file_content(location_field_txt), password, type_hash, salt)
        if save_decrypted_file(page, decrypted_content, str(file_name)):
            parent.show_start_page()

    push_button_forward.clicked.connect(lambda: open_password_salt_form(page, start_decryption, type_hash))
    update_push_button_state()

    return page
