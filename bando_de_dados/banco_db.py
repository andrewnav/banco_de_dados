import sqlite3


class BancoDeDados:
    __CRIAR_AGENDA = """
    CREATE TABLE agenda
    (
        id INTEGER PRIMARY KEY ASC,
        nome TEXT,
        numero_telefone TEXT       
    )"""
    __ESCREVER_AGENDA = """
    INSERT INTO agenda (nome, numero_telefone)
        VALUES (?,?)"""
    __MOSTRAR_AGENDA = """
    SELECT *
        FROM agenda
        ORDER BY nome"""
    __PROCURAR_POR_NOME = """
    SELECT *
        FROM agenda
        WHERE nome=(?)"""
    __PROCURAR_POR_TELEFONE = """
    SELECT *
        FROM agenda
        WHERE numero_telefone=(?)"""

    def __init__(self):
        self.__banco = sqlite3.connect('./bando_de_dados/armazenamento/banco.db')
        self.__cursor = self.__banco.cursor()

    def criar_tabela(self):
        try:
            self.__cursor.execute(self.__CRIAR_AGENDA)
            self.__banco.commit()
        except sqlite3.Error as erro:
            print(erro)
        finally:
            self.__banco.close()

    def escrever_agenda(self, dados: tuple):
        try:
            self.__cursor.execute(self.__ESCREVER_AGENDA, dados)
            self.__banco.commit()
        except sqlite3.Error as erro:
            print(erro)
        finally:
            self.__banco.close()

    def mostrar_agenda(self):
        try:
            self.__cursor.execute(self.__MOSTRAR_AGENDA)
            print(f"{'Nome':^25} - {'Telefone':^25}")
            for x in self.__cursor.fetchall():
                print(f"{x[1]:^25}  {x[2]:^25}")
        except sqlite3.Error as erro:
            print(erro)
        finally:
            self.__banco.close()


    def procura_por_nome(self, nome):
        try:
            self.__cursor.execute(self.__PROCURAR_POR_NOME, (nome,))
            print(f"{'Nome':^25} - {'Telefone':^25}")
            for x in self.__cursor.fetchall():
                print(f"{x[1]:^25}  {x[2]:^25}")
        except sqlite3.Error as erro:
            print(erro)
        finally:
            self.__banco.close()

    def procura_por_telefone(self, telefone):
        try:
            self.__cursor.execute(self.__PROCURAR_POR_TELEFONE, (telefone,))
            print(f"{'Nome':^25} - {'Telefone':^25}")
            for x in self.__cursor.fetchall():
                print(f"{x[1]:^25}  {x[2]:^25}")
        except sqlite3.Error as erro:
            print(erro)
        finally:
            self.__banco.close()





