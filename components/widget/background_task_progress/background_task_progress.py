from PySide6 import QtWidgets
from PySide6.QtCore import QThreadPool

from .._base import Base
from .background_task import BackgroundTask


class BackgroundTaskProgress(Base):
    def __init__(self, parent=None, *, tasks: list[BackgroundTask]):
        if not tasks:
            raise ValueError('tasks should not be empty')
        self.tasks = tasks

        self._thread_pool = QThreadPool.globalInstance()

        super().__init__(parent)

    def _initialize(self):
        self.progress_bar = QtWidgets.QProgressBar()

        self.progress_label = QtWidgets.QLabel()

    def _layout(self) -> QtWidgets.QGridLayout:
        layout = QtWidgets.QGridLayout()

        self.progress_bar.setRange(-1, len(self.tasks) - 1)
        layout.addWidget(self.progress_bar, 0, 0)

        self.progress_label.setText(self._progress(0))
        layout.addWidget(self.progress_label, 0, 1)

        return layout

    def _progress(self, cur: int | str) -> str:
        return f'{cur}/{len(self.tasks)}'

    def _update_progress(self):
        cur = self.progress_bar.value()
        self.progress_bar.setValue(cur + 1)
        self.progress_label.setText(self._progress(cur + 2))

    def start(self):
        for task in self.tasks:
            task.progress_signal.end.connect(self._update_progress)
            self._thread_pool.start(task)
        self.show()
