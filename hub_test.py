import pyautogui
import time
from coordenadas import*



def copiar_nome():
    """Copia o nome da célula na planilha."""
    pyautogui.hotkey("ctrl", "c")
    time.sleep(0.2)
    pyautogui.hotkey("alt", "tab")


def copiar_email():
    """Copia o email da célula na planilha."""
    pyautogui.press("right")
    pyautogui.hotkey("ctrl", "c")
    time.sleep(0.2)
    pyautogui.hotkey("alt", "tab")

def copiar_telefone():
    """Copia o telefone da célula na planilha."""
    pyautogui.press("right")
    pyautogui.hotkey("ctrl", "c")
    time.sleep(0.2)
    pyautogui.press("left")
    pyautogui.press("left")
    pyautogui.press("down")
    pyautogui.hotkey("alt", "tab")
    time.sleep(0.2)





def colar_nome():
    """Cola o nome no campo de nome do sistema."""
    pyautogui.click(coordenada_nome)  # <-- ajustar coordenada
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.2)
    pyautogui.hotkey("alt", "tab")
    time.sleep(0.2)


def colar_email():
    """Cola o email no campo de email do sistema."""
    pyautogui.click(coordenada_email)  # <-- ajustar coordenada
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.2)
    pyautogui.hotkey("alt", "tab")
    time.sleep(0.2)


def colar_telefone():
    """Cola o telefone no campo de telefone do sistema."""
    pyautogui.click(coordenada_telefone)  # <-- ajustar coordenada
    pyautogui.hotkey("ctrl", "v")
    time.sleep(0.2)
    pyautogui.click(coordenada_situacao)
    time.sleep(0.5)
    pyautogui.write("novo")
    pyautogui.press("Enter")
    time.sleep(0.5)
    pyautogui.click(coordenada_criar)
    time.sleep(0.5)
    pyautogui.hotkey("alt", "tab")
    time.sleep(0.2)
    
    
    
    
def criar_contato():
    pyautogui.click(coordenada_novo)
    time.sleep(0.2)
    pyautogui.click(coordenada_novo_contato)
    time.sleep(0.2)
    pyautogui.hotkey("alt", "tab")
    time.sleep(0.2)




# Ativa a segurança
pyautogui.FAILSAFE = True


qtd_repeticoes = 5


for i in range(qtd_repeticoes):
    time.sleep(5)
    criar_contato()
    time.sleep(2)
    copiar_nome()
    time.sleep(1)
    colar_nome()
    time.sleep(1)
    
        
    copiar_email()
    time.sleep(1)
    colar_email()
    time.sleep(1)
    
    
    copiar_telefone()
    time.sleep(1)
    colar_telefone()
    time.sleep(1)
    