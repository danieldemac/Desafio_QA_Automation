# frontend/steps/browser_windows_steps.py
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


@when('clico no botão "{texto_botao}"')
def step_clico_botao(context, texto_botao):
    botao_xpath = f"//button[contains(text(), '{texto_botao}')]"
    WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, botao_xpath))
    ).click()


@then('uma nova janela é aberta')
def step_nova_janela_aberta(context):
    # Guarda a janela original
    context.janela_original = context.driver.current_window_handle

    # Aguarda até que uma nova janela seja aberta
    WebDriverWait(context.driver, 10).until(
        lambda d: len(d.window_handles) > 1
    )


@then('valido a mensagem "{mensagem}" na nova janela')
def step_valido_mensagem_janela(context, mensagem):
    # Pega a nova janela (que não é a original)
    novas_janelas = [
        janela for janela in context.driver.window_handles
        if janela != context.janela_original
    ]
    nova_janela = novas_janelas[0]
    context.driver.switch_to.window(nova_janela)

    # Valida a mensagem na nova janela
    WebDriverWait(context.driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, "body"))
    )
    assert mensagem in context.driver.page_source


@then('fecho a nova janela')
def step_fecho_janela(context):
    # Fecha a nova janela e volta para a original
    context.driver.close()
    context.driver.switch_to.window(context.janela_original)
