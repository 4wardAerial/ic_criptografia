from time import sleep
import os

from conversor_msg import tabela_char

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def escolha_opcoes(opcoes: tuple) -> int:
    print("\nDigite o número correspondente a sua escolha:")
    while(True):
        escolha = input("> ")
        if escolha not in opcoes:
            print("Selecione uma opção válida.")
        else:
            return int(escolha)
    
def escolha_nomes(outros_dict: dict) -> str:
    print("\nDigite o nome da pessoa com quem quer conversar:")
    while(True):
        nome = input("> ")
        if nome not in outros_dict:
            print("Escolha uma pessoa que está na lista.")
        else:
            return nome

def inicio():
    cls()
    sleep(0.3)
    print("---------------------")
    sleep(0.3)
    print("Bem-vind@ ao sistema.")
    sleep(0.3)
    print("---------------------")
    sleep(2)

def repetir() -> int:
    print("\n---------------------")
    print("Deseja continuar no sistema?")
    sleep(0.5)
    print("1) Sim")
    sleep(0.3)
    print("2) Não")
    sleep(0.3)
    return escolha_opcoes(('1', '2'))

def voltar():
    cls()
    print("\n---------------------")
    
def sair():
    print("\nObrigad@ por usar o sistema.")
    print("---------------------")
    sleep(2)

def listar_nomes(lista_nomes):
    print()
    for nome in lista_nomes:
        sleep(0.3)
        print(f"- {nome}")
    sleep(0.5)

def listar_tudo(outros_dict: dict, cpub_n: int, cpub_e: int):
    tam_nome = max(len(nome) for nome in outros_dict)
    tam_n = max(len(str(v1)) for v1, _ in outros_dict.values())
    tam_e = max(len(str(v2)) for _, v2 in outros_dict.values())
    print(f"\n- {'Eu':<{tam_nome}} : {str(cpub_n):<{tam_n}} , {str(cpub_e):<{tam_e}}")
    print()
    for k in outros_dict.keys():
        sleep(0.3)
        print(f"- {k.strip():<{tam_nome}} : {str(outros_dict[k][0]).strip():<{tam_n}} , {str(outros_dict[k][1]).strip():<{tam_e}}")
    sleep(0.5)

def ler_mensagem(repete: bool) -> str:
    if not repete:
        print("\nInsira sua mensagem:")
    msg = input("> ")
    return msg

def arq_inexistente(nome: str):
    print("\nO arquivo necessário não foi encontrado.")
    sleep(1)
    print(f"Certifique-se que há um arquivo de nome \"{nome}.txt\" no diretório:")
    sleep(0.3)
    print("~sistema\\content\\src\\arquivos\\mensagens")
    sleep(0.7)

##################################################
def opcoes_RSA() -> int:
    cls()
    print("---------------------")
    print("Criptografia RSA")
    print("---------------------")
    sleep(0.5)
    print("\nO que você deseja fazer?")
    sleep(0.5)
    print("\n1) Criptografar mensagem")
    sleep(0.3)
    print("2) Criptografar arquivo")
    sleep(0.3)
    print("3) Descriptografar mensagem")
    sleep(0.3)
    print("4) Descriptografar arquivo")
    sleep(0.3)
    print("5) Gerenciar chaves públicas")
    sleep(0.3)
    print("6) Criar chaves")
    sleep(0.5)
    print("\n0) Sair")
    sleep(0.5)
    return escolha_opcoes(('0', '1', '2', '3', '4', '5', '6'))

##################################################
def RSA_cripto_msg(outros_dict: dict) -> tuple:
    cls()
    print("\nCriptografia RSA")
    print("---------------------")
    sleep(0.5)
    print("\nPara quem você quer enviar uma mensagem?")
    sleep(0.5)
    listar_nomes(outros_dict.keys())
    nome = escolha_nomes(outros_dict)
    return (int(outros_dict[nome][0]), int(outros_dict[nome][1]))

def print_criptografada(partes_cripto: list[int]):
    print("\nA mensagem criptografada é:")
    print(*partes_cripto, sep=' ')

##################################################
def RSA_cripto_arq(outros_dict: dict) -> tuple:
    cls()
    print("\nCriptografia RSA de Arquivo")
    print("---------------------")
    sleep(0.5)
    print("\nPara quem você quer enviar o arquivo?")
    sleep(0.5)
    listar_nomes(outros_dict.keys())
    nome = escolha_nomes(outros_dict)
    return (int(outros_dict[nome][0]), int(outros_dict[nome][1]))

def arq_criptografado():
    print("\nSeu arquivo foi criptografado com sucesso! Ele pode ser encontrado em:")
    sleep(0.5)
    print("~sistema\\content\\src\\arquivos\\mensagens\\cyph.txt")
    sleep(0.7)

