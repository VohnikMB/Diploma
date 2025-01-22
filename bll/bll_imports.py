"""Файл для імпортування спільних елементів bll"""

from xml.etree import ElementTree
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout,
                             QStackedWidget, QHBoxLayout, QLabel, QPushButton, QDesktopWidget, QFileDialog)
from PyQt5.QtGui import QFont, QIcon
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtCore, QtWidgets, QtGui
import sys
import os

tree = ElementTree.parse('ui/texts.xml')
root = tree.getroot()


class ClickableLabel(QLabel):
    clicked = QtCore.pyqtSignal()

    def mousePressEvent(self, event):
        self.clicked.emit()
