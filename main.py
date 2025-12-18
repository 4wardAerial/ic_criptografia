from time import sleep
from pathlib import Path
from random import randrange

from erros import CharInvalidoError
import interface as inter
import criptografador as cpt
import conversor_msg as cvm

if __name__ == "__main__":
    inter.inicio()

    DIR = Path(__file__).resolve().parent
    usuario_txt: Path = DIR / "arquivos" / "dados" / "dados_usuario.txt"
    outros_txt: Path = DIR / "arquivos" / "dados" / "dados_publicos.txt"
    msg_txt: Path = DIR / "arquivos" / "mensagens" / "msg.txt"
    cyph_txt: Path = DIR / "arquivos" / "mensagens" / "cyph.txt"
    primos_txt: Path = DIR / "arquivos" / "dados" / "primos.txt"

    sair: bool = False
    while True:
        opc_rsa: int = inter.opcoes_RSA()
        # Abre o arquivo do usuário para carregar suas chaves públicas
        with usuario_txt.open('r', encoding="utf-8") as dutxt:
            cpub_n = int(dutxt.readline())  # Lê a chave pública n do arquivo do usuário
            cpub_e = int(dutxt.readline())  # Lê a chave pública e do arquivo do usuário

        outros_dict: dict = {}
        # Abre o arquivo das chaves públicas para transformá-lo num dicionário
        with outros_txt.open('r', encoding="utf-8") as outxt:
            outros_lista: list[str] = outxt.readlines()
            # Cria dicionário a partir do arquivo
            for linha in outros_lista:
                nome, n, e = linha.split(sep=',')
                outros_dict[nome] = (n, e)
        
        if opc_rsa == 0:  # Sair
            inter.sair()
            break

        elif opc_rsa == 1:  # Criptografar msg
            cout_n, cout_e = inter.RSA_cripto_msg(outros_dict)
            repete: bool = False
            while True:
                try:
                    msg: str = inter.ler_mensagem(repete)
                    partes_decimal: list[int] = cvm.converter_para_decimal(msg, cout_n)
                    break
                except CharInvalidoError as err:
                    print(f"Caractere inválido '{err.char}'. Tente novamente.")
                    repete = True

            partes_cripto: list[int] = cpt.RSA_cripto(partes_decimal, cout_n, cout_e)
            inter.print_criptografada(partes_cripto)

        elif opc_rsa == 2:  # Criptografar arq
            if not msg_txt.exists():
                inter.arq_inexistente("msg")
            else:
                cout_n, cout_e = inter.RSA_cripto_arq(outros_dict)
                with msg_txt.open('r', encoding="utf-8") as mtxt:
                    msg_lista: list[str] = mtxt.read().splitlines()
                with cyph_txt.open('w', encoding="utf-8") as ctxt:
                    falhou: bool = False
                    partes_decimal_lista: list = []
                    for i in range(len(msg_lista)):
                        try:
                            partes_decimal_lista.append(cvm.converter_para_decimal(msg_lista[i], cout_n))  
                        except CharInvalidoError as err:
                            print(f"\nCaractere inválido '{err.char}' na linha {i + 1}.")
                            sleep(0.3)
                            print("Remova-o do arquivo e tente novamente.")
                            sleep(0.7)
                            falhou = True
                            break
                    if not falhou:
                        for j in range(len(partes_decimal_lista)):
                            cyph_linha: str = cvm.lista_int_para_string(cpt.RSA_cripto(partes_decimal_lista[j], cout_n, cout_e))
                            ctxt.write(cyph_linha)
                            ctxt.write('\n')
                        inter.arq_criptografado()
                    
        elif opc_rsa == 3:  # Descriptografar msg
            repete: bool = False
            while True:
                try:
                    cyph, cpriv_d = inter.RSA_decripto_msg(repete)  # Lê a mensagem criptografada e a chave privada
                    repete = False
                except ValueError as err:
                    print("\nSua chave privada deve conter apenas algarismos decimais.")
                    print("Tente novamente.")
                    sleep(0.7)
                    repete = True
                    continue
                try:
                    partes_cripto: list[int] = cvm.string_para_lista_int(cyph)  # Converte a mensagem numa lista de inteiros
                    partes_decripto: list[int] = cpt.RSA_decripto(partes_cripto, cpriv_d, cpub_n)  # Decripta a mensagem
                    msg: str = cvm.converter_para_string(partes_decripto)  # Reune a mensagem numa string legível
                    inter.print_decriptografada(msg)
                    break
                except ValueError as err:
                    print("\nO decriptografador espera mensagens com apenas algarismos decimais.")
                    print("Tente novamente.")
                    sleep(0.7)
                    repete = True

        elif opc_rsa == 4:  # Descriptografar arq
            if not cyph_txt.exists():
                inter.arq_inexistente("cyph")
            else:
                repete: bool = False
                while True:
                    try:
                        cpriv_d = inter.RSA_decripto_arq(repete)
                        repete = False
                        with cyph_txt.open('r', encoding="utf-8") as ctxt:
                            cyph_lista: list[str] = ctxt.read().splitlines()
                        with msg_txt.open('w', encoding="utf-8") as mtxt:
                            partes_cripto_lista: list = []
                            for i in range(len(cyph_lista)):
                                partes_cripto_lista.append(cvm.string_para_lista_int(cyph_lista[i]))
                            for j in range(len(partes_cripto_lista)):
                                msg_linha_lista: list[int] = cpt.RSA_decripto(partes_cripto_lista[j], cpriv_d, cpub_n)
                                msg_linha: str = cvm.converter_para_string(msg_linha_lista)
                                mtxt.write(msg_linha)
                                mtxt.write('\n')
                        inter.arq_decriptografado()
                        break
                    except ValueError as err:
                        print("\nSua chave privada deve conter apenas algarismos decimais.")
                        print("Tente novamente.")
                        sleep(0.7)
                        repete = True
                        continue

        elif opc_rsa == 5:  # Gerenciar chaves
            nome = inter.add_chaves_nome(outros_dict, cpub_n, cpub_e)

            repete: bool = False
            while True:
                try:
                    cout_n, cout_e = inter.add_chaves(repete)
                    repete = False
                    break
                except ValueError:
                    print("\nAs chaves públicas devem conter apenas algarismos decimais.")
                    print("Tente novamente.")
                    sleep(0.7)
                    repete = True

            remover: bool = True if (cout_n == 0 or cout_e == 0) else False 
            nova_linha: str = f"{nome},{cout_n},{cout_e}\n"
            # Abre arquivo para listar todas as linhas
            with outros_txt.open('r', encoding="utf-8") as outxt:
                linhas: list[str] = outxt.readlines()

            achou: bool = False
            for i, linha in enumerate(linhas):
                nome_ou = linha.strip().split(sep=',')[0]
                if nome == nome_ou:
                    achou = True
                    linhas[i] = "" if remover else nova_linha
                    sleep(0.7)
                    inter.atualiza_arq(nome, achou, remover)
                    break
            if not achou:
                if not remover:
                    linhas.append(nova_linha)  # Adiciona linha na lista
                sleep(0.7)
                inter.atualiza_arq(nome, achou, remover)
            # Reabre arquivo para reescrevê-lo totalmente com a lista atualizada
            with outros_txt.open('w', encoding="utf-8") as outxt:
                outxt.writelines(linhas)
            
        elif opc_rsa == 6:  # Criar chaves
            inter.criar_chaves()
            # Abre o arquivo de primos para escolher 2 entre eles
            with primos_txt.open('r', encoding="utf-8") as ptxt:
                primos = ptxt.readlines()
                total_primos = len(primos)
                p = int(primos[randrange(0, total_primos, 2)])  # Lê número primo de linha par aleatória
                q = int(primos[randrange(1, total_primos, 2)])  # Lê número primo de linha ímpar aleatória

            n, e, d = cpt.calculadora_chaves_RSA(p, q)
            inter.print_chaves(p, q, n, e, d)
            # Salva as novas chaves públicas no arquivo do usuário
            with usuario_txt.open('w', encoding="utf-8") as dutxt:
                cpub: str = f"{n}\n{e}"
                dutxt.write(cpub)
            sleep(0.7)
            inter.atualiza_chaves()


        sleep(1)
        rep: int = inter.repetir()
        sleep(1)
        if rep == 1:
            inter.voltar()
        elif rep == 2:
            inter.sair()
            break
