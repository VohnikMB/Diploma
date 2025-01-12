from bll.selecter.password import *


def open_password_form(self, callback):
    self.password_window = QtWidgets.QMainWindow()
    self.password_window.setWindowTitle('Enter Password')
    self.password_window.setFixedSize(420, 235)

    central_widget = QtWidgets.QWidget()
    self.password_window.setCentralWidget(central_widget)

    layout = QtWidgets.QVBoxLayout(central_widget)

    # Add icons at the top (eye and file_password icons)
    icon_layout = QtWidgets.QHBoxLayout()
    icon_layout.addStretch(1)  # Push icons to the right

    self.eye = ClickableLabel()
    self.eye.setPixmap(QtGui.QPixmap("ui/images/show_password.png"))
    self.eye.setScaledContents(True)
    self.eye.setFixedSize(30, 30)
    self.eye.move(370, 10)  # Adjusted position
    icon_layout.addWidget(self.eye)

    self.file_password = ClickableLabel()
    self.file_password.setPixmap(QtGui.QPixmap("ui/images/file_password.png"))
    self.file_password.setScaledContents(True)
    self.file_password.setFixedSize(30, 30)
    self.file_password.move(330, 10)  # Adjusted position
    icon_layout.addWidget(self.file_password)

    layout.addLayout(icon_layout)

    # Add the password line edit
    password_layout = QtWidgets.QHBoxLayout()  # Create a horizontal layout
    password_layout.addSpacing(5)  # Add spacing to push the line edit to the right
    self.password_line = QtWidgets.QLineEdit()
    self.password_line.setStyleSheet("border: none;")
    self.password_line.setFixedSize(370, 40)  # Adjusted size
    password_layout.addWidget(self.password_line)
    layout.addLayout(password_layout)  # Add this layout to the main vertical layout

    # Add the confirm password line edit
    confirm_password_layout = QtWidgets.QHBoxLayout()  # Create a new horizontal layout for spacing
    confirm_password_layout.addSpacing(5)  # Same spacing as above
    self.confirm_password_line = QtWidgets.QLineEdit()
    self.confirm_password_line.setStyleSheet("border: none;")
    self.confirm_password_line.setFixedSize(370, 40)  # Adjusted size
    confirm_password_layout.addWidget(self.confirm_password_line)
    layout.addLayout(confirm_password_layout)  # Add this layout to the main vertical layout

    # Add the buttons at the bottom
    button_layout = QtWidgets.QHBoxLayout()

    button_layout.addStretch(10)  # Add stretch to balance the spacing on both sides

    self.push_button_back = QtWidgets.QPushButton("Назад")
    self.push_button_back.setFixedSize(141, 51)
    button_layout.addWidget(self.push_button_back)
    self.push_button_back.setStyleSheet(root.find(".//text[@id='style_push_button_main']").text.strip())
    self.push_button_back.clicked.connect(self.password_window.close)

    button_layout.addSpacing(83)  # Spacing between buttons

    self.push_button_submit = QtWidgets.QPushButton("Далі")
    self.push_button_submit.setFixedSize(141, 51)
    button_layout.addWidget(self.push_button_submit)
    self.push_button_submit.setStyleSheet(root.find(".//text[@id='style_push_button_start_frag_NA']").text.strip())
    self.push_button_submit.setEnabled(False)
    button_layout.addStretch(10)  # Add stretch to balance the spacing on both sides

    layout.addLayout(button_layout)  # Add this layout to the main vertical layout
    self.password_line.setEchoMode(QtWidgets.QLineEdit.Password)
    self.confirm_password_line.setEchoMode(QtWidgets.QLineEdit.Password)
    self.eye.clicked.connect(lambda: toggle_password_visibility(self))
    self.file_password.clicked.connect(lambda: password_in_file(self))
    self.password_line.textChanged.connect(lambda: check_password_match(self))
    self.confirm_password_line.textChanged.connect(lambda: check_password_match(self))
    self.push_button_submit.clicked.connect(lambda: submit_password(self, callback))
    self.password_window.show()


def submit_password(self, callback):
    callback(self.password_line.text())  # Pass the password to the callback
    self.password_window.close()


def password_in_file(self):
    pass_file, bool_info = select_pass_file()
    if bool_info:
        self.password_line.setText(pass_file)
        self.confirm_password_line.setText(pass_file)


def toggle_password_visibility(self):
    current_mode = self.password_line.echoMode()
    if current_mode == QtWidgets.QLineEdit.Password:
        self.password_line.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.confirm_password_line.setEchoMode(QtWidgets.QLineEdit.Normal)
    else:
        self.password_line.setEchoMode(QtWidgets.QLineEdit.Password)
        self.confirm_password_line.setEchoMode(QtWidgets.QLineEdit.Password)


def check_password_match(self):
    password = self.password_line.text()
    confirm_password = self.confirm_password_line.text()
    if password == confirm_password:
        self.push_button_submit.setStyleSheet(root.find(".//text[@id='style_push_button_start_frag']").text.strip())
        self.push_button_submit.setEnabled(True)
    else:
        self.push_button_submit.setEnabled(False)
        self.push_button_submit.setStyleSheet(root.find(".//text[@id='style_push_button_start_frag_NA']").text.strip())
