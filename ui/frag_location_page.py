from ui.imports_ui import *
from bll.save_files.divide_function import *


def create_frag_location_page(parent, slider, hash_type, data, file_name):
    page = QtWidgets.QWidget(parent)
    push_button_forward = QtWidgets.QPushButton(page)
    push_button_forward.setGeometry(QtCore.QRect(730, 560, 141, 51))
    push_button_forward.setObjectName("push_button_forward")
    push_button_forward.setText("Далі")

    push_button_back = QtWidgets.QPushButton(page)
    push_button_back.setGeometry(QtCore.QRect(130, 560, 141, 51))
    push_button_back.setObjectName("push_button_back")
    push_button_back.setText("Назад")
    push_button_back.clicked.connect(parent.show_frag_page)  # Navigate to the start page
    push_button_back.setStyleSheet(root.find(".//text[@id='style_push_button_main']").text.strip())

    data_divide = divide_data(data, slider)
    files_name = divide_files_name(slider, hash_type, file_name)

    location_fields = []
    for i in range(slider):
        location_field = QtWidgets.QLineEdit(page)
        location_field.setGeometry(QtCore.QRect(130, 40 + i * 60, 671, 41))
        location_field.setObjectName(f"locatio_{i}")
        location_field.setText(f"save/{files_name[i]}")
        location_fields.append(location_field)

    location_buttons = []
    for i in range(slider):
        location_button = ClickableLabel(page)
        location_button.setGeometry(QtCore.QRect(820, 30 + i * 60, 71, 61))
        location_button.setStyleSheet("image: url(ui/images/folder.png);")
        location_button.setObjectName(f"folder_{i}")
        location_buttons.append(location_button)

        location_button.clicked.connect(lambda: open_file_dialog(i))
        location_buttons.append(location_button)

    def open_file_dialog(index):
        """Функція для відкриття діалогу збереження окремого фрагменту."""
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_path, _ = QFileDialog.getSaveFileName(
            page,
            "Виберіть місце для збереження фрагменту",
            f"save/{files_name[index]}",
            "All Files (*)",
            options=options,
        )
        if file_path:
            location_fields[index].setText(file_path)
    return page
