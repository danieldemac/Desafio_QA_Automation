# frontend/features/web_tables.feature
Feature: Web Tables no DemoQA

  Scenario: Criar, editar e deletar um registro
    Given acesso o site "https://demoqa.com"
    And navego para "Elements" > "Web Tables"
    When crio um novo registro com dados aleatórios
    And edito o registro criado
    And deleto o registro criado
    Then o registro não deve mais aparecer na tabela

  Scenario Outline: Criar e deletar múltiplos registros (Bônus)
    Given acesso o site "https://demoqa.com"
    And navego para "Elements" > "Web Tables"
    When crio <quantidade> registros com dados aleatórios
    And deleto todos os registros criados
    Then a tabela deve estar vazia

    Examples:
      | quantidade |
      | 12         |