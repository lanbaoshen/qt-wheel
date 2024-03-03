import time

from components.dialog.task_progress import Task, TaskProgress


def test_task_progress():
    tasks = [Task(target=object) for _ in range(20)]
    task_progress = TaskProgress(tasks=tasks)

    assert task_progress.maximum() == 19
