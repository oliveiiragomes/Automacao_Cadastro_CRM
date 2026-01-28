# 🤖 Automação GUI - Sistema de Cadastro de Contatos

## 📋 Descrição da Automação

Esta é uma aplicação de automação GUI (Interface Gráfica do Usuário) desenvolvida em Python que permite cadastrar contatos automaticamente em um sistema através de preenchimento de formulários. A automação lê dados de uma planilha CSV e preenche os campos de contato (nome, email e telefone) de forma automatizada, economizando tempo em tarefas repetitivas.

A aplicação utiliza controle de mouse, teclado e monitor para simular ações do usuário, permitindo integração com praticamente qualquer sistema que possua interface gráfica.

---

## ✨ Funcionalidades

- ✅ **Cadastro Automático de Contatos**: Preenche automaticamente formulários com dados de contatos
- ✅ **Leitura de Dados em CSV**: Importa informações de uma planilha em formato CSV
- ✅ **Interface em Menu**: Interface de linha de comando amigável para controlar a automação
- ✅ **Personalização de Planilhas**: Permite escolher diferentes arquivos CSV como fonte de dados
- ✅ **Segurança Failsafe**: Ativa segurança para evitar travamentos, permitindo interromper a automação movendo o mouse para um canto da tela
- ✅ **Campos Suportados**: Nome, Email, Telefone e Situação do Contato
- ✅ **Delays Configuráveis**: Pausas entre cliques para garantir estabilidade

---

## 🔧 Requisitos para Rodar a Automação

### Requisitos de Sistema
- **Sistema Operacional**: Windows 7 ou superior
- **Python**: Versão 3.7 ou superior
- **RAM**: Mínimo 2GB
- **Resolução de Tela**: Recomenda-se 1920x1080 (as coordenadas são configuradas de acordo com as configurações do seu monitor, para verificar isso rode o arquivo "pgmouseinfo.py" para verificar as coordenadas)

### Dependências Python
As seguintes bibliotecas Python são necessárias:

- `pyautogui` (>= 0.9.53) — Automação de mouse e teclado

### Arquivos Necessários
- `auto_test.py` - Script principal de automação
- `coordenadas.py` - Coordenadas dos campos na interface
- `interface_automacao.py` - Interface do menu
- `planilha_dados.csv` - Dados dos contatos a serem criados (ou arquivo CSV customizado)

---

## 📦 Tutorial de Instalação

### Passo 1: Verificar Instalação do Python

Abra o PowerShell e verifique se Python está instalado:

```powershell
python --version
```

Se Python não estiver instalado, baixe em: https://www.python.org/downloads/

**Importante**: Durante a instalação, marque a opção **"Add Python to PATH"**

### Passo 2: Clonar ou Baixar o Projeto

Navegue até a pasta do projeto (substitua <seu_usuario> pelo seu usuário ou use o caminho onde baixou o projeto):

```powershell
cd "C:\Users\<seu_usuario>\OneDrive\Área de Trabalho\AUTOMACAO_GUI"
```

### Passo 3: Instalar Dependências

Esta aplicação foi escrita para rodar diretamente na máquina do usuário (sem uso obrigatório de ambiente virtual). Atualize o `pip` e instale a dependência necessária:

```powershell
pip install --upgrade pip
pip install pyautogui
```

### Passo 4: Configurar Coordenadas (Importante!)

As coordenadas dos campos devem ser ajustadas para sua resolução de tela. Edite o arquivo `coordenadas.py`:

```python
coordenada_novo = (682, 131)              # Botão "Novo Contato"
coordenada_novo_contato = (675, 173)      # Menu "Novo Contato"
coordenada_nome = (2057, 380)             # Campo de Nome
coordenada_email = (2038, 295)            # Campo de Email
coordenada_telefone = (2131, 718)         # Campo de Telefone
coordenada_situacao = (2068, 882)         # Campo de Situação
coordenada_criar = (2051, 1033)           # Botão de Criar
```

Para descobrir as coordenadas corretas, use a ferramenta `pgmouseinfo.py`:

```powershell
python pgmouseinfo.py
```

