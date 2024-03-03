from PySide6.QtCore import QRunnable


class BackgroundTask(QRunnable):
    """
    Background Task for background task progress dialog,
    callback will be assigned by background task progress dialog
    """
    def __init__(self, *, target, callback=object):
        super().__init__()
        self._target, self._callback = target, callback

    def run(self):
        try:
            self._target()
        finally:
            self._callback()
