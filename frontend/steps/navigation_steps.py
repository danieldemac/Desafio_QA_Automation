# frontend/steps/navigation_steps.py
from behave import given
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@given('navego para "{menu}" > "{submenu}"')
def step_navega_menu(context, menu, submenu):
    # Remove anúncios que possam estar bloqueando a tela
    context.driver.execute_script("""
        var elements = document.querySelectorAll('iframe');
        for (var i = 0; i < elements.length; i++) {
            elements[i].remove();
        }
    """)
    time.sleep(2)
    
    # Clique no menu principal
    menu_xpath = f"//h5[contains(text(), '{menu}')]"
    menu_element = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, menu_xpath))
    )
    context.driver.execute_script("arguments[0].scrollIntoView(true);", menu_element)
    menu_element.click()
    
    # Clique no submenu
    submenu_xpath = f"//span[contains(text(), '{submenu}')]"
    submenu_element = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, submenu_xpath))
    )
    submenu_element.click()