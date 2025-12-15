from time import sleep
from pathlib import Path
from random import randrange

import interface as inter
import criptografador as cpt
import conversor_msg as cvm

if __name__ == "__main__":
    inter.inicio()
    sleep(2)

    while(True):
        tipo_c: int = inter.tipo_de_cripto()
        sleep(1)

        if tipo_c == 1:  # RSA
            opc_rsa: int = inter.opcoes_RSA()
            # Abre o arquivo do usuário para carregar suas chaves públicas
            DIR = Path(__file__).resolve().parent
            usuario_txt = DIR / "arquivos" / "dados_usuario.txt"
            with usuario_txt.open(encoding="utf-8") as dutxt:
                cpub_n = int(dutxt.readlines()[0])  # Lê a chave pública n do arquivo do usuário
                cpub_e = int(dutxt.readlines()[1])  # Lê a chave pública e do arquivo do usuário

            if opc_rsa == 1:  # Criptografar msg
                inter.RSA_cripto()

            elif opc_rsa == 2:  # Descriptografar msg
                cyph, cpriv_d = inter.RSA_decripto()  # Lê a mensagem criptografada e a chave privada
                partes_cripto: list[int] = cvm.string_para_lista_int(cyph)  # Converte a mensagem numa lista de inteiros
                partes_decripto: list[int] = cpt.RSA_decripto(partes_cripto, cpriv_d, cpub_n)  # Decripta a mensagem
                msg: str = cvm.converter_para_string(partes_decripto)  # Reune a mensagem numa string legível
                inter.print_decriptografada(msg)

            elif opc_rsa == 3:  # Criar chaves
                inter.criar_chaves()
                # Abre o arquivo de primos para escolher 2 entre eles
                DIR = Path(__file__).resolve().parent
                primos_txt = DIR / "arquivos" / "primos.txt"
                with primos_txt.open(encoding="utf-8") as ptxt:
                    primos = ptxt.readlines()
                    total_primos = len(primos)
                    p = int(primos[randrange(0, total_primos, 2)])  # Lê número primo de linha par aleatória
                    q = int(primos[randrange(1, total_primos, 2)])  # Lê número primo de linha ímpar aleatória

                n, e, d = cpt.calculadora_chaves_RSA(p, q)
                inter.print_chaves(p, q, n, e, d)
                # Salva as novas chaves públicas no arquivo do usuário
                DIR = Path(__file__).resolve().parent
                usuario_txt = DIR / "arquivos" / "dados_usuario.txt"

            elif opc_rsa == 4:  # Add chaves
                pass


        '''
        elif tipo_c == 2:  # ElGamal
            if c_ou_d == 1:
                pass
            elif c_ou_d == 2:
                pass

        elif tipo_c == 3:  # Polinomial
            if c_ou_d == 1:
                pass
            elif c_ou_d == 2:
                pass
        '''
        
        rep: int = inter.repetir()
        if rep == 1:
            inter.voltar()
            continue
        elif rep == 2:
            inter.sair()
            break
