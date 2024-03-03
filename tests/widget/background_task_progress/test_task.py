import time


from PySide6.QtCore import QThreadPool
from components.widget.background_task_progress import BackgroundTask


def test_task():
    def update_temp():
        time.sleep(0.1)
        temp.append(1)

    temp = []

    thread_pool = QThreadPool.globalInstance()
    task = BackgroundTask(target=update_temp)
    thread_pool.start(task)

    assert temp == []

    time.sleep(0.2)
    assert temp == [1]
