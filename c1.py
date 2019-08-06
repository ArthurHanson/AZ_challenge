#!/usr/bin/python3
"""
Challenge 1:
Write a program that finds the consecutive number ranges within in a sequence of integers.
Consecutive numbers are integer numbers one after the other.

The program must accept as its first argument a path to an input filename.
Each line in this input file contains sequence of integers separated by whitespace.

Input Sample:
1 2 3 4 7 8 9 11 13
1 2 3 5 6 7 9 10 11 12
1 3 5 6 7 9 11 12 13

Output Sample:
1-4 7-9
1-3 5-7 9-12
5-7 11-13
"""
import sys


def usage():
	print("usage: python c1.py input-1.txt")
	sys.exit(1)


def sequence_finder(line: str) -> str:
	"""Returns a string denoting consecutive number ranges given a sequence of integers as a string."""
	results = []
	values = list(map(int, line.strip().split()))  # cast to int and split on default " "
	last = values[0]
	start = last
	for i in range(1, len(values)):
		if values[i] != last + 1:
			# detected break in sequence
			if last - start > 0:
				results.append((start, last))
			# restart next sequence
			start = values[i]
			last = start
		else:
			# add to current sequence
			last = values[i]
	# evaluate last value
	if last - start > 0:
		results.append((start, last))
	str_out = ""
	space = ""
	for result in results:
		str_out += space + str(result[0]) + "-" + str(result[1])
		space = " "
	return str_out

if __name__ == "__main__":
	if len(sys.argv) != 2:
		usage()

	file = sys.argv[1]
	try:
		with open(file, 'r') as f:
			lines = f.readlines()
	except IOError:
		print("Could not read file:", file)
		sys.exit(1)

	for line in lines:
		print(sequence_finder(line))
