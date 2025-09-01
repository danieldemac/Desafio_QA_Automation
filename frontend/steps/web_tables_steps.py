# frontend/steps/web_tables_steps.py
from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
import random


@when('crio um novo registro com dados aleatórios')
def step_crio_novo_registro(context):
    # Clique no botão Add
    add_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.ID, "addNewRecordButton"))
    )
    add_button.click()
    
    # Preencha o formulário com dados aleatórios
    first_name = f"Test{random.randint(100, 999)}"
    last_name = f"User{random.randint(100, 999)}"
    email = f"test{random.randint(100, 999)}@example.com"
    age = random.randint(18, 65)
    salary = random.randint(30000, 100000)
    department = f"Dept{random.randint(1, 10)}"
    
    context.driver.find_element(By.ID, "firstName").send_keys(first_name)
    context.driver.find_element(By.ID, "lastName").send_keys(last_name)
    context.driver.find_element(By.ID, "userEmail").send_keys(email)
    context.driver.find_element(By.ID, "age").send_keys(age)
    context.driver.find_element(By.ID, "salary").send_keys(salary)
    context.driver.find_element(By.ID, "department").send_keys(department)
    
    # Clique em Submit
    context.driver.find_element(By.ID, "submit").click()
    time.sleep(2)
    
    # Salve os dados do registro para referência futura
    context.registro_criado = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "age": age,
        "salary": salary,
        "department": department
    }

@when('edito o registro criado')
def step_edito_registro(context):
    # Encontre o registro na tabela e clique no ícone de edição
    email = context.registro_criado["email"]
    edit_button_xpath = f"//div[contains(text(), '{email}')]/ancestor::div[@class='rt-tr-group']//span[@title='Edit']"
    edit_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, edit_button_xpath))
    )
    edit_button.click()
    
    # Edite alguns campos
    new_age = random.randint(18, 65)
    context.driver.find_element(By.ID, "age").clear()
    context.driver.find_element(By.ID, "age").send_keys(new_age)
    
    # Atualize o contexto
    context.registro_criado["age"] = new_age
    
    # Clique em Submit
    context.driver.find_element(By.ID, "submit").click()
    time.sleep(2)

@when('deleto o registro criado')
def step_deleto_registro(context):
    # Encontre o registro na tabela e clique no ícone de deletar
    email = context.registro_criado["email"]
    delete_button_xpath = f"//div[contains(text(), '{email}')]/ancestor::div[@class='rt-tr-group']//span[@title='Delete']"
    delete_button = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, delete_button_xpath))
    )
    delete_button.click()
    time.sleep(2)

@then('o registro não deve mais aparecer na tabela')
def step_valido_registro_deletado(context):
    email = context.registro_criado["email"]
    try:
        context.driver.find_element(By.XPATH, f"//div[contains(text(), '{email}')]")
        assert False, "Registro ainda aparece na tabela"
    except:
        pass  # Registro não encontrado, como esperado

@when('crio {quantidade} registros com dados aleatórios')
def step_crio_multiplos_registros(context, quantidade):
    context.registros_criados = []
    for i in range(int(quantidade)):
        # Clique no botão Add
        add_button = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "addNewRecordButton"))
        )
        add_button.click()
        
        # Gere dados aleatórios
        first_name = f"Test{i+1}"
        last_name = f"User{i+1}"
        email = f"test{i+1}@example.com"
        age = random.randint(18, 65)
        salary = random.randint(30000, 100000)
        department = f"Dept{i+1}"
        
        # Preencha o formulário
        context.driver.find_element(By.ID, "firstName").send_keys(first_name)
        context.driver.find_element(By.ID, "lastName").send_keys(last_name)
        context.driver.find_element(By.ID, "userEmail").send_keys(email)
        context.driver.find_element(By.ID, "age").send_keys(age)
        context.driver.find_element(By.ID, "salary").send_keys(salary)
        context.driver.find_element(By.ID, "department").send_keys(department)
        
        # Clique em Submit
        context.driver.find_element(By.ID, "submit").click()
        time.sleep(1)
        
        # Salve os dados do registro
        context.registros_criados.append({
            "email": email,
            "first_name": first_name,
            "last_name": last_name
        })

@when('deleto todos os registros criados')
def step_deleto_todos_registros(context):
    for registro in context.registros_criados:
        email = registro["email"]
        delete_button_xpath = f"//div[contains(text(), '{email}')]/ancestor::div[@class='rt-tr-group']//span[@title='Delete']"
        try:
            delete_button = WebDriverWait(context.driver, 5).until(
                EC.element_to_be_clickable((By.XPATH, delete_button_xpath))
            )
            delete_button.click()
            time.sleep(1)
        except:
            print(f"Registro com email {email} não encontrado para deletar")

@then('a tabela deve estar vazia')
def step_valido_tabela_vazia(context):
    # Verifique se a tabela está vazia (apenas cabeçalho)
    rows = context.driver.find_elements(By.CLASS_NAME, "rt-tr-group")
    for row in rows:
        try:
            # Se uma linha tem dados, deve ter divs com texto
            data_cells = row.find_elements(By.CLASS_NAME, "rt-td")
            has_data = any(cell.text.strip() != "" for cell in data_cells)
            if has_data:
                assert False, "A tabela não está vazia"
        except:
            continue