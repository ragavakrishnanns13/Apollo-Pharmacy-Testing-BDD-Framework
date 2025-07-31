from behave import *
from tests.test_location_selection import TestLocationSelection
from utilities.config_reader import ConfigReader

@given(u'I am on the Location Selection page')
def step_impl(context):
    configobj = ConfigReader()
    url = configobj.get_url()
    context.driver.get(url)
    context.location_selection = TestLocationSelection(context.driver)

@when(u'I click on the address section')
def step_impl(context):
    context.location_selection.click_address()

@when(u'I choose a different location')
def step_impl(context):
    context.location_selection.choose_different_location()

@when(u'I enter the location "{location}"')
def step_impl(context, location):
    context.location_selection.enter_location(location)

@when(u'I select Hosur from suggestions')
def step_impl(context):
    context.location_selection.select_hosur()

@when(u'I click on Pharmacy Near Me')
def step_impl(context):
    context.location_selection.click_pharmacy_near_me()

@then(u'I enter full screen mode')
def step_impl(context):
    context.location_selection.enter_full_screen()
