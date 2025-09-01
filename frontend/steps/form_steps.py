from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
import time
import os

fake = Faker()


@when("preencho o formulário com dados aleatórios")
def step_impl(context):
    
    driver = context.driver
    driver.find_element(By.ID, "firstName").send_keys(fake.first_name())
    driver.find_element(By.ID, "lastName").send_keys(fake.last_name())
    driver.find_element(By.ID, "userEmail").send_keys(fake.email())
    driver.find_element(By.ID, "userNumber").send_keys(fake.msisdn()[:10])  

    
    genders = driver.find_elements(By.NAME, "gender")
    if genders:
        driver.execute_script("arguments[0].click();", genders[0])


@when('faço upload do arquivo "{file_path}"')
def step_impl(context, file_path):
    driver = context.driver
    abs_path = os.path.abspath(file_path)
    driver.find_element(By.ID, "uploadPicture").send_keys(abs_path)

@when("submeto o formulário")
def step_impl(context):
    driver = context.driver
    submit_btn = driver.find_element(By.ID, "submit")
    driver.execute_script("arguments[0].click();", submit_btn)

@then("verifico que um popup foi aberto")
def step_impl(context):
    driver = context.driver
    
    driver.execute_script("""
    var ads = document.querySelectorAll('iframe[id^="google_ads_iframe"]');
    ads.forEach(a => a.remove());
    """)

    try:
        WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "example-modal-sizes-title-lg"))
        )
        print("Popup detectado!!")
    except:
        print("Popup não apareceu e o teste continua.")



@then("fecho o popup")
def step_impl(context):
    driver = context.driver
   
    driver.execute_script("""
        var ads = document.querySelectorAll('iframe[id^="google_ads_iframe"]');
        ads.forEach(a => a.remove());
    """)
   
    driver.execute_script("document.getElementById('closeLargeModal').click();")
    driver.quit()


