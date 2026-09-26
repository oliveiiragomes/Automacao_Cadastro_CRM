import os
from automacao import run_automation

# Variável global para armazenar o caminho da planilha
planilha_path = 'planilha_dados.csv'  # padrão

def menu():
    global planilha_path

    while True:
        print("\n=== Interface de Automação ===")
        print("1. Iniciar automação")
        print("2. Inserir planilha")
        print("3. Sair")
        escolha = input("Escolha uma opção: ").strip()

        if escolha == '1':
            if os.path.exists(planilha_path):
                print(f"Iniciando automação com a planilha: {planilha_path}")
                run_automation(planilha_path)
                print("Automação finalizada!")
            else:
                print(f"Erro: Arquivo '{planilha_path}' não encontrado. Insira um caminho válido.")
        elif escolha == '2':
            novo_path = input("Digite o caminho completo para a planilha CSV: ").strip()
            if os.path.exists(novo_path):
                planilha_path = novo_path
                print(f"Planilha definida para: {planilha_path}")
            else:
                print("Erro: Arquivo não encontrado. Tente novamente.")
        elif escolha == '3':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu()
