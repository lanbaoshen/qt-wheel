import pytest

from PySide6 import QtWidgets


@pytest.fixture(scope='session', autouse=True)
def app():
    app = app if (app := QtWidgets.QApplication.instance()) else QtWidgets.QApplication()
    yield app
    app.quit()
    del app
