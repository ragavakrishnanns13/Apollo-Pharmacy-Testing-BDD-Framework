from behave import *
from tests.test_product_category import TestProductCategory
from utilities.config_reader import ConfigReader

@given(u'I am on the Product Category page')
def step_impl(context):
    configobj = ConfigReader()
    url = configobj.get_url()
    context.driver.get(url)
    context.product_category = TestProductCategory(context.driver)

@when(u'I scroll to the footer section')
def step_impl(context):
    context.product_category.scroll_to_footer()

@when(u'I click on the Formula link')
def step_impl(context):
    context.product_category.click_formula()

@when(u'I switch to the newly opened window')
def step_impl(context):
    context.product_category.switch_to_new_window()

@when(u'I hover over the Infant category')
def step_impl(context):
    context.product_category.hover_infant()

@when(u'I click on the Baby Food category')
def step_impl(context):
    context.product_category.click_baby_food()

@when(u'I scroll to the Read Section')
def step_impl(context):
    context.product_category.scroll_to_read_section()

@then(u'I click on View All')
def step_impl(context):
    context.product_category.click_view_all()
