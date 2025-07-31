from behave import *
from tests.test_apollo_products import TestApolloProducts
from utilities.config_reader import ConfigReader

@given(u'I am on the Apollo Pharmacy homepage')
def step_impl(context):
    configobj = ConfigReader()
    url = configobj.get_url()
    context.driver.get(url)
    context.apollo_products = TestApolloProducts(context.driver)

@when(u'I hover over Apollo Products')
def step_impl(context):
    context.apollo_products.hover_apollo_products()

@when(u'I select ORS Drinks')
def step_impl(context):
    context.apollo_products.select_ors_drinks()

@when(u'I sort products by price')
def step_impl(context):
    context.apollo_products.sort_by_price()

@when(u'I add a product to cart')
def step_impl(context):
    context.apollo_products.add_product()

@when(u'I click on the view the cart option')
def step_impl(context):
    context.apollo_products.view_cart()

@when(u'I change the quantity to 5')
def step_impl(context):
    context.apollo_products.change_quantity()

@when(u'I proceed to checkout')
def step_impl(context):
    context.apollo_products.proceed_to_checkout()
