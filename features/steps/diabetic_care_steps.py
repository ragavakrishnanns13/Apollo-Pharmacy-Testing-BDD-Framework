from behave import *
from tests.test_diabetic_care import TestDiabeticCare
from utilities.config_reader import ConfigReader

@given(u'I am on the Diabetic Care page')
def step_impl(context):
    configobj = ConfigReader()
    url = configobj.get_url()
    context.driver.get(url)
    context.diabetic_care = TestDiabeticCare(context.driver)

@when(u'I scroll to the Health section')
def step_impl(context):
    context.diabetic_care.scroll_to_health()

@when(u'I click on Diabetic Care')
def step_impl(context):
    context.diabetic_care.click_diabetic_care()

@when(u'I select the first diabetic product')
def step_impl(context):
    context.diabetic_care.select_first_product()

@when(u'I click on Login')
def step_impl(context):
    context.diabetic_care.click_login()

@when(u'I enter primary phone number "{phone_number}"')
def step_impl(context, phone_number):
    context.diabetic_care.enter_phone_number(phone_number)

