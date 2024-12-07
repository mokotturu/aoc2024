from itertools import product
from operator import add, mul


def myeval(expr: list, target: int) -> int:
	res = 0
	op = add
	for elem in expr:
		if callable(elem):
			op = elem
		else:
			res = op(res, elem)

		if res > target:
			return -1

	return res


def main(file):
	D = []
	lines = file.read().splitlines()
	for line in lines:
		test_val, nums = line.split(": ")
		nums = list(map(int, nums.split()))
		D.append([int(test_val), *nums])

	total = 0
	for _d in D:
		test_val_key, nums = _d[0], _d[1:]
		num_slots = len(nums) - 1
		possible_ops = [add, mul]
		possible_op_combinations = product(possible_ops, repeat=num_slots)
		for op_combination in possible_op_combinations:
			expr = []
			for num_idx, num in enumerate(nums):
				expr.append(num)
				if num_idx < len(op_combination):
					expr.append(op_combination[num_idx])
			res = myeval(expr, test_val_key)
			if res == test_val_key:
				total += test_val_key
				break

	print(total)
