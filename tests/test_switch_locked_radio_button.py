import pytest
from PySide6.QtWidgets import QLineEdit

from components import SwitchLockedRadioButton


def test_locked_default_true():
    line_edit = QLineEdit()
    switch_locked_radio_button = SwitchLockedRadioButton(effect_group=[line_edit])

    assert switch_locked_radio_button.isChecked() is True
    assert line_edit.isReadOnly() is True


def test_locked_default_false():
    line_edit = QLineEdit()
    switch_locked_radio_button = SwitchLockedRadioButton(locked_default=False, effect_group=[line_edit])

    assert switch_locked_radio_button.isChecked() is False
    assert line_edit.isReadOnly() is False


@pytest.mark.skipif(reason='When only running the radio button, checked can not change to unchecked by clicking')
def test_unlock():
    line_edit = QLineEdit()
    switch_locked_radio_button = SwitchLockedRadioButton(effect_group=[line_edit])
    switch_locked_radio_button.click()

    assert switch_locked_radio_button.isChecked() is False
    assert line_edit.isReadOnly() is False


def test_lock():
    line_edit = QLineEdit()
    switch_locked_radio_button = SwitchLockedRadioButton(locked_default=False, effect_group=[line_edit])
    switch_locked_radio_button.click()

    assert switch_locked_radio_button.isChecked() is True
    assert line_edit.isReadOnly() is True
