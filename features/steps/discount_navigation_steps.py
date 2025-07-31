from behave import *
from tests.test_discount_navigation import TestDiscountNavigation
from utilities.config_reader import ConfigReader

@given(u'I am on the Discount page')
def step_impl(context):
    configobj = ConfigReader()
    url = configobj.get_url()
    context.driver.get(url)
    context.discount_nav = TestDiscountNavigation(context.driver)

@when(u'I click on Discount section')
def step_impl(context):
    context.discount_nav.click_discount()

@when(u'I scroll to Category section')
def step_impl(context):
    context.discount_nav.scroll_to_category()

@when(u'I click on Home category')
def step_impl(context):
    context.discount_nav.click_home()

@when(u'I scroll to Add button section')
def step_impl(context):
    context.discount_nav.scroll_to_add()

@when(u'I click Add buttons with stock "{stock}"')
def step_impl(context, stock):
    stock_bool = stock.lower() == "true"
    context.discount_nav.click_add_buttons(stock_bool)
