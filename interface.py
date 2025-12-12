import csv
import time
from pathlib import Path
from criptografador import *

DIR = Path(__file__).resolve().parent
csv_path = DIR / "arquivos" / "usuarios.csv"

def carregar_usuarios():
    with csv_path.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return {linha["nome"]: linha for linha in reader}

def cadastro(nome: str):
    print("\n-------------------------------------------------")
    print("Para gerarmos suas chaves, vamos precisar de números primos.")
    print("\nDigite o número referente a sua escolha:")
    print("1. Fornecer os próprios primos")
    print("2. Usar primos aleatórios")
    escolha_primos = int(input("> "))

    if escolha_primos == 1:
        print("Digite seu primeiro primo:")
        p = int(input("> "))
        print("Digite seu segundo primo:")
        q = int(input("> "))
    elif escolha_primos == 2:
        pass
    else:
        print("Entrada inválida! Primos serão escolhidos aleatoriamente.")
        

def login():
    usuarios = carregar_usuarios()

    print("\n-------------------------------------------------")
    print("Bem-vind@ ao sistema. Por favor, insira seu nome:")
    nome = input("> ")

    if nome not in usuarios:
        print("\nNome não registrado no sistema. Vamos iniciar o cadastro.")
        time.sleep(1)
        cadastro(nome)
    else:
        print("Insira sua chave privada:")
        chave_priv = input("> ")

login()



