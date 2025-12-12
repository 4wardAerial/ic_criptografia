import conversor_msg as cm
from erros import CharInvalidoError


def RSA_cripto(partes_decimal: list[int], cpub_n: int, cpub_e: int) -> list[int]:
    partes_cripto = []
    for msg in partes_decimal:
        partes_cripto.append(pow(msg, cpub_e, cpub_n))
    return partes_cripto

def RSA_decripto(partes_cripto: list[int], cpriv_d: int, cpub_n: int) -> list[int]:
    partes_decripto = []
    for cyp in partes_cripto:
        partes_decripto.append(pow(cyp, cpriv_d, cpub_n))
    return partes_decripto

if __name__ == "__main__":
    while(True):
        msg = input("Qual mensagem: ")
        
        try:
            lista_dec = cm.converter_para_decimal(msg, 10)
            
            print("Obrigado por usar nossos sistemas\n")
            break
        except CharInvalidoError as err:
            print(f"Caractere inválido: {err.char}. Tente novamente.\n")