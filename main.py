from time import sleep
from pathlib import Path

import interface as inter
import criptografador as cpt
import conversor_msg as cvm

if __name__ == "__main__":
    inter.inicio()
    sleep(2)

    while(True):
        tipo_c: int = inter.tipo_de_cripto()
        sleep(1)
        c_ou_d: int = inter.critpo_ou_decripto()

        if tipo_c == 1:  # RSA
            DIR = Path(__file__).resolve().parent
            primos_txt = DIR / "arquivos" / "dados_usuario.txt"
            with primos_txt.open(encoding="utf-8") as dutxt:
                cpub_n = int(dutxt.readlines()[0])

            if c_ou_d == 1:
                inter.RSA_cripto()
            elif c_ou_d == 2:
                cyph, cpriv_d = inter.RSA_decripto()  # Lê a mensagem criptografada e a chave privada
                partes_cripto: list[int] = cvm.string_para_lista_int(cyph)  # Converte a mensagem numa lista de inteiros
                partes_decripto: list[int] = cpt.RSA_decripto(partes_cripto, cpriv_d, cpub_n)  # Decripta a mensagem
                msg: str = cvm.converter_para_string(partes_decripto)  # Reune a mensagem numa string legível
                inter.print_decriptografada(msg)

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
        
        rep: int = inter.repetir()
        if rep == 1:
            inter.voltar()
            continue
        elif rep == 2:
            inter.sair()
            break
