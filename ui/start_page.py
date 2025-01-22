from ui.imports_ui import *
from bll.selecter.select_files import *


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

    self.setting = QLabel(self.central_widget)
    self.setting.setGeometry(QtCore.QRect(875, 10, 41, 41))
    self.setting.setStyleSheet("image: url(ui/images/setting.png);")
    self.setting.setText("")
    self.setting.setObjectName("setting")

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
