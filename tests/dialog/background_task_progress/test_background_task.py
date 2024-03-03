import time


from PySide6.QtCore import QThreadPool
from components.dialog.background_task_progress import BackgroundTask


def test_background_task():
    def update_temp():
        time.sleep(0.1)
        temp.append(1)

    temp = []

    thread_pool = QThreadPool.globalInstance()
    background_task = BackgroundTask(target=update_temp, callback=update_temp)
    thread_pool.start(background_task)

    assert temp == []

    time.sleep(0.3)
    assert temp == [1, 1]
