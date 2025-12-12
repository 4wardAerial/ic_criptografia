import random
import conversor_msg as cm
from pathlib import Path
from funcoes import alg_euclides_extendido, escolha_e

def RSA_cripto(partes_decimal: list[int], cpub_n: int, cpub_e: int) -> list[int]:
    partes_cripto = []
    for msg in partes_decimal:
        partes_cripto.append(pow(msg, cpub_e, cpub_n))
    return partes_cripto

def RSA_decripto(partes_cripto: list[int], cpriv_d: int, cpub_n: int) -> list[int]:
    partes_decripto = []
    for cyph in partes_cripto:
        partes_decripto.append(pow(cyph, cpriv_d, cpub_n))
    return partes_decripto

def calculadora_chaves_RSA(p: int, q: int):
    n: int = p * q
    phi: int = (p - 1) * (q - 1)
    e: int = escolha_e(phi)
    mdc: tuple = alg_euclides_extendido(e, phi)
    d: int = mdc[1] % phi
    return n, e, d

if __name__ == "__main__":
    DIR = Path(__file__).resolve().parent
    primos_txt = DIR / "arquivos" / "primos.txt"
    with primos_txt.open(encoding="utf-8") as ptxt:
        primos = ptxt.readlines()
        total_primos = len(primos)
        p = int(primos[random.randrange(0, total_primos, 2)])
        q = int(primos[random.randrange(1, total_primos, 2)])

    n, e, d = calculadora_chaves_RSA(p, q)

    msg_teste = "Msg bem grande essa kkkkkkk ou sera?"
    max_tam = len(str(n)) - 1
    partes_decimal = cm.converter_para_decimal(msg_teste, max_tam)
    print(partes_decimal)

    partes_cripto = RSA_cripto(partes_decimal, n, e)
    print(partes_cripto)

    partes_decripto = RSA_decripto(partes_cripto, d, n)
    print(partes_decripto)

    print(cm.converter_para_string(partes_decripto))
