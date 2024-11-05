import sys
from ui.imports_ui import *
from ui.page_manager import PageManager


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.frag_page = None
        self.stacked_widget = None
        self.init_ui()

    def init_ui(self):
        self.stacked_widget = QStackedWidget()
        self.page_manager = PageManager(self)
        self.create_and_add_pages()

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.stacked_widget)
        self.setLayout(main_layout)

        self.setWindowTitle('Масняк Б. ІТ-31сп Дипломна робота')
        self.setFixedSize(960, 660)
        centering(self)
        self.show()

    def create_and_add_pages(self):
        # Create pages
        self.start_page = self.page_manager.start_page()
        self.page2 = self.page_manager.createPage2()
        self.frag_page = self.page_manager.create_frag_page()

        # Add pages to the stacked widget
        self.stacked_widget.addWidget(self.start_page)
        self.stacked_widget.addWidget(self.page2)
        self.stacked_widget.addWidget(self.frag_page)

    def show_start_page(self):
        self.page_manager.show_start_page()

    def show_de_frag_page(self):
        self.page_manager.show_de_frag_page()

    def show_frag_page(self):
        self.page_manager.show_frag_page()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    sys.exit(app.exec_())
