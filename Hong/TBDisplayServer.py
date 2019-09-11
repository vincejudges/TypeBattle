import pygame 
import sys
import time
from threading import Thread
import socket
from network import Network

screen = pygame.display.set_mode((800, 600), 0, 0)

lines = []
word = []
chars = []
Apos = 0
Bpos = 0
font_type = "LiberationMono-Regular.ttf"
network = Network()

def init():
	global lines
	pygame.init()
	pygame.display.set_caption("TypeBattle!")
	file = open('file.txt', 'r')
	lines = file.readlines()
	for s in lines:
		for ch in s:
			if ch != '\n':
				word.append(ord(ch))
			chars.append(ch)

def loop():
    bg_color = (155,230,155)
    while True:
        screen.fill(bg_color)
        action()
        pygame.time.delay(100)
        pygame.display.update()

def action():
    global network
    printWords()
    status = network.report("REQ")
    if (status is not None):
        a, b = status.split(',')
        Apos = max(Apos, int(a))
        Bpos = max(Bpos, int(b))


def printWords():
    global chars
    global Apos, Bpos
    global font_type
    L = 60
    T = 60
    pos = 0
    mxpos = max(Apos, Bpos)
    mnpos = min(Apos, Bpos)
    for ii in range(len(chars)):
        while chars[pos] == '\n':
            L += 20
            T = 60
            pos += 1 
        pygame.font.init()
        font = pygame.font.Font(font_type, 16)
        color = (0, 0, 0)
        if pos <= mnpos:
            color = (255, 0, 255)
        elif (pos <= mxpos):
            color = (0, 0, 255) if Apos > Bpos else (255, 0, 0)
        else:
            color = (0, 0, 0)
        if chars[pos] == ' ':
            strshow = font.render("_", True, color)
        else:
            strshow = font.render("%s"%chars[pos], True, color)
        pos += 1
        screen.blit(strshow, (T, L))
        T = T + 12