##################################################
def RSA_decripto_msg(repete: bool) -> tuple:
    if not repete:
        cls()
        print("\nDescriptografia RSA")
        print("---------------------")
        sleep(0.5)
    print("\nInsira a mensagem cifrada:")
    cyph = input("> ")
    sleep(0.5)
    print("\nInsira sua chave privada 'd':")
    cpriv_d = int(input("> "))
    return (cyph, cpriv_d)

def print_decriptografada(msg: str):
    print("\nA mensagem descriptografada é:")
    print(msg)

##################################################
def RSA_decripto_arq(repete: bool) -> int:
    if not repete:
        cls()
        print("\nDescriptografia RSA de Arquivo")
        print("---------------------")
        sleep(0.5)
    print("\nInsira sua chave privada:")
    cpriv_d = int(input("> "))
    return cpriv_d


def arq_decriptografado():
    print("\nSeu arquivo foi descriptografado com sucesso! Ele pode ser encontrado em:")
    sleep(0.5)
    print("~sistema\\content\\src\\arquivos\\mensagens\\msg.txt")
    sleep(0.7)

##################################################
def add_chaves_nome(outros_dict: dict, cpub_n: int, cpub_e: int) -> str:
    cls()
    print("\nGerenciar chaves públicas RSA")
    print("---------------------")
    sleep(0.5)
    print("\nNo momento o sistema tem as seguintes chaves:")
    sleep(0.7)
    listar_tudo(outros_dict, cpub_n, cpub_e)
    print("\nInsira o nome da pessoa que quer adicionar/remover do sistema.")
    print("Para mudar a sua chave, insira \"Eu\":")
    nome = input("> ")
    sleep(0.5)
    return nome

def add_chaves_usuario(repete: bool) -> tuple:
    if not repete:
        print("\nInsira suas novas chaves públicas (n, e).")
        sleep(0.5)
        print("\nO sistema não vai criar uma chave privada correspondente, então\n" \
        "certifique-se de já tê-la em mãos antes de fazer isso.")
        sleep(0.5)
        print("Para cancelar a mudança, insira 0 como uma das chaves:")
        sleep(0.5)
    print("\nChave pública 'n':")
    cpub_n = int(input("> "))
    sleep(0.5)
    print("\nChave pública 'e':")
    cpub_e = int(input("> "))
    sleep(0.5)
    return (cpub_n, cpub_e)

def add_chaves_outros(repete: bool) -> tuple:
    if not repete:
        print("\nInsira as chaves públicas (n, e) dessa pessoa.")
        sleep(0.5)
        print("Para removê-la do sistema, insira 0 como uma das chaves:")
        sleep(0.5)
    print("\nChave pública 'n':")
    cout_n = int(input("> "))
    sleep(0.5)
    print("\nChave pública 'e':")
    cout_e = int(input("> "))
    sleep(0.5)
    return (cout_n, cout_e)

def atualiza_arq_usuario(cancelar: bool):
    if cancelar:
        print("\nSuas chaves públicas não foram mudadas.")
    else:
        print("\nSuas chaves públicas foram atualizadas no sistema!")
    sleep(0.7)

def atualiza_arq_outros(nome: str, achou: bool = False, remover: bool = False):
    if achou:
        if remover:
            print(f"\n{nome} e suas chaves foram removid@s do sistema.")
        else:
            print(f"\n{nome} já estava no sistema. Suas chaves públicas foram atualizadas!")
    else:
        if remover:
            print(f"\n{nome} não estava no sistema.")
        else:
            print(f"\n{nome} foi adicionad@ ao sistema e está pront@ para receber mensagens!")
    sleep(0.7)

##################################################
def criar_chaves():
    cls()
    print("\nCriar chaves RSA")
    print("---------------------")
    sleep(0.5)

def print_chaves(p: int, q: int, n: int, e: int, d: int):
    print("\nOs primos escolhidos foram:")
    sleep(0.5)
    print(f"{p} e {q}")
    sleep(0.5)
    print("\nO par de chaves públicas 'n, e' gerado foi:")
    sleep(0.5)
    print(f"{n} e {e}")
    sleep(0.5)
    print("\nA chave privada 'd' gerada foi:")
    sleep(0.5)
    print(d)
    sleep(0.7)

def mudar_ou_nao() -> int:
    print("\nDeseja mudar as próprias chaves para as novas geradas?")
    sleep(0.5)
    print("1) Mudar")
    sleep(0.3)
    print("2) Não mudar")
    sleep(0.5)
    return escolha_opcoes(('1', '2'))

def atualiza_chaves():
    print("\nSua chave pública foi atualizada no sistema! Ela pode ser encontrada em:")
    sleep(0.5)
    print("~sistema\\content\\src\\arquivos\\dados\\dados_usuario.txt")
    sleep(0.5)
    print("Sua chave privada não será salva! Guarde-a em um local seguro.")
    sleep(0.7)

def nao_atualiza_chaves():
    print("\nSuas chaves não foram alteradas.")
    sleep(0.7)

##################################################
