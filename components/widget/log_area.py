from datetime import datetime

from PySide6 import QtWidgets

from components.widget._base import Base


class LogArea(Base):
    def _initialize(self):
        self.log_text_edit = QtWidgets.QTextEdit()
        self.clear_push_button = QtWidgets.QPushButton('Clear')

    def _connect(self):
        self.clear_push_button.clicked.connect(self.log_text_edit.clear)

    def _layout(self) -> QtWidgets.QGridLayout:
        layout = QtWidgets.QGridLayout()
        layout.addWidget(self.clear_push_button, 0, 0)
        layout.addWidget(self.log_text_edit, 1, 0)
        return layout

    def log(self, msg: str, level: str = 'INFO'):
        self.log_text_edit.append(f'{str(datetime.now())} [{level}] {msg}')
