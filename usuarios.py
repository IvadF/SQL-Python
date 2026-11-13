#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import gi
gi.require_version("Gtk", "3.0")

from gi.repository import Gtk
import mysql.connector
import repositorio_usuario as repo


class Aplicacao:
    def __init__(self):
        builder = Gtk.Builder()
        builder.add_from_file("usuarios.glade")
        self.janela = builder.get_object("janela")
        self.ent_nome = builder.get_object("ent_nome")
        self.ent_login = builder.get_object("ent_login")
        self.ent_senha = builder.get_object("ent_senha")
        self.btn_gravar = builder.get_object("btn_gravar")
        self.btn_editar = builder.get_object("btn_editar")
        self.btn_excluir = builder.get_object("btn_excluir")
        self.lbl_mensagem = builder.get_object("lbl_mensagem")
        self.tvw_usuarios = builder.get_object("tvw_usuarios")
        self.lst_usuarios = builder.get_object("lst_usuarios")
        self.selecao = self.tvw_usuarios.get_selection()
        self.id_em_edicao = None
        self.janela.connect("destroy", Gtk.main_quit)
        self.carregar_tabela()

        self.btn_gravar.connect("clicked", self.ao_gravar)
        self.selecao.connect("changed", self.ao_mudar_selecao)
        self.janela.show_all()

    def mostrar_mensagem(self, texto):
        self.lbl_mensagem.set_text(texto)

    def carregar_tabela(self):
        self.lst_usuarios.clear()
        try:
            for id_usuario, nome, login in repo.listar():
                self.lst_usuarios.append([id_usuario, nome, login])
        except mysql.connector.Error as erro:
           self.mostrar_mensagem(f"Erro ao acessar o banco: {erro.msg}")

    def limpar_formulario(self):
        self.ent_nome.set_text("")
        self.ent_login.set_text("")
        self.ent_senha.set_text("")
        self.id_em_edicao = None
        self.btn_gravar.set_label("Gravar")

    def linha_selecionada(self): """

        PAREI NO PASSO 5
        """
        modelo, posicao = self.selecao.get_selected()
        if posicao is None:
            return None
        return modelo[posicao][0], modelo[posicao][1], modelo[posicao][2]

    def ao_gravar(self, componente=None, dados=None):
        nome = self.ent_nome.get_text().strip()
        login = self.ent_login.get_text().strip()
        senha = self.ent_senha.get_text()
        if not nome or not login or not senha:
            self.mostrar_mensagem("Preencha nome, login e senha.")
            return
        try:
            if self.id_em_edicao is None:
                repo.inserir(nome, login, senha)
                self.mostrar_mensagem(f"Usuário \"{login}\" gravado.")
            else:
                repo.atualizar(self.id_em_edicao, nome, login, senha)
               self.mostrar_mensagem(f"Usuário \"{login}\" alterado.")
        except mysql.connector.Error as erro:
            if erro.errno == 1062:          # violou o UNIQUE
                self.mostrar_mensagem(f"O login \"{login}\" já está em uso.")
            else:
                self.mostrar_mensagem(f"Erro ao gravar: {erro.msg}")
            return
        self.limpar_formulario()
        self.carregar_tabela()

if __name__ == "__main__":
    Aplicacao()
    Gtk.main()
