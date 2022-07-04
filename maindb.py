import re

from bando_de_dados.banco_db import BancoDeDados
import re

t = '(75)98874-6563'

def recebe_telefone():
    while True:
        try:
            padrao = '([0-9]{2})([0-9]{4,5})([0-9]{4})'
            telefone = input("Digite o telefone: ")
            telefone = re.search(padrao,telefone)
            telefone = f'({telefone.group(1)}){telefone.group(2)}-{telefone.group(3)}'
        except AttributeError:
            print("Telefone Inválido !\n Digite apenas DDD + Numero")
            continue
        else:
            return telefone

BancoDeDados().procura_por_telefone(recebe_telefone())