### Passo 5: Preparar Dados (Planilha CSV)

Crie um arquivo CSV com os dados dos contatos. O formato deve ser:

```csv
Nome;Email;Telefone
João Silva;joao@email.com;+55 11 98765 4321
Maria Santos;maria@email.com;+55 11 99876 5432
```

**Importante**: 
- Use `;` (ponto e vírgula) como separador
- A primeira linha deve conter: `Nome;Email;Telefone`
- Encoding deve ser UTF-8

### Passo 6: Executar a Automação

Execute o script principal com a interface de menu:

```powershell
python interface_automacao.py
```

Ou execute diretamente:

```powershell
python auto_test.py
```

A interface oferecerá as seguintes opções:

```
=== Interface de Automação ===
1. Iniciar automação
2. Inserir planilha
3. Sair

Escolha uma opção:
```

---

## 🎯 Como Usar

### Exemplo de Uso Completo

1. **Inicie a aplicação**:
   ```powershell
   python interface_automacao.py
   ```

2. **Escolha a opção 2 para inserir a planilha** (se não quiser usar a padrão):
   ```
   Digite o caminho completo para a planilha CSV: C:\dados\contatos.csv
   ```

3. **Escolha a opção 1 para iniciar a automação**:
   ```
   Iniciando automação com a planilha: planilha_dados.csv
   ```

4. **A automação irá**:
   - Clicar no botão "Novo Contato"
   - Preencher Nome, Email e Telefone
   - Definir Situação do lead como "novo"
   - Clicar em "Criar"
   - Repetir para cada linha da planilha

### Segurança - Failsafe

A automação possui proteção contra travamentos. Para interromper em qualquer momento:

**Mova o mouse rapidamente para o canto superior esquerdo da tela** (coordenada 0,0)

---

## 🐛 Possíveis de Problemas

### Problema: "ModuleNotFoundError: No module named 'pyautogui'"

**Solução**:
```powershell
pip install pyautogui
```

### Problema: Coordenadas não correspondem à sua tela

**Solução**: Execute `pgmouseinfo.py` para descobrir as coordenadas corretas:
```powershell
python pgmouseinfo.py
```

Atualize as coordenadas em `coordenadas.py`

### Problema: Arquivo CSV não encontrado

**Solução**: Verifique se o caminho está correto e se o arquivo existe:
```powershell
Get-ChildItem -Path "C:\Users\<seu_usuario>\OneDrive\Área de Trabalho\AUTOMACAO_GUI\planilha_dados.csv"
```

### Problema: Automação muito lenta ou rápida

**Solução**: Ajuste os valores de `time.sleep()` no arquivo `auto_test.py`

---

## 📁 Estrutura do Projeto

```
AUTOMACAO_GUI/
├── auto_test.py                 # Script principal de automação
├── coordenadas.py               # Coordenadas dos campos
├── interface_automacao.py       # Interface do menu
├── pgmouseinfo.py              # Ferramenta para encontrar coordenadas
├── planilha_dados.csv          # Dados dos contatos (exemplo)
├── coordenadas.txt             # Backup de coordenadas
├── README.md                   # Este arquivo
├── Fluxograma_automacao.bpm   # Diagrama do fluxo
├── Dsol.excalidraw            # Esboço visual
└── cache/                      # Pasta de cache
```

---

## 💡 Dicas e Boas Práticas

1. **Teste com poucos registros**: Comece com 2-3 contatos para verificar se as coordenadas estão corretas
2. **Mantenha a janela ativa**: Não minimize a janela do aplicativo durante a automação
3. **Feche outras aplicações**: Minimize programas que possam interferir com os cliques
4. **Backup de dados**: Faça backup da planilha antes de executar a automação
5. **Verificação manual**: Revise alguns registros após a automação para garantir preenchimento correto

---

## 📞 Suporte

Para dúvidas ou problemas:

1. Verifique o arquivo `coordenadas.txt` para referência
2. Consulte o diagrama em `Fluxograma_automacao.bpm`
3. Execute o script de teste: `hub_test.py`

---

## 📄 Licença

Projeto desenvolvido para automação local.

---
