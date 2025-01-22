from bll.selecter.password import *

"""
password_salt_form.py. Файл містить функцію `open_password_salt_form`, 
 яка створює графічний інтерфейс вікна для вводу пароля та, за необхідності, хеш-солі.

Елементи Qt:
    - ClickableLabel:
        - self.eye: Іконка для відображення/приховування введеного пароля.
        - self.file_password: Іконка для завантаження пароля з файлу.
    - QLineEdit:
        - self.password_line: Поле для введення пароля.
        - self.salt_line: Поле для введення значення солі.
    - QPushButton:
        - self.push_button_back: Кнопка для закриття вікна (Назад).
        - self.push_button_submit: Кнопка для підтвердження введення (Далі).

Функції:
    - open_password_salt_form: Створює вікно для введення пароля та налаштовує всі інтерактивні елементи.
    - submit_password: Передає введені значення пароля та солі до функції обробки (start_decryption) і закриває вікно.
    - password_in_file: Відкриває діалог вибору файлу, отримує пароль з файлу та вставляє його у відповідне поле.
    - toggle_password_visibility: Перемикає режим відображення пароля (звичайний текст або прихований).
    - check_password_match: Перевіряє заповненість обов'язкових полів і активує або деактивує кнопку "Далі".
"""


def open_password_salt_form(self, start_decryption, salt):
    self.salt = salt
    self.password_window = QtWidgets.QMainWindow()
    self.password_window.setWindowTitle('Enter Password')
    self.password_window.setFixedSize(420, 235)

    central_widget = QtWidgets.QWidget()
    self.password_window.setCentralWidget(central_widget)

    layout = QtWidgets.QVBoxLayout(central_widget)
    icon_layout = QtWidgets.QHBoxLayout()
    icon_layout.addStretch(1)

    self.eye = ClickableLabel()
    self.eye.setPixmap(QtGui.QPixmap("ui/images/show_password.png"))
    self.eye.setScaledContents(True)
    self.eye.setFixedSize(30, 30)
    self.eye.move(370, 10)
    icon_layout.addWidget(self.eye)

    self.file_password = ClickableLabel()
    self.file_password.setPixmap(QtGui.QPixmap("ui/images/file_password.png"))
    self.file_password.setScaledContents(True)
    self.file_password.setFixedSize(30, 30)
    self.file_password.move(330, 10)
    icon_layout.addWidget(self.file_password)

    layout.addLayout(icon_layout)

    password_layout = QtWidgets.QHBoxLayout()
    password_layout.addSpacing(5)
    self.password_line = QtWidgets.QLineEdit()
    self.password_line.setPlaceholderText("password")
    self.password_line.setStyleSheet("border: none;")
    self.password_line.setFixedSize(370, 40)
    password_layout.addWidget(self.password_line)
    layout.addLayout(password_layout)

    confirm_password_layout = QtWidgets.QHBoxLayout()
    confirm_password_layout.addSpacing(5)
    self.salt_line = QtWidgets.QLineEdit()
    self.salt_line.setStyleSheet("border: none;")
    self.salt_line.setFixedSize(370, 40)
    confirm_password_layout.addWidget(self.salt_line)
    if salt == "salt":
        self.salt_line.setPlaceholderText("salt")
        self.salt_line.setEnabled(True)
    else:
        self.salt_line.setEnabled(False)

    layout.addLayout(confirm_password_layout)

    button_layout = QtWidgets.QHBoxLayout()
    button_layout.addStretch(10)

    self.push_button_back = QtWidgets.QPushButton("Назад")
    self.push_button_back.setFixedSize(141, 51)
    button_layout.addWidget(self.push_button_back)
    self.push_button_back.setStyleSheet(root.find(".//text[@id='style_push_button_main']").text.strip())
    self.push_button_back.clicked.connect(self.password_window.close)

    button_layout.addSpacing(83)

    self.push_button_submit = QtWidgets.QPushButton("Далі")
    self.push_button_submit.setFixedSize(141, 51)
    button_layout.addWidget(self.push_button_submit)
    self.push_button_submit.setStyleSheet(root.find(".//text[@id='style_push_button_start_frag_NA']").text.strip())
    self.push_button_submit.setEnabled(False)
    button_layout.addStretch(10)

    layout.addLayout(button_layout)
    self.password_line.setEchoMode(QtWidgets.QLineEdit.Password)

    self.eye.clicked.connect(lambda: toggle_password_visibility(self))
    self.file_password.clicked.connect(lambda: password_in_file(self))

    self.password_line.textChanged.connect(lambda: check_password_match(self))
    self.salt_line.textChanged.connect(lambda: check_password_match(self))
    self.push_button_submit.clicked.connect(lambda: submit_password(self, start_decryption))
    self.password_window.show()


def submit_password(self, start_decryption):
    start_decryption(self.password_line.text(), self.salt_line.text())
    self.password_window.close()


def password_in_file(self):
    pass_file, bool_info = select_pass_file()
    if bool_info:
        self.password_line.setText(pass_file)


def toggle_password_visibility(self):
    current_mode = self.password_line.echoMode()
    if current_mode == QtWidgets.QLineEdit.Password:
        self.password_line.setEchoMode(QtWidgets.QLineEdit.Normal)
    else:
        self.password_line.setEchoMode(QtWidgets.QLineEdit.Password)


def check_password_match(self):
    password = self.password_line.text()
    salt_value = self.salt_line.text()

    if self.salt == "salt":
        if password and salt_value:
            self.push_button_submit.setStyleSheet(root.find(".//text[@id='style_push_button_start_frag']").text.strip())
            self.push_button_submit.setEnabled(True)
        else:
            self.push_button_submit.setStyleSheet(
                root.find(".//text[@id='style_push_button_start_frag_NA']").text.strip())
            self.push_button_submit.setEnabled(False)
    else:
        if password:
            self.push_button_submit.setStyleSheet(root.find(".//text[@id='style_push_button_start_frag']").text.strip())
            self.push_button_submit.setEnabled(True)
        else:
            self.push_button_submit.setStyleSheet(
                root.find(".//text[@id='style_push_button_start_frag_NA']").text.strip())
            self.push_button_submit.setEnabled(False)
