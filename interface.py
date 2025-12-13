import csv
import time
from pathlib import Path
from criptografador import *

def escolha_opcoes(opcoes: tuple) -> int:
    print("\nDigite o número correspondente a sua escolha:")

    while(True):
        escolha = int(input("> "))
        if escolha not in opcoes:
            print("Selecione uma opção válida.")
        else:
            return escolha

def carregar_usuarios():
    pass

def cadastro(nome: str):
    pass
        

def login():
    pass

def critpo_ou_decripto() -> int:
    print("O que você deseja fazer com sua mensagem?")
    print("1) Criptografá-la")
    print("2) Descriptografá-la")

    return escolha_opcoes((1, 2))

def tipo_de_cripto() -> int:
    print("Qual sistema criptográfico deseja utilizar?")
    print("1) RSA")
    print("2) ElGamal")
    print("3) Polinomial")

    return escolha_opcoes((1, 2, 3))


