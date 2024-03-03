import time


from PySide6.QtCore import QThreadPool
from components.dialog.task_progress import Task


def test_background_task():
    def update_temp():
        time.sleep(0.1)
        temp.append(1)

    temp = []

    thread_pool = QThreadPool.globalInstance()
    background_task = Task(target=update_temp)
    thread_pool.start(background_task)

    assert temp == []

    time.sleep(0.2)
    assert temp == [1]