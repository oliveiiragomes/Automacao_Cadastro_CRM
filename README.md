# Automação de cadastro de contatos

Este projeto usa mouse e teclado para preencher um formulário de cadastro com os dados de um arquivo CSV. A interface é um menu de terminal; os cliques são feitos por coordenadas de tela configuradas em `coordenadas.py`.

> Use apenas em um sistema ao qual você tem autorização de acesso. Antes de cadastrar dados reais, teste com uma planilha pequena e confira os resultados.

## Requisitos

- Windows e Python instalado e disponível no PowerShell (`python --version`).
- A biblioteca `pyautogui`.
- O sistema de cadastro aberto, na mesma tela e posição usadas para configurar as coordenadas.

## Instalação

Abra a pasta do projeto no VS Code e use o terminal PowerShell integrado. Crie um ambiente virtual e instale a dependência:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install pyautogui
```

O ambiente virtual evita instalar a dependência globalmente. Os comandos deste guia usam o Python desse ambiente.

## Prepare as coordenadas

Os valores que já estão em `coordenadas.py` são específicos de uma tela e de uma disposição do sistema. Eles podem não servir no seu computador. Configure o sistema de cadastro na resolução, no zoom e na posição em que pretende executar a automação.

1. Em um segundo terminal PowerShell, também aberto na pasta do projeto, execute:

   ```powershell
   .\.venv\Scripts\python.exe pgmouseinfo.py
   ```

2. Mova o ponteiro sobre cada botão ou campo e anote as coordenadas exibidas: Novo, Novo contato, Nome, Email, Telefone, Situação e Criar.
3. Encerre a ferramenta com `Ctrl+C` e substitua os valores correspondentes em `coordenadas.py`.
4. Mantenha o sistema de cadastro na mesma posição durante a automação. Se mudar a resolução, o zoom ou a posição da janela, confira as coordenadas novamente.

## Prepare o CSV

O arquivo padrão é `planilha_dados.csv`, localizado na pasta do projeto. A automação espera um CSV em UTF-8, separado por ponto e vírgula (`;`), com estes cabeçalhos exatos:

```csv
Nome;Email;Telefone
Ana Souza;ana@example.com;+55 11 98765 4321
```

Cada linha abaixo do cabeçalho representa um contato. Mantenha as três colunas e evite acentos nos valores: a automação digita o texto pelo teclado usando `pyautogui.write`. Confira os dados antes de iniciar; o CSV que acompanha o projeto contém vários registros de exemplo.

## Executar

No terminal PowerShell aberto na pasta do projeto, inicie o menu:

```powershell
.\.venv\Scripts\python.exe interface_automacao.py
```

O menu oferece:

- `1. Iniciar automação`: usa `planilha_dados.csv` por padrão. Antes de escolher, abra o formulário de cadastro e deixe a tela pronta.
- `2. Inserir planilha`: informa outro arquivo CSV. Digite o caminho do arquivo existente, por exemplo `C:\dados\contatos.csv`, sem aspas. Depois escolha a opção 1.
- `3. Sair`: encerra o menu.

Para cada linha do arquivo, a automação abre um novo contato, preenche nome, email e telefone, define a situação como `novo` e aciona Criar. Ela não valida se o cadastro foi aceito pelo sistema; confira os registros ao final.

## Interromper a automação

O PyAutoGUI tem proteção de emergência habilitada. Mova o ponteiro do mouse para o canto superior esquerdo da tela para interromper a execução. Como a automação controla mouse e teclado, não use o computador nem mova ou minimize a janela do sistema enquanto ela estiver rodando.

## Problemas comuns

- **`No module named 'pyautogui'`**: instale a dependência com:

  ```powershell
  .\.venv\Scripts\python.exe -m pip install pyautogui
  ```

- **Planilha não encontrada**: confirme que o caminho digitado existe. Para usar o arquivo padrão, execute o comando a partir da pasta do projeto.
- **Erro de coluna ou dados não preenchidos**: confirme que a primeira linha é exatamente `Nome;Email;Telefone`, que o delimitador é `;` e que não há colunas faltando.
- **Cliques no lugar errado**: atualize as coordenadas em `coordenadas.py` com `pgmouseinfo.py` e confira resolução, zoom e posição da janela.

## Arquivos do projeto

- `interface_automacao.py`: menu e seleção do CSV.
- `automacao.py`: leitura do CSV e preenchimento do formulário.
- `coordenadas.py`: coordenadas de botões e campos.
- `pgmouseinfo.py`: ferramenta para consultar a posição do mouse.
- `planilha_dados.csv`: planilha de exemplo usada por padrão.
