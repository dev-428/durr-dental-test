from selenium import webdriver
from behave import fixture


@fixture
def before_scenario(context, scenario):
    """
    Loads up chrome driver before each scenario.
    """
    
    context.driver = webdriver.Chrome()

@fixture
def after_scenario(context, scenario):
    """
    Quits chrome criver after each scenario.
    """
    
    context.driver.quit()
