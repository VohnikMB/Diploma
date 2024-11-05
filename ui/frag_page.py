from ui.imports_ui import *
from bll.select_file import *
from bll.hash.hash_crypt_function import *
from ui.password_form import *


def create_frag_page(parent):
    page = QtWidgets.QWidget(parent)
    encrypted_data = None  # Initialize a variable to store the encrypted data
    type_hash = "md5"

    # Додаємо зображення
    choose_file_img = ClickableLabel(page)
    choose_file_img.setGeometry(QtCore.QRect(90, 180, 221, 201))
    choose_file_img.setAutoFillBackground(False)
    choose_file_img.setText("")
    choose_file_img.setStyleSheet("image: url(ui/images/pickFile.png);")
    choose_file_img.setScaledContents(True)
    choose_file_img.setObjectName("choose_file_img")

    # Додаємо кнопки
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

    # Додаємо слайдер
    slider = QtWidgets.QSlider(page)
    slider.setGeometry(QtCore.QRect(714, 345, 151, 22))
    slider.setMinimum(2)
    slider.setMaximum(8)
    slider.setOrientation(QtCore.Qt.Horizontal)
    slider.setObjectName("slider")
    slider.setStyleSheet(root.find(".//text[@id='style_slider']").text.strip())

    # Додаємо текст слайдера
    slaider_text = QtWidgets.QLabel(page)
    slaider_text.setGeometry(QtCore.QRect(530, 345, 151, 22))
    font = QtGui.QFont()
    font.setPointSize(11)
    slaider_text.setFont(font)
    slaider_text.setText("Кількість фрагментів:")
    slaider_text.setObjectName("slaider_text")

    # Додаємо радіо-кнопки
    salt_radio_button = QtWidgets.QRadioButton(page)
    salt_radio_button.setGeometry(QtCore.QRect(720, 295, 141, 17))
    salt_radio_button.setFont(QtGui.QFont('', 11))
    salt_radio_button.setText("sha256+salt")
    salt_radio_button.setStyleSheet(root.find(".//text[@id='style_radio_button']").text.strip())
    salt_radio_button.setObjectName("salt")

    md5_radio_button = QtWidgets.QRadioButton(page)
    md5_radio_button.setGeometry(QtCore.QRect(720, 215, 141, 17))
    md5_radio_button.setFont(QtGui.QFont('', 11))
    md5_radio_button.setText("md5")
    md5_radio_button.setChecked(True)
    md5_radio_button.setObjectName("md5")
    md5_radio_button.setStyleSheet(root.find(".//text[@id='style_radio_button']").text.strip())

    sha521_radio_button = QtWidgets.QRadioButton(page)
    sha521_radio_button.setGeometry(QtCore.QRect(720, 255, 141, 17))
    sha521_radio_button.setFont(QtGui.QFont('', 11))
    sha521_radio_button.setText("sha512")
    sha521_radio_button.setObjectName("sha512")
    sha521_radio_button.setStyleSheet(root.find(".//text[@id='style_radio_button']").text.strip())

    sha521_radio_button.toggled.connect(lambda: radio_button_click("sha521", sha521_radio_button.isChecked()))
    md5_radio_button.toggled.connect(lambda: radio_button_click("md5", md5_radio_button.isChecked()))
    salt_radio_button.toggled.connect(lambda: radio_button_click("salt", salt_radio_button.isChecked()))

    # Додаємо поле введення для "сіль"
    salt_line = QtWidgets.QLineEdit(page)
    salt_line.setGeometry(QtCore.QRect(530, 290, 151, 31))
    salt_line.setText("1111")
    salt_line.setStyleSheet("border: none;")
    salt_line.setObjectName("salt_line")
    salt_line.setEnabled(False)

    def radio_button_click(selected_type, is_checked):
        nonlocal type_hash
        if is_checked:
            type_hash = selected_type
            print(type_hash)
        if selected_type == "salt":
            salt_line.setEnabled(True)
        else:
            salt_line.setEnabled(False)

    def check_and_style_button():
        print(f"Current select value: {select}")  # Додаємо виведення значення змінної select
        if select:
            print("Applying selected style.")  # Додаємо перевірку
            push_button_frag.setStyleSheet(root.find(".//text[@id='style_push_button_start_frag']").text.strip())
        else:
            print("Applying not selected style.")  # Додаємо перевірку
            push_button_frag.setStyleSheet(root.find(".//text[@id='style_push_button_start_frag_NA']").text.strip())

        push_button_frag.update()  # Примусово оновлюємо кнопку
        push_button_frag.repaint()  # Примусово перерендерюємо

    def encrypt_file_content():
        global select  # Використовуємо глобальну змінну select
        nonlocal encrypted_data  # Access the outer scope variable
        file_content = open_file_dialog()  # Після цього select стає True або False

        # Оновлюємо стиль кнопки одразу після вибору файлу
        check_and_style_button()  # Викликаємо функцію для перевірки стилю одразу після вибору файлу

        if file_content != "None":  # Якщо файл обрано, продовжуємо
            encrypted_data = encrypt_data(file_content, "40002", type_hash, salt_line.text())
            print(encrypted_data)
        else:
            print("No file selected")

    def decrypt_data_content():
        if encrypted_data is not None:
            print(encrypted_data)
            decrypted_data = decrypt_data(encrypted_data, "40002", type_hash, salt_line.text())
            print(decrypted_data)
        else:
            print("No encrypted data available for decryption.")



    choose_file_img.clicked.connect(encrypt_file_content)  # Pass the function reference without parentheses

    push_button_frag.clicked.connect(lambda: open_password_form(page))
    push_button_main.clicked.connect(parent.show_start_page)  # Navigate to the start page

    return page


