from PySide6 import QtWidgets


class SwitchLockedRadioButton(QtWidgets.QRadioButton):
    UNLOCK = 'Unlock'
    LOCK = 'Lock'

    def __init__(
        self, parent=None,
        *,
        locked_default: bool = True,
        effect_group: list[QtWidgets.QLineEdit | QtWidgets.QTextEdit] = None
    ):
        super().__init__(parent)
        self.setObjectName(self.__class__.__name__)

        self.effect_group = effect_group

        self._init_status(locked_default)

        self.clicked.connect(self._lock_and_unlock)

    def _init_status(self, locked_default: bool = True):
        self.setChecked(locked_default)

        if self.effect_group:
            for widget in self.effect_group:
                widget.setReadOnly(locked_default)

        self.setText(self.UNLOCK if locked_default else self.LOCK)

    def _lock_and_unlock(self):
        if self.effect_group:
            for widget in self.effect_group:
                widget.setReadOnly(self.isChecked())

        self.setText(self.UNLOCK if self.isChecked() else self.LOCK)
