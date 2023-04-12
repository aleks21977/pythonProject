import time

import pytest
from selenium.webdriver.common.by import By
from faker import Faker
from helpers.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_fill_form(app):
    fake = Faker()

    app.open_home_page()

    full_name = fake.name()
    email = fake.email()
    cur_address = fake.address().replace('\n', '')
    per_address = fake.address().replace('\n', '')

    field_full_name = app.find_elements_by_xpath("//*[@placeholder='Full Name']")
    field_email = app.find_elements_by_xpath("//*[@placeholder='name@example.com']")
    field_cur_address = app.find_elements_by_xpath("//textarea[@id='currentAddress']")
    field_per_address = app.find_elements_by_xpath("//textarea[@id='permanentAddress']")

    field_full_name.send_keys(full_name)
    field_email.send_keys(email)
    field_cur_address.send_keys(cur_address)
    field_per_address.send_keys(per_address)

    button_submit = app.wd.find_element(By.ID, "submit")
    button_submit.click()

    text_full_name = app.get_element_text("//p[@id='name']")
    text_email = app.get_element_text("//p[@id='email']")
    text_cur_address = app.get_element_text("//p[@id='currentAddress']")
    text_per_address = app.get_element_text("//p[@id='permanentAddress']")

    assert text_full_name == ("Name:" + full_name)
    assert text_email == ("Email:" + email)
    assert text_cur_address == ("Current Address :" + cur_address)
    assert text_per_address == ("Permananet Address :" + per_address)


