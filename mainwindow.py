import random

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QRadioButton, QLabel, QPushButton, QMenu, QMessageBox


class MainWindow(QWidget):
    def __init__(self, words):
        super().__init__()
        self.words = words
        self.current_level = None
        # Layout oluştur
        self.layout = QVBoxLayout()

        # Zorluk seviyesi butonlarını ekle
        self.level_layout = QHBoxLayout()
        self.radio_easy = QRadioButton("Easy")
        self.radio_medium = QRadioButton("Medium")
        self.radio_hard = QRadioButton("Hard")
        self.level_layout.addWidget(self.radio_easy)
        self.level_layout.addWidget(self.radio_medium)
        self.level_layout.addWidget(self.radio_hard)

        # Zorluk seviyesi radio butonlarını bir fonksiyona bağla
        self.radio_easy.toggled.connect(lambda: self.set_level("easy"))
        self.radio_medium.toggled.connect(lambda: self.set_level("medium"))
        self.radio_hard.toggled.connect(lambda: self.set_level("hard"))

        # Level Selection'ı Main Layout'a ekle
        self.layout.addLayout(self.level_layout)

        # word label oluştur ve layouta ekle
        self.label_word = QLabel()
        self.label_word.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.label_word)

        # meaning label oluştur ve layouta ekle
        self.label_meaning = QLabel()
        self.label_meaning.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.label_meaning)

        # "Show Meaning" butonu oluştur ve layouta ekle
        self.button_show_meaning = QPushButton("Show Meaning")
        self.button_show_meaning.clicked.connect(self.show_meaning)
        self.layout.addWidget(self.button_show_meaning)

        # "Next Word" butonu oluştur ve layouta ekle
        self.button_next = QPushButton("Next Word")
        self.button_next.clicked.connect(self.show_random_word)
        self.layout.addWidget(self.button_next)

        # Bir menü oluştur
        self.menu = QMenu()
        self.menu_insert_word = QAction("Insert Word", self)
        self.menu.addAction(self.menu_insert_word)
        self.menu_insert_word.triggered.connect(self.insert_word_dialog)

        # Menu butonu oluştur ve layouta ekle
        self.button_menu = QPushButton('Menu')
        self.button_menu.setMenu(self.menu)
        self.layout.addWidget(self.button_menu)

        self.setLayout(self.layout)

        self.show_random_word()

        self.setup_styles()

    def set_level(self, level):
        """Sets the current difficulty level of the words."""
        self.current_level = level
        self.show_random_word()

    def show_random_word(self):
        """Shows a random word from the selected level"""
        if self.current_level:
            level_words = [word for word in self.words if word.level == self.current_level]
            if level_words:
                self.word = random.choice(level_words)
                self.label_word.setText(self.word.word)
                self.label_meaning.clear()
            else:
                QMessageBox.warning(self, "Warning", f"No word found for level: {self.current_level}")
        else:
            QMessageBox.warning(self, "Warning", "Please select a difficulty level")

    def show_meaning(self):
        """Displays the meaning of the current word"""
        if hasattr(self, 'word'):
            self.label_meaning.setText(self.word.meaning)
        else:
            QMessageBox.warning(self, "Warning", "No word to show meaning.")

    def setup_styles(self):
        """Defines the styles for the buttons and labels"""
        self.label_word.setStyleSheet("QLabel { color: blue; font-size: 30px; }")
        self.label_meaning.setStyleSheet("QLabel { color: green; font-size: 20px; }")

    def insert_word_dialog(self):
        pass






