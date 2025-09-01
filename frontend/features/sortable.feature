# frontend/features/sortable.feature
Feature: Sortable no DemoQA

  Scenario: Ordenar elementos em ordem crescente
    Given acesso o site "https://demoqa.com"
    And navego para "Interactions" > "Sortable"
    When arrasto todos os elementos para ordem crescente
    Then os elementos devem estar na ordem correta