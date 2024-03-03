from components.widget import Param
from components.widget.param import settings


def test_params():
    param_widget = Param()
    assert param_widget.params.foo == param_widget.foo_line_edit.text()


def test_settings():
    param_widget = Param()
    param_widget._save_settings()
    assert settings.value(param_widget.FOO) == param_widget.foo_line_edit.text()
