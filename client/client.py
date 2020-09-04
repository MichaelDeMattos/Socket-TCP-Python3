#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import time

def enviar_dados(host = 'localhost', port=8082):
	# -- Constroi o socket TCP
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	
	# --> Realiza a conexão com o servidor
	try:	
		servidor = (host, port) 
		print("Conectado: %s porta: %s" % (host, port))
		sock.connect(servidor)
		 
	except socket.error as e:
		print("Erro ao realizar conexão com o servidor\n"
			  "Consulte os detalhes do erro: %s" % (str(e)))
		exit()
		
	# --> Envio de dados 
	try:
		while True: 
			msg = input("Texto a ser enviado ao servidor: ")				
			print("Processando informações!!!")
			time.sleep(1)
			print("Enviando informações ao servidor")
			time.sleep(1)
			
			if msg == "":
				sock.sendall("VALOR NULL".encode('utf-8'))
			else:
				sock.sendall(msg.encode('utf-8'))
			
			retorno = sock.recv(100) # --> retorno do servidor
			print("Aguardando resposta...")
			time.sleep(0.5)
			print("\n")
			print(retorno.decode("UTF-8"))
			return enviar_dados() # --> retorna ao início da execução
	except socket.error as e: 
		print("Socket error: %s" %str(e))

if __name__ == '__main__':
	enviar_dados()
