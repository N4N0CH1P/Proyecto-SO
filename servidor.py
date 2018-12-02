#!/usr/bin/env python
# -*- coding: utf-8 -*-
#This sample program, based on the one in the standard library documentation, receives incoming messages and echos them back to the sender. It starts by creating a TCP/IP socket.

import socket
import sys
import time
# CREATE OBJECT PROCESO
class Proceso:
    pid = 0
    marcoPagina = 0
    paginaProceso = 0
    pageSize = 0
    counter = 0

    def _init_(self,pid,pageSize):
        self.pageSize = pageSize
        self.pid = pid


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Then bind() is used to associate the socket with the server address. In this case, the address is localhost, referring to the current server, and the port number is 10000.

# Bind the socket to the port
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

#Calling listen() puts the socket into server mode, and accept() waits for an incoming connection.

# Listen for incoming connections
sock.listen(1)


# Wait for a connection
print >>sys.stderr, 'waiting for a connection'
connection, client_address = sock.accept()

#accept() returns an open connection between the server and client, along with the address of the client. The connection is actually a different socket on another port (assigned by the kernel). Data is read from the connection with recv() and transmitted with sendall().

try:
	print >>sys.stderr, 'connection from', client_address
    memReal = [] #AQUI SE ALMACENAN LOS PROCESOS QUE ESTAN EN MEMORIA REAL
    colaListos = [] #AQUIE SE ALMACENAN LOS PROCESOS QUE ESTAN EN LA COLA DE LISTOS
    procesosCreados = [] #AQUI SE ALMACENAN LOS PROCESOS QUE YA SE CREARON PARA PODER BUSCARLOS EN BASE A SUS PID
    cont = 0 #CONTADOR PARA SABER EL NUMERO DEL ULTIMO PROCESO QUE HAY EN EL SIMULADOR
    cpu = -1 #ESTA VARIABLE ALMACENA EL VALOR DEL PID DEL PROCESO QUE ESTA EN LA CPU
    realAddress = 0#DIRECCION DE MEMORIA EN LA CUAL ESTA ALMACENADO UN PROCESO
	while True:
		data = connection.recv(256)
		print >>sys.stderr, 'server received "%s"' % data
        command = data.split() #SE DECLARA UNA VARIABLE QUE DIVIDE EL COMANDO
        #AQUI SE EVALUAN LOS COMANDOS AL EJECUTARSE
        if ( command[0] == 'QuantumV'):
            quantumV = command[1]
        elif ( command[0] == 'RealMemory'):
            realMemory = command[1]
        elif ( command[0]) == 'SwapMemory' ):
            swapMemory = command[1];
        elif ( command [0] == 'PageSize'):
            pageSize = pageSize
        else:
            if(command[0] == "Create"):
                proceso = Proceso(cont,command[1]/pageSize);
                procesosCreados.append(proceso)
                if(memReal == []):
                    memReal.append(proceso)
                else:
                    colaListos.append(proceso)
		if data:
			print >>sys.stderr, 'sending answer back to the client'

			connection.sendall('process created')
		else:
			print >>sys.stderr, 'no data from', client_address
			connection.close()
			sys.exit()

finally:
     # Clean up the connection
	print >>sys.stderr, 'se fue al finally'
	connection.close()

#When communication with a client is finished, the connection needs to be cleaned up using close(). This example uses a try:finally block to ensure that close() is always called, even in the event of an error.


def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
