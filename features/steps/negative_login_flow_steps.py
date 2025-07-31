from behave import *
from tests.test_negative_login_flow import TestNegativeLoginFlow
from utilities.config_reader import ConfigReader

@given(u'I am on the Negative Login page')
def step_impl(context):
    configobj = ConfigReader()
    url = configobj.get_url()
    context.driver.get(url)
    context.negative_login = TestNegativeLoginFlow(context.driver)

@when(u'I open the page and click on the login button')
def step_impl(context):
    context.negative_login.click_login()

@when(u'I click the phone number input div')
def step_impl(context):
    context.negative_login.click_phone_number_div()

@when(u'I enter an invalid phone number "{phone_number}"')
def step_impl(context, phone_number):
    context.negative_login.enter_invalid_phone_number(phone_number)

@then(u'I verify the wrong number message')
def step_impl(context):
    context.negative_login.verify_wrong_number_message()

@then(u'I close the error pop-up')
def step_impl(context):
    context.negative_login.close_popup()

@then(u'I click the WhatsApp button')
def step_impl(context):
    context.negative_login.click_whatsapp()
