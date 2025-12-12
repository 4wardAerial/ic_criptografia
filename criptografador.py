import conversor_msg as cm
from erros import CharInvalidoError


while(True):
    msg = input("Qual mensagem: ")
    
    try:
        lista_dec = cm.converter_para_decimal(msg)
        print(lista_dec)
        print("Obrigado por usar nossos sistemas\n")
        break
    except CharInvalidoError as err:
        print(f"Caractere inválido: {err.char}. Tente novamente.\n")