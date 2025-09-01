# frontend/steps/sortable_steps.py
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

@when('arrasto todos os elementos para ordem crescente')
def step_arrasto_elementos_ordem_crescente(context):
    # Obtém todos os elementos da lista
    items = WebDriverWait(context.driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".vertical-list-container .list-group-item"))
    )
    
    # Ordem esperada (crescente)
    expected_order = ["One", "Two", "Three", "Four", "Five", "Six"]
    
    # Para cada item na ordem esperada, move para a posição correta
    for i, expected_item in enumerate(expected_order):
        # Encontra o elemento que deve estar na posição i
        for item in items:
            if item.text == expected_item:
                # Se já está na posição correta, pula
                if items.index(item) == i:
                    break
                    
                # Move o elemento para a posição i
                actions = ActionChains(context.driver)
                actions.click_and_hold(item)
                actions.move_by_offset(0, (i - items.index(item)) * 50)  # Ajuste a distância conforme necessário
                actions.release()
                actions.perform()
                
                time.sleep(1)  # Pequena pausa para a animação
                break
        
        # Atualiza a lista de elementos após cada movimento
        items = context.driver.find_elements(By.CSS_SELECTOR, ".vertical-list-container .list-group-item")

@then('os elementos devem estar na ordem correta')
def step_valido_ordem_correta(context):
    # Obtém todos os elementos da lista
    items = WebDriverWait(context.driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".vertical-list-container .list-group-item"))
    )
    
    # Ordem esperada (crescente)
    expected_order = ["One", "Two", "Three", "Four", "Five", "Six"]
    
    # Verifica se cada elemento está na posição correta
    for i, item in enumerate(items):
        assert item.text == expected_order[i], f"Elemento na posição {i} é '{item.text}', mas esperado '{expected_order[i]}'"
    
    print("Todos os elementos estão na ordem correta!")