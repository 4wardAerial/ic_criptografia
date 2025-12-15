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

    '0': 62, '1': 63, '2': 64, '3': 65, '4': 66, '5': 67, '6': 68, '7': 69,
    '8': 70, '9': 71,

    ',': 72, '.': 73, '!': 74, '?': 75, ' ': 76
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
def converter_para_decimal(msg: str, n: int) -> list[int]:
    # Como todo char está entre 10 e 66, todos tem 2 algarimos, então o tamanho 
    # máximo de cada partição da string tem que se, em chars, metade da qntd. 
    # de algarimos
    max_chars = (len(str(n)) - 1) // 2
    decimais = []
    parte_decimal = ""

    for c in msg:
        if c not in tabela_char:
            raise CharInvalidoError(c)  # Barra caracter inválido
        
        # Transforma o caractere numa string do inteiro correspondente
        valor_char = f"{tabela_char[c]:02d}"

        # Se adicionar o inteiro exceder o maximo de caracteres, 
        # particiona a string
        if len(parte_decimal) + 2 > 2 * max_chars:
            decimais.append(int(parte_decimal))
            parte_decimal = ""
        
        parte_decimal += valor_char
    
    # Inclui a ultima parte
    if parte_decimal:
        decimais.append(int(parte_decimal))
    return decimais

'''
Baseado na tabela inversa de conversão, transforma uma lista de inteiros decimais
numa única string correspondente. Caso encontre um valor sem char relacionado, 
printa um '#' no lugar.  
'''
def converter_para_string(partes_decimal: list[int]) -> str:
    string = ""

    for dec in partes_decimal:
        dec_str = str(dec)

        # Garante qntd par de caracteres 
        if len(dec_str) % 2 != 0:
            dec_str = "0" + dec_str
        
        for i in range(0, len(dec_str), 2):
            valor_int = int(dec_str[i:i+2])  # Pega caracteres 2 a 2
            if valor_int not in tabela_int:
                string += '#'
            else:
                string += str(tabela_int.get(valor_int))

    return string

'''
Transforma uma string de números separados por espaços em uma lista de inteiros
'''
def string_para_lista_int(msg: str) -> list[int]:
    partes_int = [int(m) for m in msg.split()]
    return partes_int


def lista_int_para_string(lista: list[int]) -> str:
    msg = ""
    for i in lista:
        msg += str(i) + ' '
    return msg