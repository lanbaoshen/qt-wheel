from PySide6 import QtWidgets
from PySide6.QtCore import QThreadPool

from .task import Task


class TaskProgress(QtWidgets.QProgressDialog):
    def __init__(self, parent=None, *, tasks: list[Task]):
        if not tasks:
            raise ValueError('tasks should not be empty')
        super().__init__(parent)

        self.tasks = tasks
        self.setRange(-1, len(self.tasks) - 1)

        self._thread_pool = QThreadPool.globalInstance()

    def _update_progress(self):
        self.setValue(self.value() + 1)

    def start(self):
        for task in self.tasks:
            task.progress_signal.end.connect(self._update_progress)
            self._thread_pool.start(task)
        self.exec()
