# -*- coding: utf-8 -*-
from conexao import conectar

def nome_da_funcao(parametros):
    with conectar() as conexao:            # 1. abre a conexão com o banco
        cursor = conexao.cursor()          # 2. cria o cursor
        cursor.execute(SQL, valores)       # 3. envia o comando SQL
        # 4a. consulta (SELECT): busca o resultado com fetchall() ou fetchone()
        # 4b. alteração (INSERT, UPDATE, DELETE): confirma com commit()


def listar():
   """READ: devolve uma lista de tuplas (id, nome, tipo), em ordem alfabética."""
   with conectar() as conexao:
       cursor = conexao.cursor()
       cursor.execute("SELECT id, nome, tipo FROM categoria ORDER BY nome")
       return cursor.fetchall()

def inserir(nome, tipo):
   """CREATE: grava uma nova categoria."""
   with conectar() as conexao:
       cursor = conexao.cursor()
       cursor.execute("INSERT INTO categoria (nome, tipo) VALUES (%s, %s)", (nome, tipo))
       conexao.commit()

def atualizar(id_categoria, nome, tipo):
   """UPDATE: altera o nome e o tipo da categoria com esse id."""
   with conectar() as conexao:
       cursor = conexao.cursor()
       cursor.execute("UPDATE categoria SET nome = %s, tipo = %s WHERE id = %s", (nome, tipo, id_categoria))
       conexao.commit()

def excluir(id_categoria):
   """DELETE: apaga a categoria com esse id."""
   with conectar() as conexao:
       cursor = conexao.cursor()
       cursor.execute("DELETE FROM categoria WHERE id = %s", (id_categoria,))
       conexao.commit()
