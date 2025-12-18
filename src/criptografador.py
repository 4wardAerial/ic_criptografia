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
    print(calculadora_chaves_RSA(9167720013620060891, 12192536085444167230027))
