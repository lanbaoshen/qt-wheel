import time

from components.widget.background_task_progress import BackgroundTask, BackgroundTaskProgress


def test_task_progress():
    tasks = [BackgroundTask(target=object) for _ in range(20)]
    task_progress = BackgroundTaskProgress(tasks=tasks)

    assert task_progress.progress_bar.maximum() == 19
