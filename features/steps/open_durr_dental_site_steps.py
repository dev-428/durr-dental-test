import time
from selenium import webdriver
from behave import given, when, then


@given('I open VistaSoft Monitor on my browser')
def open_vistasoft_monitor(context):
    url = context.config.userdata.get('VistaSoftMonitorWelcomePageLink')
    context.driver.get(url)
    time.sleep(5)
