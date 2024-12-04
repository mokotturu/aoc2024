def main(file):
	word_to_find = "XMAS"
	arr = []

	lines = file.read().splitlines()
	for line in lines:
		arr.append(line)

	# horrible!

	occurrences = 0
	for i in range(len(arr)):
		count = arr[i].count(word_to_find)
		occurrences += count
		count = arr[i][::-1].count(word_to_find)
		occurrences += count

	for i in range(len(arr[0])):
		vert = ''.join([arr[j][i] for j in range(len(arr))])
		count = vert.count(word_to_find)
		occurrences += count
		count = vert[::-1].count(word_to_find)
		occurrences += count

	diagonals = []

	row, col = len(arr) - 1, 0
	while not (row == 0 and col == len(arr[0])):
		diagonal = ''.join([arr[row + i][col + i] for i in range(min(len(arr) - row, len(arr[0]) - col))])
		diagonals.append(diagonal)
		if row > 0:
			row -= 1
		else:
			col += 1

	row, col = len(arr) - 1, len(arr[0]) - 1
	while not (row < 0 and col == 0):
		diagonal = ''.join([arr[row - i][col + i] for i in range(min(row + 1, len(arr[0]) - col))])
		diagonals.append(diagonal)
		if col > 0:
			col -= 1
		else:
			row -= 1

	for diagonal in diagonals:
		count = diagonal.count(word_to_find)
		occurrences += count
		count = diagonal[::-1].count(word_to_find)
		occurrences += count

	print(occurrences)
