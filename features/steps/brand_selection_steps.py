from behave import *
from tests.test_brand_selection import TestBrandSelection
from utilities.config_reader import ConfigReader

@given(u'I am on the Brand Selection page')
def step_impl(context):
    configobj = ConfigReader()
    url = configobj.get_url()
    context.driver.get(url)
    context.brand_selection = TestBrandSelection(context.driver)

@when(u'I scroll to Browse By section')
def step_impl(context):
    context.brand_selection.scroll_to_browse_by()

@when(u'I click on Oral Care')
def step_impl(context):
    context.brand_selection.click_oral_care()

@when(u'I click on Brands filter')
def step_impl(context):
    context.brand_selection.select_brand()

@when(u'I select Colgate brand')
def step_impl(context):
    context.brand_selection.select_colgate()

@when(u'I add the first product to the cart')
def step_impl(context):
    context.brand_selection.add_product()

@when(u'I select the first product')
def step_impl(context):
    context.brand_selection.select_first_product()

@when(u'I scroll to Available Offers')
def step_impl(context):
    context.brand_selection.scroll_to_offers()

@then(u'I verify the Available Offers section')
def step_impl(context):
    context.brand_selection.verify_offers()
