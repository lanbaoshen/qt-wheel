from PySide6 import QtWidgets
from PySide6.QtCore import QSettings
from pydantic import BaseModel

from ..base_widget import BaseWidget


settings = QSettings('settings.ini', QSettings.IniFormat)


class _Params(BaseModel):
    foo: str


class ParamWidget(BaseWidget):
    # Settings
    FOO = 'foo'

    def _initialize(self):
        self.foo_label = QtWidgets.QLabel('Foo:')

        self.foo_line_edit = QtWidgets.QLineEdit(settings.value(self.FOO))

    def _layout(self) -> QtWidgets.QGridLayout:
        layout = QtWidgets.QGridLayout()

        layout.addWidget(self.foo_label, 0, 0)
        layout.addWidget(self.foo_line_edit, 0, 1)

        return layout

    def _save_settings(self):
        params = self.params
        settings.setValue(self.FOO, params.foo)

    @property
    def params(self) -> _Params:
        return _Params(
            foo=self.foo_line_edit.text(),
        )
