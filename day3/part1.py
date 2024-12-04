import re


def main(file):
	total = 0
	lines = file.read().splitlines()
	for line in lines:
		matches = re.findall(r"mul\((\d+),(\d+)\)", line)
		for match in matches:
			total += int(match[0]) * int(match[1])
	print(total)
