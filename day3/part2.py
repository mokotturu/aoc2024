import re


def main(file):
	total = 0
	lines = file.read().splitlines()
	use = True
	for line in lines:
		matches = re.findall(r"mul\((\d+),\s*(\d+)\)|(do\(\))|(don't\(\))", line)
		for match in matches:
			match = list(filter(None, match))
			if len(match) == 1 and match[0] == "do()":
				use = True
			elif len(match) == 1 and match[0] == "don't()":
				use = False
			elif len(match) == 2 and use:
				total += int(match[0]) * int(match[1])
	print(total)
