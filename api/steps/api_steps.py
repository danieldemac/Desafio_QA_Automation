import requests
from behave import given, when, then
from faker import Faker
import json

fake = Faker()

BASE_URL = "https://demoqa.com"

@given("que eu crio um usuário válido")

def step_impl(context):
    
    context.username = fake.user_name()
    context.password = fake.password()
    url = f"{BASE_URL}/Account/v1/User"
    payload = {
        "userName": context.username,
        "password": context.password
    }
    
    response = requests.post(url, json=payload)
    context.user_id = response.json().get("userID")
    
    print(f"Usuário criado: {context.username}, userID: {context.user_id}")
    print("Resposta:\n", json.dumps(response.json(), indent=4))

@when("eu gero um token de acesso para este usuário")

def step_impl(context):
    
    url = f"{BASE_URL}/Account/v1/GenerateToken"
    payload = {
        "userName": context.username,
        "password": context.password
    }
    
    response = requests.post(url, json=payload)
    context.token = response.json().get("token")
    
    print("Token gerado:", context.token)
    print("Resposta:\n", json.dumps(response.json(), indent=4))

@when("verifico se o usuário está autorizado")
def step_impl(context):
    
    url = f"{BASE_URL}/Account/v1/Authorized"
    headers = {"Authorization": f"Bearer {context.token}"}
    response = requests.get(url, headers=headers)
    
    print("Status HTTP:", response.status_code)
    print("Conteúdo retornado:\n", response.text)

@when("consulto a lista de livros disponíveis")

def step_impl(context):
    
    url = f"{BASE_URL}/BookStore/v1/Books"
    response = requests.get(url)
    context.books = response.json().get("books", [])[:2]
    
    print("Livros disponíveis (2 selecionados):", [b['title'] for b in context.books])
    print("Resposta completa:\n", json.dumps(response.json(), indent=4))

@when("escolho dois livros e reservo para o usuário")

def step_impl(context):
    
    url = f"{BASE_URL}/BookStore/v1/Books"
    headers = {"Authorization": f"Bearer {context.token}"}
    payload = {
        "userId": context.user_id,
        "collectionOfIsbns": [{"isbn": b["isbn"]} for b in context.books]
    }
    response = requests.post(url, json=payload, headers=headers)
    
    print("Livros reservados:", payload["collectionOfIsbns"])
    print("Resposta:\n", json.dumps(response.json(), indent=4))

@then("eu devo visualizar os detalhes do usuário com os livros reservados")

def step_impl(context):
    
    url = f"{BASE_URL}/Account/v1/User/{context.user_id}"
    headers = {"Authorization": f"Bearer {context.token}"}
    response = requests.get(url, headers=headers)
    user_details = response.json()
    

    print("Detalhes do usuário com livros reservados:")
    print(json.dumps(user_details, indent=4))
    
    with open("api/user_details.json", "w", encoding="utf-8") as f:
        json.dump(user_details, f, indent=4, ensure_ascii=False)
    print("Arquivo 'user_details.json' criado com sucesso na pasta 'api'.")

