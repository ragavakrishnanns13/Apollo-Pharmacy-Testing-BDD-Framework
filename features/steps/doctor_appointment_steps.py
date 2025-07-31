from behave import *
from tests.test_doctor_appointment import TestDoctorAppointment
from utilities.config_reader import ConfigReader

@given(u'I am on the Doctor Appointment page')
def step_impl(context):
    configobj = ConfigReader()
    url = configobj.get_url()
    context.driver.get(url)
    context.doctor_appointment = TestDoctorAppointment(context.driver)

@when(u'I click on Doctor Appointment section')
def step_impl(context):
    context.doctor_appointment.click_doctor_appointment()

@when(u'I select Neurology specialty')
def step_impl(context):
    context.doctor_appointment.select_neurology()

@when(u'I sort doctors by Relevance')
def step_impl(context):
    context.doctor_appointment.sort_by_relevance()

@when(u'I sort doctors by Experience')
def step_impl(context):
    context.doctor_appointment.sort_by_experience()

@when(u'I click on Consult')
def step_impl(context):
    context.doctor_appointment.click_consult()

@when(u'I click on Continue')
def step_impl(context):
    context.doctor_appointment.click_continue()

@when(u'I enter phone number "{phone_number}"')
def step_impl(context, phone_number):
    context.doctor_appointment.enter_phone_number(phone_number)

@then(u'I verify the error message for invalid phone number')
def step_impl(context):
    context.doctor_appointment.verify_error_message()
