from ui.imports_ui import *

from .frag_page import create_frag_page
from .start_page import setup_ui
from .info_widgets import open_info_widget


class PageManager:
    def __init__(self, parent):
        self.parent = parent

    def start_page(self):
        page = QWidget()
        setup_ui(self, page)
        return page

    def open_info_widget(self):
        open_info_widget(self)

    def createPage2(self):
        page = QWidget()
        layout = QVBoxLayout()

        label = QLabel('Це сторінка 2', self.parent)
        label.setFont(QFont('Times', 18, QFont.Bold))

        button_layout = QHBoxLayout()

        btn_to_page1 = QPushButton('Перейти на сторінку 1', self.parent)
        btn_to_page1.setFont(QFont('Arial', 12))
        btn_to_page1.setStyleSheet("QPushButton { font-size: 24px; }")
        btn_to_page1.setFixedSize(200, 60)
        button_layout.addWidget(btn_to_page1)
        btn_to_page1.clicked.connect(self.parent.show_start_page)

        btn_to_page3 = QPushButton('Перейти на сторінку 3', self.parent)
        btn_to_page3.setFont(QFont('Arial', 12))
        btn_to_page3.setStyleSheet("QPushButton { font-size: 24px; }")
        btn_to_page3.setFixedSize(200, 60)
        button_layout.addWidget(btn_to_page3)
        btn_to_page3.clicked.connect(self.parent.show_frag_page)

        layout.addWidget(label)
        layout.addLayout(button_layout)
        page.setLayout(layout)

        return page

    def create_frag_page(self):
        return create_frag_page(self.parent)

    def show_start_page(self):
        self.parent.stacked_widget.setCurrentIndex(0)

    def showPage2(self):
        self.parent.stacked_widget.setCurrentIndex(1)

    def show_frag_page(self):
        self.parent.stacked_widget.setCurrentIndex(2)
