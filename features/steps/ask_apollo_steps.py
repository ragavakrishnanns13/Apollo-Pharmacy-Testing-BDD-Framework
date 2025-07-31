from behave import *
from tests.test_ask_apollo import TestAskApollo
from utilities.config_reader import ConfigReader

@given(u'I am on the Ask Apollo homepage')
def step_impl(context):
    configobj = ConfigReader()
    url = configobj.get_url()
    context.driver.get(url)
    context.ask_apollo = TestAskApollo(context.driver)

@when(u'I scroll and click the banner')
def step_impl(context):
    context.ask_apollo.scroll_and_click_banner()

@when(u'I click on doctor')
def step_impl(context):
    context.ask_apollo.click_doctor()

@when(u'I select the first option')
def step_impl(context):
    context.ask_apollo.select_first_option()

@when(u'I scroll and click Book Now')
def step_impl(context):
    context.ask_apollo.scroll_and_book()

@when(u'I click on Consult Online')
def step_impl(context):
    context.ask_apollo.consult_online()
