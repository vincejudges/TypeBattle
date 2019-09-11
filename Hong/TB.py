import pygame
import sys
import random
import time
from threading import Thread
from Game_status import *
import socket
from network import Network


screen = pygame.display.set_mode((800, 600), 0, 0)
# back = pygame.image.load("bk.jpg")
word = []
chars = []
nowpos = 0
score = 0
lines = []
start_time = 0
game_began = Game_status.NOT_START
speed = 0
font_type = "LiberationMono-Regular.ttf"
threads = []
ready_time = -1
network = Network()


def init():
	global lines
	pygame.init()
	pygame.display.set_caption("TypeBattle!")
	file = open('file.txt', 'r')
	lines = file.readlines()
	for str in lines:
		for ch in str:
			if ch != '\n':
				word.append(ord(ch))
			chars.append(ch)

def loop():
	bg_color = (230, 155, 155)
	while True:
		# screen.blit(back, (0, 0))
		screen.fill(bg_color)
		action()
		pygame.time.delay(1)
		pygame.display.update()

def action():
	global score
	global nowpos
	global word
	global start_time
	global game_began
	global ready_time
	global network
	printWords()
	if game_began == Game_status.NOT_START:
		status = network.try_recv(0.5)
		if (status is not None and status == "BEGIN"):
			game_began = Game_status.READY
		else:
			printGameStatus("Please wait for other player...")
		return
	if game_began == Game_status.END:
		printGameStatus("Game over")
		pygame.time.delay(5000)
		sys.exit()
	if game_began == Game_status.READY:
		if ready_time == -1:	
			ready_time = time.time()
		else :
			delta = 5 - (time.time() - ready_time)
			printGameStatus("GET READY! START IN {:.2f} second". format(delta))
			if (delta <= 0):
				game_began = Game_status.RUNNING
				start_time = time.time()
		return 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			# if nowpos == 0:
			# 	start_time = time.time()
			if nowpos == len(word):
				print("Goooooooooood!")
				continue
			if event.unicode == chr(word[nowpos]):
				score += 1
				nowpos += 1
				if (send_to_server(network) == "END"):
					game_began = Game_status.END
			if nowpos == len(word):
				send_to_server(network, finished=True)
				game_began = Game_status.END
	printScore()

# TO DO
def send_to_server(network, finished=False):
	if (finished) :
		network.report("FIN")
	else:
		return network.report("{},{}".format(nowpos, speed))

def printGameStatus(status_str):
	font = pygame.font.Font(font_type, 24)
	screen.blit(font.render(status_str, True, (255, 0, 0)), (80, 40))

def printScore():
	global speed
	# pygame.font.init()
	font = pygame.font.Font(font_type, 16)
	deg = score * 100.0 / len(word)
	now_time = time.time()
	if nowpos != len(word):
		speed = score / max((now_time - start_time), 1)
	scoreShow = font.render("Degree of completion: %.2f %%" % deg, True, (255, 0, 0))
	speedShow = font.render("Speed: %.2f" % speed, True, (255, 0, 0))
	screen.blit(scoreShow, (20, 20))
	screen.blit(speedShow, (20, 40))

def printWords():
	global chars
	global nowpos
	global font_type
	L = 60
	T = 60
	pos = 0
	for ii in range(0, nowpos):
		while chars[pos] == '\n':
			L = L + 20
			T = 60 
			pos += 1
		pygame.font.init()
		font = pygame.font.Font(font_type, 16)
		if chars[pos] == ' ':
			strShow = font.render("_", True, (0, 0, 255))
		else:
			strShow = font.render("%s" % chars[pos], True, (0, 0, 255))
		pos += 1
		screen.blit(strShow, (T, L))
		T = T + 12
	while pos < len(chars):
		while chars[pos] == '\n':
			L = L + 20
			T = 60
			pos += 1
		pygame.font.init()
		font = pygame.font.Font(font_type, 16)
		strShow = font.render("%s" % chars[pos], True, (0, 0, 0))
		pos += 1
		screen.blit(strShow, (T, L))
		T = T + 12

if __name__ == '__main__':
	init()
	loop()

	