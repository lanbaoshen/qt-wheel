from components import ParamWidget
from components.param_widget.param_widget import settings


def test_params():
    param_widget = ParamWidget()
    assert param_widget.params.foo == param_widget.foo_line_edit.text()


def test_settings():
    param_widget = ParamWidget()
    param_widget._save_settings()
    assert settings.value(param_widget.FOO) == param_widget.foo_line_edit.text()
