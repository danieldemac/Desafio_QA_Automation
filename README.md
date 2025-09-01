<h1 style="text-align:center; font-size:24px; font-weight:bold;">🤖 QA Automation - DemoQA</h1>
<p style="text-align:center;">Teste automatizado completo do site <strong>DemoQA</strong>, incluindo <strong>API</strong> e cenários frontend, usando <strong>Python, Selenium, Requests e Behave</strong>.</p>

<h2 style="text-align:center;">📋 Visão Geral</h2>
<p>Este projeto implementa automação completa para o desafio de <strong>QA Automation da Accenture</strong>, cobrindo:</p>
<ul>
  <li><strong>Parte 1</strong>: Testes de API (criação de usuário, autenticação, reserva de livros)</li>
  <li><strong>Parte 2</strong>: Testes de Frontend (5 cenários de automação web)</li>
</ul>

<h2 style="text-align:center;">🛠️ Pré-requisitos</h2>
<ul>
  <li>Python 3.12+</li>
  <li>Google Chrome</li>
  <li>ChromeDriver compatível com sua versão do Chrome</li>
  <li>Dependências Python:</li>
</ul>
<pre>pip install -r requirements.txt</pre>
<blockquote>
  <pre>
selenium==4.15.0
behave==1.2.6
requests==2.31.0
faker==19.3.0
  </pre>
</blockquote>

<h2 style="text-align:center;">📁 Estrutura do Projeto</h2>
<pre>
Desafio_QA_Automation/
│
├── api/
│
├── frontend/
│   ├── features/
│   │   ├── form.feature
│   │   ├── browser_windows.feature
│   │   ├── web_tables.feature
│   │   ├── progress_bar.feature
│   │   └── sortable.feature
│   ├── steps/
│   │   ├── common_steps.py
│   │   ├── navigation_steps.py
│   │   ├── form_steps.py
│   │   ├── browser_windows_steps.py
│   │   ├── web_tables_steps.py
│   │   ├── progress_bar_steps.py
│   │   └── sortable_steps.py
│   └── files/
│       └── sample.txt
│
├── requirements.txt
└── README.md
</pre>

<h2 style="text-align:center;">🚀 Como Executar os Testes</h2>

<h3>Testes de API</h3>
<pre>python -m behave api/features/api_flow.feature</pre>
<p>Isso irá executar o fluxo completo da API:</p>
<ul>
  <li>Criar um usuário</li>
  <li>Gerar token de acesso</li>
  <li>Verificar autorização</li>
  <li>Listar livros disponíveis</li>
  <li>Reservar dois livros</li>
  <li>Listar detalhes do usuário com livros reservados</li>
</ul>

<h3>Testes de Frontend</h3>
<p>Para executar todos os testes frontend:</p>
<pre>python -m behave frontend/features/</pre>
<p>Para executar testes específicos:</p>
<pre>
# Practice Form
python -m behave frontend/features/form.feature

# Browser Windows
python -m behave frontend/features/browser_windows.feature

# Web Tables (inclui bônus de 12 registros)
python -m behave frontend/features/web_tables.feature

# Progress Bar
python -m behave frontend/features/progress_bar.feature

# Sortable
python -m behave frontend/features/sortable.feature
</pre>

<h2 style="text-align:center;">🎯 Funcionalidades Implementadas</h2>

<h3>API</h3>
<ul>
  <li>Criação de usuário com dados dinâmicos usando Faker</li>
  <li>Autenticação e geração de token</li>
  <li>Reserva de livros com seleção aleatória</li>
  <li>Validação de respostas e persistência de resultados em JSON</li>
</ul>

<h3>Frontend</h3>
<ul>
  <li><strong>Practice Form</strong>: Preenchimento de formulário com upload de arquivo</li>
  <li><strong>Browser Windows</strong>: Manipulação de janelas e validação de conteúdo</li>
  <li><strong>Web Tables</strong>: CRUD completo + bônus de criação de 12 registros</li>
  <li><strong>Progress Bar</strong>: Controle e validação de barra de progresso</li>
  <li><strong>Sortable</strong>: Drag and drop para ordenação de elementos</li>
</ul>

<h2 style="text-align:center;">⚙️ Características Técnicas</h2>
<ul>
  <li>Padrão BDD com Gherkin</li>
  <li>Estrutura modular e organizada</li>
  <li>Steps compartilhados para evitar duplicação</li>
  <li>Geração de dados dinâmicos com Faker</li>
  <li>Tratamento de anúncios e elementos sobrepostos</li>
  <li>Esperas explícitas com WebDriverWait</li>
  <li>Validações com asserções</li>
</ul>

<h2 style="text-align:center;">📝 Observações Importantes</h2>
<ul>
  <li>O código remove automaticamente iframes de anúncios antes de interagir com elementos</li>
  <li>Os dados dos formulários são gerados aleatoriamente usando a biblioteca Faker</li>
  <li>O arquivo <code>sample.txt</code> é utilizado para testes de upload</li>
  <li>Os testes geram um arquivo JSON (<code>user_details.json</code>) com os resultados da API</li>
  <li>Para debugging, você pode inserir pausas no código: <pre>input("Pressione Enter para continuar...")</pre></li>
</ul>

<h2 style="text-align:center;">🔧 Possíveis Melhorias Futuras</h2>
<ul>
  <li>Implementação do padrão Page Object Model</li>
  <li>Geração de relatórios HTML com Allure ou Behave-html-formatter</li>
  <li>Screenshots automáticas em caso de falha</li>
  <li>Configuração de CI/CD com GitHub Actions</li>
  <li>Execução em paralelo para reduzir tempo de teste</li>
  <li>Configuração multi-navegador (Chrome, Firefox, Edge)</li>
</ul>

<h2 style="text-align:center;">📞 Suporte</h2>
<p>Em caso de dúvidas ou problemas com a execução dos testes, verifique:</p>
<ol>
  <li>Se todas as dependências estão instaladas corretamente</li>
  <li>Se a versão do ChromeDriver é compatível com seu Chrome</li>
  <li>Se o site DemoQA está acessível</li>
</ol>
