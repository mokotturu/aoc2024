def is_safe(nums):
	last_diff = nums[1] - nums[0]
	if last_diff == 0 or last_diff > 3 or last_diff < -3:
		return False

	for i in range(2, len(nums)):
		diff = nums[i] - nums[i - 1]
		if (last_diff > 0 and diff not in [1, 2, 3]) or (last_diff < 0 and diff not in [-1, -2, -3]):
			break
		last_diff = diff
	else:
		return True


def main(file):
	num_safe = 0
	lines = file.read().splitlines()
	for line in lines:
		nums = list(map(int, line.split()))
		# improve
		num_safe += is_safe(nums) or any(is_safe(nums[:i] + nums[i + 1:]) for i in range(len(nums)))

	print(num_safe)
