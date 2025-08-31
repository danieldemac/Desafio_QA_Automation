from behave import given, when, then

@given("que eu crio um usuário válido")
def step_impl(context):
    print("Usuário criado (placeholder)")

@when("eu gero um token de acesso para este usuário")
def step_impl(context):
    print("Token gerado (placeholder)")

@when("verifico se o usuário está autorizado")
def step_impl(context):
    print("Usuário autorizado (placeholder)")

@when("consulto a lista de livros disponíveis")
def step_impl(context):
    print("Livros listados (placeholder)")

@when("escolho dois livros e reservo para o usuário")
def step_impl(context):
    print("Livros reservados (placeholder)")

@then("eu devo visualizar os detalhes do usuário com os livros reservados")
def step_impl(context):
    print("Detalhes do usuário exibidos (placeholder)")
