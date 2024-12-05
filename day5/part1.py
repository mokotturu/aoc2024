import matplotlib.pyplot as plt
import networkx as nx


def main(file):
	orders = []
	updates = []
	correct = []

	lines = file.read().splitlines()

	# horrible!

	proc_updates = False
	for line in lines:
		if not proc_updates and line != '':
			first, second = map(int, line.split('|'))
			orders.append((first, second))
		elif proc_updates and line != '':
			nums = list(map(int, line.split(',')))
			updates.append(nums)

		if not proc_updates and line == '':
			proc_updates = True

	G = nx.DiGraph()
	for order in orders:
		G.add_edge(order[0], order[1])

	for update_idx, update in enumerate(updates):
		updated = {node: False for node in G.nodes()}
		for i in range(len(update)):
			if update[i] in G:
				children = list(G.successors(update[i]))
				if all([elem in children for elem in update[i+1:]]):
					updated[update[i]] = True

		if all([updated[elem] for elem in update]):
			correct.append(update_idx)

	res = sum(updates[update_idx][len(updates[update_idx]) // 2] for update_idx in correct)
	print(res)
