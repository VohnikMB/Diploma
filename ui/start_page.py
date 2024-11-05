from ui.imports_ui import *


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

    self.frag = ClickableLabel(self.central_widget)
    self.frag.setGeometry(QtCore.QRect(190, 210, 221, 201))
    self.frag.setStyleSheet("image: url(ui/images/deFrag.png);")

    self.frag.setText("")
    self.frag.setObjectName("deFrag")

    self.defrag = ClickableLabel(self.central_widget)
    self.defrag.setGeometry(QtCore.QRect(540, 210, 221, 201))
    self.defrag.setStyleSheet("image: url(ui/images/frag.png);")
    self.defrag.setText("")
    self.defrag.setObjectName("frag")

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

    self.frag.clicked.connect(self.parent.show_de_frag_page)
    self.defrag.clicked.connect(self.parent.show_frag_page)

    self.info.clicked.connect(self.open_info_widget)

    fragment = root.find(".//text[@id='deFrag']")
    self.text_deFrag.setText(fragment.text.strip())
    fragment = root.find(".//text[@id='frag']")
    self.text_frag.setText(fragment.text.strip())

    QtCore.QMetaObject.connectSlotsByName(page)
