import pyautogui
import time
import csv
from coordenadas import*


# Ativa a segurança
pyautogui.FAILSAFE = True



def criar_contato():
    pyautogui.click(coordenada_novo)
    time.sleep(0.5)
    pyautogui.click(coordenada_novo_contato)
    time.sleep(0.5)


def colar_nome(nome):
    """Cola o nome no campo de nome do sistema."""
    pyautogui.click(coordenada_nome)  # <-- ajustar coordenada
    pyautogui.write(nome)
    time.sleep(1)


def colar_email(email):
    """Cola o email no campo de email do sistema."""
    pyautogui.click(coordenada_email)  # <-- ajustar coordenada
    pyautogui.write(email)
    time.sleep(1)


def colar_telefone(telefone):
    """Cola o telefone no campo de telefone do sistema."""
    pyautogui.click(coordenada_telefone)  # <-- ajustar coordenada
    pyautogui.write(telefone)
    time.sleep(1)
    pyautogui.click(coordenada_situacao)
    time.sleep(1)
    pyautogui.write("novo")
    pyautogui.press("Enter")
    time.sleep(1)
    pyautogui.click(coordenada_criar)
    time.sleep(1)

def run_automation(planilha_path):
    """Executa a automação usando a planilha especificada."""
    # Carregando os dados do CSV para uma lista de dicionários
    dados = []
    with open(planilha_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            dados.append(row)

    # Loop para percorrer a lista de dados e preencher o formulário
    for usuario in dados:
        time.sleep(5)
        
        criar_contato()
        time.sleep(2)
        
        colar_nome(usuario['Nome'])
        time.sleep(1)
            
        colar_email(usuario['Email'])
        time.sleep(1)
        
        
        colar_telefone(usuario['Telefone'])
        time.sleep(1)
    