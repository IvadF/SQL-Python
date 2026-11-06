# -*- coding: utf-8 -*-
from conexao import conectar

def main():
    with conectar() as conexao:
        cursor = conexao.cursor() #é quem faz o select no SQL
        cursor.execute("SELECT VERSION(), DATABASE()")
        versao, banco = cursor.fetchone()
        print("--Select funcionou--")
        print("Versao:", versao)
        print("Banco:", banco)

if __name__ == "__main__":
    main()
