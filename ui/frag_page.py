from bll.selecter.select_file import *
from bll.hash.hash_crypt_function import *
from ui.password_form import *
from ui.imports_ui import *

"""
create_frag_page.py. Модуль, що містить функцію створення сторінки налаштування шифрування та розділення файлів.

Елементи Qt:
     - QPushButton:
        - push_button_frag: Кнопка для переходу до наступного етапу.
        - push_button_main: Кнопка для повернення на попередню сторінку.
    - QSlider: Слайдер для вибору кількості фрагментів поділу, від 2 до 8.
    - QLabel: Текст слайдера.
    - QRadioButton:
        - blake_radio_button: Вибір алгоритму "BLAKE2b" (встановлений за замовчуванням).
        - salt_radio_button: Вибір алгоритму "sha256+salt".
        - sha521_radio_button: Вибір алгоритму "sha512".
    - QLineEdit:
            - salt_line: Поле для введення значення солі.

Функції:
    - create_frag_page: Створює сторінку для вибору файлу, налаштування шифрування та розділення на фрагменти.
    - radio_button_click: Обробляє події перемикання радіо-кнопок для вибору алгоритму.
    - encrypt_file_content: Відкриває діалог вибору файлу для шифрування.
    - start_encryption: Розпочинає шифрування даних і перенаправляє на наступну сторінку.
"""


def create_frag_page(parent):
    page = QtWidgets.QWidget(parent)
    file_content = None
    file_name = None
    type_hash = "BLAKE2b"

    choose_file_img = ClickableLabel(page)
    choose_file_img.setGeometry(QtCore.QRect(90, 180, 221, 201))
    choose_file_img.setAutoFillBackground(False)
    choose_file_img.setText("")
    choose_file_img.setStyleSheet("image: url(ui/images/pickFile.png);")
    choose_file_img.setScaledContents(True)
    choose_file_img.setObjectName("choose_file_img")

    push_button_frag = QtWidgets.QPushButton(page)
    push_button_frag.setGeometry(QtCore.QRect(730, 560, 141, 51))
    push_button_frag.setText("Далі")
    push_button_frag.setStyleSheet(root.find(".//text[@id='style_push_button_start_frag_NA']").text.strip())
    push_button_frag.setObjectName("push_button_frag")

    push_button_main = QtWidgets.QPushButton(page)
    push_button_main.setGeometry(QtCore.QRect(130, 560, 141, 51))
    push_button_main.setText("Назад")
    push_button_main.setStyleSheet(root.find(".//text[@id='style_push_button_main']").text.strip())
    push_button_main.setObjectName("push_button_main")

    slider = QtWidgets.QSlider(page)
    slider.setGeometry(QtCore.QRect(714, 345, 151, 22))
    slider.setMinimum(2)
    slider.setMaximum(8)
    slider.setOrientation(QtCore.Qt.Horizontal)
    slider.setObjectName("slider")
    slider.setStyleSheet(root.find(".//text[@id='style_slider']").text.strip())

    slaider_text = QtWidgets.QLabel(page)
    slaider_text.setGeometry(QtCore.QRect(530, 345, 151, 22))
    font = QtGui.QFont()
    font.setPointSize(11)
    slaider_text.setFont(font)
    slaider_text.setText("Кількість фрагментів:")
    slaider_text.setObjectName("slaider_text")

    salt_radio_button = QtWidgets.QRadioButton(page)
    salt_radio_button.setGeometry(QtCore.QRect(720, 295, 141, 17))
    salt_radio_button.setFont(QtGui.QFont('', 11))
    salt_radio_button.setText("sha256+salt")
    salt_radio_button.setStyleSheet(root.find(".//text[@id='style_radio_button']").text.strip())
    salt_radio_button.setObjectName("salt")

    blake_radio_button = QtWidgets.QRadioButton(page)
    blake_radio_button.setGeometry(QtCore.QRect(720, 215, 141, 17))
    blake_radio_button.setFont(QtGui.QFont('', 11))
    blake_radio_button.setText("BLAKE2b")
    blake_radio_button.setChecked(True)
    blake_radio_button.setObjectName("BLAKE2b")
    blake_radio_button.setStyleSheet(root.find(".//text[@id='style_radio_button']").text.strip())

    sha521_radio_button = QtWidgets.QRadioButton(page)
    sha521_radio_button.setGeometry(QtCore.QRect(720, 255, 141, 17))
    sha521_radio_button.setFont(QtGui.QFont('', 11))
    sha521_radio_button.setText("sha512")
    sha521_radio_button.setObjectName("sha512")
    sha521_radio_button.setStyleSheet(root.find(".//text[@id='style_radio_button']").text.strip())

    sha521_radio_button.toggled.connect(lambda: radio_button_click("sha512", sha521_radio_button.isChecked()))
    blake_radio_button.toggled.connect(lambda: radio_button_click("BLAKE2b", blake_radio_button.isChecked()))
    salt_radio_button.toggled.connect(lambda: radio_button_click("salt", salt_radio_button.isChecked()))

    salt_line = QtWidgets.QLineEdit(page)
    salt_line.setGeometry(QtCore.QRect(530, 290, 151, 31))
    salt_line.setText("1111")
    salt_line.setStyleSheet("border: none;")
    salt_line.setObjectName("salt_line")
    salt_line.setEnabled(False)
    push_button_frag.setEnabled(False)

    def radio_button_click(selected_type, is_checked):
        nonlocal type_hash
        if is_checked:
            type_hash = selected_type
        if selected_type == "salt":
            salt_line.setEnabled(True)
        else:
            salt_line.setEnabled(False)

    def encrypt_file_content():
        nonlocal file_content
        nonlocal file_name
        file_content, file_name, bool_info = open_file_dialog()
        if bool_info:
            push_button_frag.setStyleSheet(root.find(".//text[@id='style_push_button_start_frag']").text.strip())
            push_button_frag.setEnabled(True)

        else:
            push_button_frag.setStyleSheet(root.find(".//text[@id='style_push_button_start_frag_NA']").text.strip())
            push_button_frag.setEnabled(False)

    def start_encryption(password):
        encrypted_data = encrypt_data(file_content, password, type_hash, salt_line.text())
        parent.show_frag_location_page(slider.value(), type_hash, encrypted_data, file_name)

    choose_file_img.clicked.connect(encrypt_file_content)
    push_button_frag.clicked.connect(lambda: open_password_form(page, start_encryption))
    push_button_main.clicked.connect(parent.show_start_page)

    return page
