from xml.etree import ElementTree
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout,
                             QStackedWidget, QHBoxLayout, QLabel, QPushButton, QDesktopWidget, QFileDialog)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtCore, QtWidgets, QtGui
import webbrowser
import sys
import os


tree = ElementTree.parse('ui/texts.xml')
root = tree.getroot()


# Utiles qt
def centering(widget):
    screen_geometry = QDesktopWidget().availableGeometry()
    window_geometry = widget.frameGeometry()
    center_point = screen_geometry.center()
    window_geometry.moveCenter(center_point)
    widget.move(window_geometry.topLeft())


class ClickableLabel(QLabel):
    clicked = QtCore.pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()
