#!/usr/bin/python3
from engine import character
from protocol import reliability

class Player(object):
	def __init__(self, ip, port, nickname):
		self.ip = ip
		self.port = port
		self.nickname = nickname
		self.remote_seq = reliability.remote_seq()

		self.character = character.Character(30, 348)
