import csv
import time
from pathlib import Path
from criptografador import *

DIR = Path(__file__).resolve().parent
csv_path = DIR / "arquivos" / "usuarios.csv"

def carregar_usuarios():
    with csv_path.open(encoding="utf-8") as f:
        reader = csv.DictReader(f)
        return {linha["nome"]: linha for linha in reader}

def cadastro(nome: str):
    pass
        

def login():
    pass

login()



