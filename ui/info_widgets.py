from ui.imports_ui import *


def open_info_widget(self):
    self.info_window = QtWidgets.QMainWindow()
    self.info_window.setWindowTitle('Info')
    self.info_window.setFixedSize(550, 520)

    central_widget = QtWidgets.QWidget()
    self.info_window.setCentralWidget(central_widget)

    layout = QtWidgets.QVBoxLayout(central_widget)
    spacer_top = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
    layout.addItem(spacer_top)

    self.textEdit = QtWidgets.QTextEdit()
    self.textEdit.setObjectName("textEdit")
    self.textEdit.setReadOnly(True)

    fragment = root.find(".//text[@id='info']")
    html_content = fragment.text.strip()
    self.textEdit.setHtml(html_content)

    layout.addWidget(self.textEdit)
    spacer = QtWidgets.QSpacerItem(20, 25, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
    layout.addItem(spacer)

    icon_layout = QtWidgets.QHBoxLayout()
    self.textEdit.setStyleSheet("border: none;")

    self.git = ClickableLabel()
    self.git.setPixmap(QtGui.QPixmap("ui/images/Git.png"))
    self.git.setScaledContents(True)
    self.git.setFixedSize(41, 41)
    icon_layout.addWidget(self.git)

    self.linkedin = ClickableLabel()
    self.linkedin.setPixmap(QtGui.QPixmap("ui/images/linkedin.png"))
    self.linkedin.setScaledContents(True)
    self.linkedin.setFixedSize(41, 41)
    icon_layout.addWidget(self.linkedin)

    layout.addLayout(icon_layout)
    self.git.clicked.connect(open_webpage_git)
    self.linkedin.clicked.connect(open_webpage_link)
    self.info_window.show()


def open_webpage_git():
    try:
        webbrowser.open("https://github.com/VohnikMB/Diploma", new=0, autoraise=True)
    except Exception as e:
        print(f"Error opening GitHub: {e}")


def open_webpage_link():
    try:
        webbrowser.open("https://www.linkedin.com/in/vohnik/", new=0, autoraise=True)
    except Exception as e:
        print(f"Error opening LinkedIn: {e}")
