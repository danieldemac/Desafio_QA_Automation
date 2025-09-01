Feature: Preencher formulário no DemoQA

  Scenario: Preencher e submeter o Practice Form
    Given acesso o site "https://demoqa.com/automation-practice-form"
    When preencho o formulário com dados aleatórios
    And faço upload do arquivo "frontend/files/sample.txt"
    And submeto o formulário
    Then verifico que um popup foi aberto
    And fecho o popup
