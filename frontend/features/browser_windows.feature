# frontend/features/browser_windows.feature
Feature: Browser Windows no DemoQA

  Scenario: Abrir e fechar nova janela
    Given acesso o site "https://demoqa.com"
    And navego para "Alerts, Frame & Windows" > "Browser Windows"
    When clico no botão "New Window"
    Then uma nova janela é aberta
    And valido a mensagem "This is a sample page" na nova janela
    And fecho a nova janela