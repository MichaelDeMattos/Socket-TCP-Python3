#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

def receber_dados(host = 'localhost', port=8082):
	data_payload = 2048 # --> maximo de dados retornados por um cliente
	# -- Constroi o socket TCP
	sock = socket.socket(socket.AF_INET,  socket.SOCK_STREAM)
	# -- Habilita o reuso da porta no host especificado
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	# Endereço do servidor 
	servidor = (host, port)
	print ("Servidor iniciado! %s porta %s" % servidor)
	sock.bind(servidor)
	# Define a quantidade maxima de clientes conectados
	sock.listen(5) 
	i = 0
	while True: 
		print ("Pronto para receber dados do cliente!!!")
		client, address = sock.accept() 
		recebido = client.recv(data_payload)
		print(recebido.decode("UTF-8"))
		client.send(recebido)
		if i != 0: break

if __name__ == '__main__':
	receber_dados()
