# frontend/steps/common_steps.py
from behave import given
from selenium import webdriver

@given('acesso o site "{url}"')
def step_acesso_site(context, url):
    if not hasattr(context, 'driver'):
        context.driver = webdriver.Chrome()
        context.driver.maximize_window()
    context.driver.get(url)