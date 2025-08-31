Feature: Fluxo de API do desafio Accenture

  Scenario: Criar usuário, autenticar e reservar livros
    Given que eu crio um usuário válido
    When eu gero um token de acesso para este usuário
    And verifico se o usuário está autorizado
    And consulto a lista de livros disponíveis
    And escolho dois livros e reservo para o usuário
    Then eu devo visualizar os detalhes do usuário com os livros reservados
