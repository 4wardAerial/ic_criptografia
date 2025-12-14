from time import sleep
from pathlib import Path

import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def escolha_opcoes(opcoes: tuple) -> int:
    print("\nDigite o número correspondente a sua escolha:")
    while(True):
        escolha = int(input("> "))
        if escolha not in opcoes:
            print("Selecione uma opção válida.")
        else:
            return escolha
    
def escolha_nomes():
    pass

def inicio():
    cls()
    print("\nBem-vind@ ao sistema.")
    print("---------------------")

def repetir() -> int:
    sleep(0.7)
    print("\n---------------------")
    print("Deseja continuar no sistema?")
    sleep(0.7)
    print("1) Sim")
    sleep(0.5)
    print("2) Não")
    sleep(0.5)
    return escolha_opcoes((1, 2))

def voltar():
    cls()
    print("\n---------------------")
    
def sair():
    sleep(1)
    print("\nObrigad@ por usar o sistema.")
    print("---------------------")

def tipo_de_cripto() -> int:
    print("\nQual sistema criptográfico deseja utilizar?")
    sleep(0.7)
    print("1) RSA")
    sleep(0.5)
    print("2) ElGamal")
    sleep(0.5)
    print("3) Polinomial")
    sleep(0.7)
    return escolha_opcoes((1, 2, 3))

def critpo_ou_decripto() -> int:
    print("\nO que você deseja fazer com sua mensagem?")
    sleep(0.7)
    print("1) Criptografá-la")
    sleep(0.5)
    print("2) Descriptografá-la")
    sleep(0.7)
    return escolha_opcoes((1, 2))

def listar_nomes():
    DIR = Path(__file__).resolve().parent
    outros_csv = DIR / "arquivos" / "dados_outros.csv"
    with outros_csv.open(encoding="utf-8") as docsv:
        pass


def RSA_cripto():
    cls()
    print("\nCriptografia RSA")
    print("---------------------")
    sleep(0.7)
    print("Para quem você quer enviar uma mensagem?")
    listar_nomes()
    sleep(0.7)
    return escolha_nomes()

def RSA_decripto() -> tuple:
    cls()
    print("\nDecriptografia RSA")
    print("---------------------")
    sleep(0.7)
    print("\nInsira a mensagem cifrada:")
    sleep(0.7)
    cyph = input("> ")
    sleep(0.7)
    print("\nInsira sua chave privada:")
    sleep(0.7)
    cpriv_d = int(input("> "))
    return (cyph, cpriv_d)

def print_decriptografada(msg: str):
    print("\nA mensagem decriptografada é:")
    print(msg)

