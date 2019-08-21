import pygame, sys, random

screen = pygame.display.set_mode((800, 600), 0, 0)
back = pygame.image.load("bk.jpg")
word = []
nowpos = 0
score = 0

def init():
	pygame.init()
	pygame.display.set_caption("TypeBattle!")
	file = open('file.txt', 'r')
	lines = file.readlines()
	for str in lines:
		for ch in str:
			if ch != '\n':
				word.append(ord(ch))


def loop():
	while True:
		screen.blit(back, (0, 0))
		action()
		pygame.time.delay(1)
		pygame.display.update()

def action():
	global score
	global nowpos
	global word
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if nowpos == len(word) - 1:
				print("Goooooooooood!")
				continue
			if event.key == word[nowpos]:
				score += 1
				nowpos += 1
	printScore()
	
def printScore():
	pygame.font.init()
	font = pygame.font.Font("tahomabd.ttf", 16)
	scoreShow = font.render("score:%s"%score,True,(255,0,0))
	screen.blit(scoreShow, (20,20))


if __name__ == '__main__':
	init()
	loop()