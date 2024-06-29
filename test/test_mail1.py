import pytest


@pytest.fixture()#дія до тог як ми запустимо систему

def set_up():
    print('Вхід в систему')

def test_sending_mail1(set_up):# передаємо функцію для входа всистему
    print('Лист відправлено')

def test_sending_mail2(set_up):# передаємо функцію для входа всистему
    print('Лист відправлено')
