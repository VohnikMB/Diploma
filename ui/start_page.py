from ui.imports_ui import *
from bll.selecter.select_files import open_file_dialog

"""
setup_ui.py. Файл, що містить функцію для створення графічного інтерфейсу головної сторінки програми.

Елементи Qt:
    - ClickableLabel:
        - self.de_frag: Іконка для переходу до сторінки дешифрування.
        - self.frag: Іконка для переходу до сторінки фрагментації.
        - self.info: Іконка для відкриття інформаційного вікна.
        - self.language: Іконка зміни мови.
    - QLabel:
        - self.text_frag: Текстовий підпис для сторінки фрагментації.
        - self.text_deFrag: Текстовий підпис для сторінки дешифрування.

Функції:
    - setup_ui: Налаштовує головну сторінку інтерфейсу PyQt5 з інтерактивними елементами.
    - de_cript_page: Відкриває діалог вибору файлів для дешифрування та перемикає сторінку.
    - self.frag.clicked: Переходить до сторінки фрагментації.
    - self.info.clicked: Відкриває інформаційне вікно.
"""


def setup_ui(self, page):

    font = QtGui.QFont()
    font.setFamily("Ravie")
    font.setPointSize(16)
    font.setBold(False)
    font.setWeight(50)
    font.setStrikeOut(False)
    font.setKerning(True)

    page.resize(960, 660)
    self.central_widget = QtWidgets.QWidget(page)

    self.de_frag = ClickableLabel(self.central_widget)
    self.de_frag.setGeometry(QtCore.QRect(190, 210, 221, 201))
    self.de_frag.setStyleSheet("image: url(ui/images/deFrag.png);")

    self.de_frag.setText("")
    self.de_frag.setObjectName("deFrag")

    self.frag = ClickableLabel(self.central_widget)
    self.frag.setGeometry(QtCore.QRect(540, 210, 221, 201))
    self.frag.setStyleSheet("image: url(ui/images/frag.png);")
    self.frag.setText("")
    self.frag.setObjectName("frag")

    self.language = ClickableLabel(self.central_widget)
    self.language.setGeometry(QtCore.QRect(875, 10, 41, 41))
    self.language.setStyleSheet("image: url(ui/images/setting.png);")
    self.language.setText("")
    self.language.setObjectName("setting")

    self.info = ClickableLabel(self.central_widget)
    self.info.setGeometry(QtCore.QRect(870, 590, 41, 41))
    self.info.setStyleSheet("image: url(ui/images/info.png);")
    self.info.setText("")
    self.info.setObjectName("info")

    self.text_frag = QLabel(self.central_widget)
    self.text_frag.setGeometry(QtCore.QRect(540, 180, 221, 31))

    self.text_frag.setFont(font)
    self.text_frag.setLayoutDirection(QtCore.Qt.LeftToRight)

    self.text_deFrag = QLabel(self.central_widget)
    self.text_deFrag.setGeometry(QtCore.QRect(190, 180, 221, 31))
    self.text_deFrag.setFont(font)
    self.text_deFrag.setLayoutDirection(QtCore.Qt.LeftToRight)

    self.de_frag.clicked.connect(lambda: de_cript_page())

    self.frag.clicked.connect(self.parent.show_frag_page)

    self.info.clicked.connect(self.open_info_widget)

    fragment = root.find(".//text[@id='deFrag']")
    self.text_deFrag.setText(fragment.text.strip())
    fragment = root.find(".//text[@id='frag']")
    self.text_frag.setText(fragment.text.strip())

    QtCore.QMetaObject.connectSlotsByName(page)

    def de_cript_page():
        files, m_bool = open_file_dialog()
        if m_bool:
            self.parent.show_de_frag_page(files)
