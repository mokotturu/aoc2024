import numpy as np


def is_int(x):
	return np.mod(x, 1) == 0

def main(file):
	machines = []
	lines = file.read().splitlines()
	for i in range(0, len(lines), 4):
		button_a = lines[i].split(': ')[1].split(', ')
		button_b = lines[i + 1].split(': ')[1].split(', ')
		prize = lines[i + 2].split(': ')[1].split(', ')
		machines.append([
			list(map(int, [int(_button_a[2:]) for _button_a in button_a])),
			list(map(int, [int(_button_b[2:]) for _button_b in button_b])),
			list(map(int, [int(_prize[2:]) + 10000000000000 for _prize in prize]))
		])

	total = 0
	for machine in machines:
		l1 = np.array([[machine[0][0], machine[1][0]], [machine[0][1], machine[1][1]]])
		l2 = np.array(machine[2])
		a_presses, b_presses = np.linalg.solve(l1, l2)
		a_presses = np.round(a_presses, 3)
		b_presses = np.round(b_presses, 3)
		if not is_int(a_presses) or not is_int(b_presses):
			continue
		total += 3 * a_presses + b_presses

	print(int(total))
