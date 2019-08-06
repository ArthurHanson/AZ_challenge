#!/usr/bin/python3
"""
Challenge 3:
Given the information from the input file where the first field is the index, the second field is a reference to the
next index and the third field is the encoded value; your goal, should you choose to accept it, is to decipher the
message.

The encoded values are the hexadecimal representation of the ascii characters that make up the secret message.
The first line starts the message.  You can find the next value by looking at the reference field as it points
to the next record. The message is terminated when the next reference value is equal to '000'.

Input Sample:
001:003:48
002:000:00
003:002:69

Output Sample:
Hi
"""
import sys
import random


def usage():
	print("usage: python3 c3.py input-3.txt")
	sys.exit(1)


class AsciiCipher:
	"""Encrypts & decrypts per the instructions provided in the challenge."""
	def __init__(self):
		self.plain_text = ""
		self.cipher_text = ""

	# This function isn't required to solve the challenge. I added it to generate additional cipher texts for testing
	def encrypt(self, plain_text):
		"""Return cipher text given plain text."""
		order = [x for x in range(2, len(plain_text)+1)]
		random.shuffle(order)
		encoded = ""
		msg_dict = {
			1: (order[0], hex(ord(plain_text[0])))
		}
		for i in range(1, len(plain_text)):
			if i == len(plain_text) - 1:
				msg_dict[order[i-1]] = (0, hex(ord(plain_text[i])))
			else:
				msg_dict[order[i-1]] = (order[i], hex(ord(plain_text[i])))

		for i in sorted(msg_dict.keys()):
			encoded += str(i).zfill(3) + ":" + str(msg_dict[i][0]).zfill(3) + ":" + str(msg_dict[i][1]) + "\n"
		self.cipher_text = encoded.rstrip()
		return self.cipher_text

	# This is the only function required to solve the challenge
	def decrypt(self, cipher_text):
		"""Return plain text given cipher text."""
		msg_end = False
		decoded = ""
		idx = 0
		lines = cipher_text.splitlines()
		while not msg_end:
			line_n, next_n, code = lines[idx].split(":")
			decoded += chr(int(code, 16))
			if int(next_n) is 0:
				msg_end = True
			idx = int(next_n) - 1
		self.plain_text = decoded
		return self.plain_text


if __name__ == "__main__":
	if len(sys.argv) != 2:
		usage()

	file = sys.argv[1]
	try:
		with open(file, 'r') as f:
			text = f.read()
	except IOError:
		print("Could not read file:", file)
		sys.exit(1)

	ascii_cipher = AsciiCipher()
	print(ascii_cipher.decrypt(text))
