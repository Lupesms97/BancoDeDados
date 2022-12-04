import sqlite3
from time import sleep
from tkinter import *


class Funcionalidades():
    
    def __init__(self, arquivo):
        self.conn = sqlite3.connect(arquivo)
        self.cursor = self.conn.cursor()

    def inserir(self, nome, cpf, valorComprado, dataCompra):
        consulta = 'INSERT OR IGNORE INTO bancoDeDadosClientes (nome, cpf) VALUES (?, ?)'
        self.cursor.execute(consulta, (nome, cpf))
        self.conn.commit()

    def editar(self, nome, cpf, id):
        consulta = 'UPDATE OR IGNORE bancoDeDadosClientes SET nome=?, cpf=? WHERE id=?'
        self.cursor.execute(consulta, (nome, cpf, id))
        self.conn.commit()

    def excluir(self, id):
        consulta = 'DELETE FROM bancoDeDadosClientes WHERE id=?'
        self.cursor.execute(consulta, (id,))
        self.conn.commit()

    def listar(self):
        self.cursor.execute('SELECT * FROM bancoDeDadosClientes')

        for linha in self.cursor.fetchall():
            print(linha)

    def buscar(self, valor):
        consulta = 'SELECT * FROM bancoDeDadosClientes WHERE nome LIKE ?'
        self.cursor.execute(consulta, (f'%{valor}%', ))

        for linha in self.cursor.fetchall():
            print(linha)


    def fechar(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    agenda = Funcionalidades('bancoDeDadosClientes.sqlite3')

    encerrar = False
    while not encerrar:
        print('Bem vindo ao seu sistema de cadastro de clientes')
        sleep(2)
        print('Vamos iniciar seu programa, lembrando sempore que cada CPF é único')
        sleep(2)
        choice = int(input('Oque você desejar fazer ?'
        '\n[1] Inserir novo cliente'
        '\n[2] Exibir lista'
        '\n[3] Buscar por nome'
        '\n[4]] Excluir '
        '\n[5] Editar'
        '\n[6] encerrar'
        '\nResposta: '
        ))
        encerrar1 = False

        if choice == 1:
            while not encerrar1:
                nome = str(input('Digite o nome que você deseja cadastrar: ')).upper()
                cpf = int(input('Digite o CPF do cliente que você desja adicionar: '))
                quantidadeDigitosCpf = len(str(cpf))
                if quantidadeDigitosCpf != 11:
                        print('Você digitou um CPF invalido')
                        print('Quantidade errada')
                else:
                    print('Tem os 11')
                    agenda.inserir(nome, cpf)
                    break

        elif choice ==  3:
            nomeBusca = str(input('Digite o nome que você deseja buscar: '))
            agenda.buscar(nomeBusca)

        elif choice ==  2:
            agenda.listar()

        elif choice ==  4:
            identidadeID = int(input('Digite a ID do cliente que deseja excluir:   '))
            decidirSim = int(input('A exlusão é permanente e não tem volta, tem certeza que deseja fazer a exclusão?\n'
            '[1] sim  ou  [2] não   '))
            if decidirSim == 1:
                agenda.excluir(identidadeID,)
            elif decidirSim == 2:
                print('Exclusão cancelada')
                continue
            else:
                print('Sua resposta não foi valida')

        elif choice ==  5:
            identidadeID = int(input('Digite a ID do cliente que você deseja alterar: '))
            nome = str(input('Digite o nome para que seja substituido na id: ')).upper()
            cpf = int(input('Digite o CPF agora: '))
            agenda.editar(nome, cpf , identidadeID)

        elif choice == 6:
            encerrar = True

    print('Estamos encerrando seu programa')
    print('3')
    sleep(1)
    print('2')
    sleep(1)
    print('1')
    print('Programa encerrado')

