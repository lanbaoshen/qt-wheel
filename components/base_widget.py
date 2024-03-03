from PySide6 import QtWidgets


class BaseWidget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName(self.__class__.__name__)

        self._initialize()
        self._connect()
        self.setLayout(self._layout())

    def _initialize(self):
        """
        Initialize the internal elements of the widget
        """
        ...

    def _connect(self):
        """
        Connect the signals and slots of internal elements
        """
        ...

    def _layout(self) -> QtWidgets.QGridLayout:
        """
        Return the layout of the widget

        Returns:
            QtWidgets.QGridLayout: The layout of the widget
        """
        ...
