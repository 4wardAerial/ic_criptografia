from random import randrange

'''
Calcula o MDC entre dois números pelo método de euclides das divisões
sucessivas e os valores de m e n tais que MDC(a, b) = ma + nb.
'''
def alg_euclides_extendido(a: int, b: int) -> tuple:
    m1, n1 = 1, 0
    m2, n2 = 0, 1

    while b:
        q = a // b
        r = a % b

        a = b
        b = r
        m1, m2 = m2, m1 - q * m2
        n1, n2 = n2, n1 - q * n2

    return (a, m1, n1)

'''
Gera um valor para e, 1 < e < phi(n), coprimo com o totiente (phi(n)) para
ser usado no RSA.
'''
def escolha_e(phi: int) -> int:
    e = 65537  # Aparentemente esse é um valor comum para e
    if alg_euclides_extendido(e, phi)[0] == 1:
        return e
    # Se aquele e não funcionar, escolhe outro não tão grande
    while True:
        e = randrange(3, 2**32, 2)
        if alg_euclides_extendido(e, phi)[0] == 1:
            return e