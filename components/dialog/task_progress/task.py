from PySide6.QtCore import QRunnable, Signal, QObject


class ProgressSignal(QObject):
    end = Signal()


class Task(QRunnable):
    """
    Background Task for background task progress dialog,
    callback will be assigned by background task progress dialog
    """
    def __init__(self, *, target):
        super().__init__()
        self._target = target
        self.progress_signal = ProgressSignal()

    def run(self):
        try:
            self._target()
        finally:
            self.progress_signal.end.emit()
