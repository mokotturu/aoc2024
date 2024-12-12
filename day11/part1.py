def num_of_digits(num):
	return len(str(num))

def main(file):
	lines = file.read().splitlines()
	arr = list(map(int, lines[0].split()))

	num_blinks = 25
	for num_blink in range(num_blinks):
		new_arr = []
		for stone_idx, stone in enumerate(arr):
			if stone == 0:
				new_arr.append(1)
			elif num_of_digits(stone) % 2 == 0:
				left_half_digits = num_of_digits(stone) // 2
				left_half = stone // (10 ** left_half_digits)
				right_half = stone % (10 ** left_half_digits)
				new_arr.append(left_half)
				new_arr.append(right_half)
			else:
				new_arr.append(stone * 2024)
		arr = new_arr

	print(len(arr))
