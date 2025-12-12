from erros import CharInvalidoError

'''
Dicionário com valor decimal de cada caractere que poderá ser usado nas mensagens.
'''
tabela_char = {
    'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15, 'g': 16, 'h': 17,
    'i': 18, 'j': 19, 'k': 20, 'l': 21, 'm': 22, 'n': 23, 'o': 24, 'p': 25,
    'q': 26, 'r': 27, 's': 28, 't': 29, 'u': 30, 'v': 31, 'w': 32, 'x': 33,
    'y': 34, 'z': 35,

    'A': 36, 'B': 37, 'C': 38, 'D': 39, 'E': 40, 'F': 41, 'G': 42, 'H': 43,
    'I': 44, 'J': 45, 'K': 46, 'L': 47, 'M': 48, 'N': 49, 'O': 50, 'P': 51,
    'Q': 52, 'R': 53, 'S': 54, 'T': 55, 'U': 56, 'V': 57, 'W': 58, 'X': 59,
    'Y': 60, 'Z': 61,

    ',': 62, '.': 63, '!': 64, '?': 65, ' ': 66
}

'''
Dicionário inverso, com o valor de cada caractere para cada valor decimal que poderá
ser usado nas mensagens criptografadas.
'''
tabela_int = {valor_decimal: valor_char for valor_char, valor_decimal in tabela_char.items()}

'''
Baseado nas tabelas de conversão, transforma uma mensagem no número inteiro decimal
correspondente. No processo, divide a string em pedaços menores de acordo com um
tamanho máximo (definido por n = pq) e barra caracteres inválidos.
'''
def converter_para_decimal(msg: str):
    partes_string = [""]

    cont_tam = 0
    max_tam = 10
    i = 0
    for c in msg:
        if c not in tabela_char:
            raise CharInvalidoError(c)
        if cont_tam >= max_tam:
            partes_string.append("")
            i += 1
            cont_tam = 0
        partes_string[i] += str(tabela_char.get(c))
        cont_tam += 2

    partes_decimal = [int(ps) for ps in partes_string]
    return partes_decimal


if __name__ == "__main__":
    msg_teste = "Bacana ba1a1a"
    print(converter_para_decimal(msg_teste))
