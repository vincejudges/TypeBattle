import socket
import sys


class Network:
	def __init__(self):
		self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # host and port of the server
		self.host = "localhost"
		self.port = 5295
		self.connect()
	
	def connect(self):
		if (len(sys.argv) < 2) :
			print("Please input player name as argv, e.g. python TB.py player1")
			sys.exit()
		try:
			self.client.connect((self.host, self.port))
		except:
			print("Cannot connect to the server {}.".format((self.host, self.port)))
			sys.exit()
		self.client.send(str.encode(sys.argv[1]))
	
	def report(self, data):
		try:
			self.client.send(str.encode(data))
			result = self.client.recv(2048).decode("utf-8")
			return result
		except Exception as e:
			print(e)

	def try_recv(self):
		self.client.settimeout(0.5)
		result = None
		try:
			result = self.client.recv(2048).decode("utf-8")
			self.client.send(str.encode("RECV"))
		except socket.timeout:
			pass
		finally:
			self.client.settimeout(None)
		return result
			