import pygame
import sys
import random

screen = pygame.display.set_mode((800, 600), 0, 0)
# back = pygame.image.load("bk.jpg")
word = []
chars = []
nowpos = 0
score = 0
lines = []

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
	bg_color = (230, 230, 230)
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
	printWords()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if nowpos == len(word):
				print("Goooooooooood!")
				continue
			if event.unicode == chr(word[nowpos]):
				score += 1
				nowpos += 1
				send_to_server()
	printScore()

def send_to_server():
	print("Gao!")

def printScore():
	pygame.font.init()
	font = pygame.font.Font("LiberationMono-Regular.ttf", 16)
	scoreShow = font.render("score:%s" % score, True, (255, 0, 0))
	screen.blit(scoreShow, (20, 20))

def printWords():
	global chars
	global nowpos
	L = 60
	T = 60
	pos = 0
	for ii in range(0, nowpos):
		while chars[pos] == '\n':
			L = L + 20
			T = 60
			pos += 1
		pygame.font.init()
		font = pygame.font.Font("LiberationMono-Regular.ttf", 16)
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
		font = pygame.font.Font("LiberationMono-Regular.ttf", 16)
		strShow = font.render("%s" % chars[pos], True, (0, 0, 0))
		pos += 1
		screen.blit(strShow, (T, L))
		T = T + 12

if __name__ == '__main__':
	init()
	loop()
