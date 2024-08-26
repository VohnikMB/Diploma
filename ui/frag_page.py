from ui.imports_ui import *


def create_frag_page(parent):
    page = QtWidgets.QWidget(parent)

    # Додаємо зображення
    choose_file_img = QtWidgets.QLabel(page)
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
    salt_radio_button.setObjectName("salt_radio_button")

    md5_radio_button = QtWidgets.QRadioButton(page)
    md5_radio_button.setGeometry(QtCore.QRect(720, 215, 141, 17))
    md5_radio_button.setFont(QtGui.QFont('', 11))
    md5_radio_button.setText("md5")
    md5_radio_button.setChecked(True)
    md5_radio_button.setObjectName("md5_radio_button")
    md5_radio_button.setStyleSheet(root.find(".//text[@id='style_radio_button']").text.strip())

    sha521_radio_button = QtWidgets.QRadioButton(page)
    sha521_radio_button.setGeometry(QtCore.QRect(720, 255, 141, 17))
    sha521_radio_button.setFont(QtGui.QFont('', 11))
    sha521_radio_button.setText("sha512")
    sha521_radio_button.setObjectName("sha521_radio_button")
    sha521_radio_button.setStyleSheet(root.find(".//text[@id='style_radio_button']").text.strip())

    # Додаємо поле введення для "сіль"
    salt_line = QtWidgets.QLineEdit(page)
    salt_line.setGeometry(QtCore.QRect(530, 290, 151, 31))
    salt_line.setText("1111")
    salt_line.setStyleSheet("border: none;")

    salt_line.setObjectName("salt_line")

    # Налаштовуємо кнопки для переходу на інші сторінки
    push_button_main.clicked.connect(parent.show_start_page)  # Повернення на головну сторінку
    push_button_frag.clicked.connect(lambda: print("Кнопка 'Далі' натиснута"))  # Дія для кнопки 'Далі'

    return page
