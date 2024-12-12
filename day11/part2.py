from functools import cache


@cache
def num_of_digits(num):
	return len(str(num))

@cache
def count(stone, blink_num, num_blinks):
	if blink_num == num_blinks:
		return 1
	elif stone == 0:
		return count(1, blink_num + 1, num_blinks)
	elif num_of_digits(stone) % 2 == 0:
		left_half_digits = num_of_digits(stone) // 2
		left_half = stone // (10 ** left_half_digits)
		right_half = stone % (10 ** left_half_digits)
		return count(left_half, blink_num + 1, num_blinks) + count(right_half, blink_num + 1, num_blinks)
	else:
		return count(stone * 2024, blink_num + 1, num_blinks)

def main(file):
	lines = file.read().splitlines()
	arr = list(map(int, lines[0].split()))

	num_blinks = 75
	num_stones = 0
	for i, stone in enumerate(arr):
		num_stones += count(stone, 0, num_blinks)

	print(num_stones)
