from behave import *
from tests.test_search_flow import TestSearchFlow
from utilities.config_reader import ConfigReader

@given(u'I am on the Search page')
def step_impl(context):
    configobj = ConfigReader()
    url = configobj.get_url()
    context.driver.get(url)
    context.search_flow = TestSearchFlow(context.driver)

@when(u'I search for the product "{product_name}"')
def step_impl(context, product_name):
    context.search_flow.search_product(product_name)

@when(u'I select the first product from results')
def step_impl(context):
    context.search_flow.select_product()

@when(u'I change the product variant')
def step_impl(context):
    context.search_flow.change_variant()

@when(u'I scroll and add the product to cart')
def step_impl(context):
    context.search_flow.scroll_and_add_to_cart()

@when(u'I view the cart')
def step_impl(context):
    context.search_flow.view_cart()

@then(u'I scroll to Last Minute Buys section')
def step_impl(context):
    context.search_flow.scroll_last_minute_buys()
