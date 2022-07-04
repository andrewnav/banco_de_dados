from os import mkdir

try:
    mkdir('./bando_de_dados/armazenamento')
except FileExistsError:
    pass

try:
    arquivo = open('./bando_de_dados/armazenamento/banco.db')
except FileNotFoundError:
    arquivo = open('./bando_de_dados/armazenamento/banco.db', 'w+')
finally:
    arquivo.close()
