#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cadastro de categorias (CRUD) do projeto Finanças da Família."""
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
import mysql.connector
import repositorio_categoria as repo


TIPOS = {"R": "Receita", "D": "Despesa"}
class Aplicacao:
   def __init__(self):
       builder = Gtk.Builder()
       builder.add_from_file("categorias.glade")

       # Widgets que o código vai usar (os ids são os do Glade)
       self.janela = builder.get_object("janela")
       self.ent_nome = builder.get_object("ent_nome")
       self.cmb_tipo = builder.get_object("cmb_tipo")
       self.btn_gravar = builder.get_object("btn_gravar")
       self.btn_editar = builder.get_object("btn_editar")
       self.btn_excluir = builder.get_object("btn_excluir")
       self.lbl_mensagem = builder.get_object("lbl_mensagem")
       self.tvw_categorias = builder.get_object("tvw_categorias")
       self.lst_categorias = builder.get_object("lst_categorias")
       self.selecao = self.tvw_categorias.get_selection()

       # None = modo "nova categoria"; um número = id da categoria em edição
       self.id_em_edicao = None

       # Ligação dos sinais aos métodos (as próximas etapas acrescentam linhas aqui)
       self.janela.connect("destroy", Gtk.main_quit)
       self.carregar_tabela()
       self.janela.show_all()

   def mostrar_mensagem(self, texto):
       self.lbl_mensagem.set_text(texto)

   def carregar_tabela(self):
       """READ: busca as categorias no banco e preenche a tabela da tela."""

       self.lst_categorias.clear()
       try:
           for id_categoria, nome, tipo in repo.listar():
               self.lst_categorias.append([id_categoria, nome, TIPOS[tipo]])
       except mysql.connector.Error as erro:
           self.mostrar_mensagem(f"Erro ao acessar o banco: {erro.msg}")

if __name__ == "__main__":
   Aplicacao()
   Gtk.main()
