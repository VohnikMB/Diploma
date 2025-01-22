from ui.imports_ui import *
from .frag_page import create_frag_page
from .start_page import setup_ui
from .info_widgets import open_info_widget
from .frag_location_page import create_frag_location_page
from .de_frag_location import create_de_frag_page

"""
Модуль PageManager. Відповідає за управління сторінками додатку. 

Клас:
    - PageManager: Керує створенням і навігацією сторінками.
Функції:
    - __init__: Ініціалізує PageManager батьківським віджетом.
    - start_page: Створює та повертає стартову сторінку.
    - open_info_widget: Відкриває інформаційне вікно як модальне.
    - create_de_frag_page: Створює сторінку дефрагментації.
    - create_frag_page: Створює сторінку фрагментації.
    - create_frag_location_page: Створює сторінку з адресами збереження розділених файлів.
    
    - show_start_page: Відображає стартову сторінку.
    - show_de_frag_page: Відображає сторінку дефрагментації.
    - show_frag_page: Відображає сторінку фрагментації.
    - show_frag_location_page: Відображає сторінку з адресами збереження розділених файлів.
"""


class PageManager:
    def __init__(self, parent):
        self.parent = parent
        self.current_frag_page = None
        self.current_frag_location_page = None
        self.current_de_frag_location_page = None

    def start_page(self):
        page = QWidget()
        setup_ui(self, page)
        return page

    def open_info_widget(self):
        open_info_widget(self)

    def create_de_frag_page(self, file_name):
        if self.current_de_frag_location_page:
            self.parent.stacked_widget.removeWidget(self.current_de_frag_location_page)
            self.current_de_frag_location_page.deleteLater()
        self.current_de_frag_location_page = create_de_frag_page(self.parent, file_name)
        self.parent.stacked_widget.addWidget(self.current_de_frag_location_page)
        return self.current_de_frag_location_page

    def create_frag_page(self):
        if self.current_frag_page:
            self.parent.stacked_widget.removeWidget(self.current_frag_page)
            self.current_frag_page.deleteLater()
        self.current_frag_page = create_frag_page(self.parent)
        self.parent.stacked_widget.addWidget(self.current_frag_page)
        return self.current_frag_page

    def create_frag_location_page(self, slider_value, hash_type, data, file_name):
        if self.current_frag_location_page:
            self.parent.stacked_widget.removeWidget(self.current_frag_location_page)
            self.current_frag_location_page.deleteLater()
        self.current_frag_location_page = create_frag_location_page(self.parent, slider_value, hash_type, data, file_name)
        self.parent.stacked_widget.addWidget(self.current_frag_location_page)
        return self.current_frag_location_page

    def show_start_page(self):
        self.parent.stacked_widget.setCurrentIndex(0)

    def show_de_frag_page(self, file_name):
        self.create_de_frag_page(file_name)
        self.parent.stacked_widget.setCurrentWidget(self.current_de_frag_location_page)

    def show_frag_page(self):
        self.parent.stacked_widget.setCurrentWidget(self.current_frag_page)

    def show_frag_location_page(self, slider_value, hash_type, data, file_name):
        self.create_frag_location_page(slider_value, hash_type, data, file_name)
        self.parent.stacked_widget.setCurrentWidget(self.current_frag_location_page)
