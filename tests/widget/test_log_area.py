from components.widget import LogArea


def test_log():
    log_area = LogArea()
    log_area.log('test')
    assert log_area.log_text_edit.toPlainText().endswith('[INFO] test')


def test_clear_log():
    log_area = LogArea()
    log_area.log('test')
    log_area.clear_push_button.click()
    assert log_area.log_text_edit.toPlainText() == ''
