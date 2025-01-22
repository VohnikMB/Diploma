from ui.imports_ui import *

"""
info_widget.py. Модуль, що містить функцію для створення та відображення інформаційного вікна програми.

Елементи Qt:
    - QMainWindow:
        - info_window: Головне вікно для відображення інформації.
    - QTextEdit:
        - textEdit: Віджет для відображення текстової інформації у форматі HTML.
    - QVBoxLayout:
        - layout: Основний вертикальний макет вмісту вікна.
    - QHBoxLayout:
        - icon_layout: Горизонтальний макет для іконок соціальних мереж.
    - ClickableLabel:
        - git: Іконка для переходу на GitHub.
        - linkedin: Іконка для переходу на LinkedIn.
Функції:
    - open_info_widget: Відображає інформаційне вікно з текстом і посиланнями на соціальні мережі.
    - open_webpage_git: Відкриває GitHub-профіль у веб-браузері.
    - open_webpage_link: Відкриває LinkedIn-профіль у веб-браузері.
"""


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
    webbrowser.open("https://github.com/VohnikMB/Diploma", new=0, autoraise=True)


def open_webpage_link():
    webbrowser.open("https://www.linkedin.com/in/vohnik/", new=0, autoraise=True)
