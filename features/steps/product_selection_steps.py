from behave import *
from tests.test_product_selection import TestProductSelection
from utilities.config_reader import ConfigReader

@given(u'I am on the Product Selection page')
def step_impl(context):
    configobj = ConfigReader()
    url = configobj.get_url()
    context.driver.get(url)
    context.product_selection = TestProductSelection(context.driver)

@when(u'I click on the Offers section')
def step_impl(context):
    context.product_selection.click_offers()

@when(u'I scroll to the product section')
def step_impl(context):
    context.product_selection.scroll_to_section()

@when(u'I select Pampers product')
def step_impl(context):
    context.product_selection.select_pampers()

@when(u'I add the product to the cart')
def step_impl(context):
    context.product_selection.add_to_cart()

@when(u'I click on the cart icon')
def step_impl(context):
    context.product_selection.view_cart()

@then(u'I verify the cart page')
def step_impl(context):
    context.product_selection.verify_cart()
