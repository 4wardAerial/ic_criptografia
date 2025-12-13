from time import sleep

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

def inicio():
    cls()
    print("\n---------------------")
    print("Bem-vind@ ao sistema.")
    print("---------------------")

def tipo_de_cripto() -> int:
    print("\nQual sistema criptográfico deseja utilizar?")
    sleep(1)
    print("1) RSA")
    sleep(0.5)
    print("2) ElGamal")
    sleep(0.5)
    print("3) Polinomial")
    sleep(1)
    return escolha_opcoes((1, 2, 3))

def critpo_ou_decripto() -> int:
    print("\nO que você deseja fazer com sua mensagem?")
    sleep(1)
    print("1) Criptografá-la")
    sleep(0.5)
    print("2) Descriptografá-la")
    sleep(1)
    return escolha_opcoes((1, 2))

def RSA_cripto():
    pass

def RSA_decripto() -> tuple:
    cls()
    print("\n---------------------")
    print("Decriptografia RSA")
    print("---------------------")
    sleep(1)
    print("\nInsira a mensagem cifrada:")
    sleep(1)
    cyph = input("> ")
    sleep(1)
    print("\nInsira sua chave privada:")
    sleep(1)
    cpriv_d = int(input("> "))
    return (cyph, cpriv_d)

def print_decriptografada(msg: str):
    print("\nA mensagem decriptografada é:")
    for c in msg:
        sleep(0.1)
        print(c)

