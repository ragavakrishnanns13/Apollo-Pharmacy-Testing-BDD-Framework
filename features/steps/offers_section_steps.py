from behave import *
from tests.test_offers_section import TestOffersSection
from utilities.config_reader import ConfigReader

@given(u'I am on the Offers page')
def step_impl(context):
    configobj = ConfigReader()
    url = configobj.get_url()
    context.driver.get(url)
    context.offers_section = TestOffersSection(context.driver)

@when(u'I click on the Offers icon')
def step_impl(context):
    context.offers_section.click_offers()

@when(u'I scroll to the product section of the home page')
def step_impl(context):
    context.offers_section.scroll_to_section()

@then(u'I verify the Deals by Category section')
def step_impl(context):
    context.offers_section.verify_deals_by_category()

@when(u'I select Home Essentials category')
def step_impl(context):
    context.offers_section.select_home_essentials()

@when(u'I sort products by price from low to high')
def step_impl(context):
    context.offers_section.sort_by_price()

@when(u'I add a product to the cart')
def step_impl(context):
    context.offers_section.add_product()

@then(u'I view the cart')
def step_impl(context):
    context.offers_section.view_cart()
