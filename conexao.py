# -*- coding: utf-8 -*-
import mysql.connector
import certifi
import configparser


def conectar():
    cfg = configparser.ConfigParser()
    cfg.read("config.ini", encoding="utf-8")

    banco = cfg["banco"]
    return mysql.connector.connect(
        host = banco["host"],
        user = banco["usuario"],
        password = banco["senha"],
        port = banco["porta"],
        database = banco["nome"],
        ssl_ca = certifi.where(),
        ssl_verify_cert = True,
        ssl_verify_identity = True,
    )
