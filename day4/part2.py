def main(file):
	arr = []

	lines = file.read().splitlines()
	for line in lines:
		arr.append(line)

	count = 0
	for col in range(len(arr)):
		for row in range(len(arr[0])):
			if col > 0 and row > 0 and col < len(arr) - 1 and row < len(arr[0]) - 1 and arr[row][col] == 'A':
				if arr[row - 1][col - 1] == 'M' and arr[row + 1][col + 1] == 'S' and arr[row - 1][col + 1] == 'M' and arr[row + 1][col - 1] == 'S' or \
					arr[row - 1][col + 1] == 'M' and arr[row + 1][col - 1] == 'S' and arr[row + 1][col + 1] == 'M' and arr[row - 1][col - 1] == 'S' or \
					arr[row - 1][col - 1] == 'S' and arr[row + 1][col + 1] == 'M' and arr[row - 1][col + 1] == 'S' and arr[row + 1][col - 1] == 'M' or \
					arr[row - 1][col + 1] == 'S' and arr[row + 1][col - 1] == 'M' and arr[row + 1][col + 1] == 'S' and arr[row - 1][col - 1] == 'M':
					count += 1

	print(count)
