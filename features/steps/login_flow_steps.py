from behave import *
from tests.test_login_flow import TestLoginFlow
from locators.login_page_locators import LoginPageLocators
from utilities.config_reader import ConfigReader

@given(u'I am on the Login page')
def step_impl(context):
    configobj = ConfigReader()
    url = configobj.get_url()
    context.driver.get(url)
    context.login_flow = TestLoginFlow(context.driver)

@when(u'I click on the login button')
def step_impl(context):
    context.login_flow.click_login()

@when(u'I click the phone number input section')
def step_impl(context):
    context.login_flow.click_phone_number_div()

@when(u'I enter the phone number "{phone_number}"')
def step_impl(context, phone_number):
    context.login_flow.helper.send_keys(LoginPageLocators.phone_number_input, phone_number)

@when(u'I click the submit button')
def step_impl(context):
    context.login_flow.click_submit_button()

@when(u'I enter the OTP "{otp}"')
def step_impl(context, otp):
    context.login_flow.enter_otp_digits(otp)

@then(u'I click the final submit button')
def step_impl(context):
    context.login_flow.final_submit()
