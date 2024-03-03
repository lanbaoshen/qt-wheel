import time

from components.dialog.background_task_progress import BackgroundTask, BackgroundTaskProgress


def test_background_task_progress():
    def foo():
        time.sleep(0.1)
        print('foo')

    background_tasks = [BackgroundTask(target=foo) for _ in range(5)]
    background_task_progress = BackgroundTaskProgress(tasks=background_tasks)
    background_task_progress.start()

    assert background_task_progress.progress.value() == -1

    time.sleep(3)
    assert background_task_progress.progress.value() == 4
