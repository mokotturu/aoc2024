import matplotlib.pyplot as plt
import networkx as nx


def is_correct(G: nx.DiGraph, update: list[int]):
	updated = {node: False for node in G.nodes()}
	for i in range(len(update)):
		if update[i] in G:
			children = list(G.successors(update[i]))
			if all([elem in children for elem in update[i+1:]]):
				updated[update[i]] = True

	return all([updated[elem] for elem in update])

def main(file):
	orders = []
	updates = []
	incorrect = []

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
		if not is_correct(G, update):
			incorrect.append(update_idx)

	for ic in incorrect:
		ordered = False
		while not ordered:
			for order in orders:
				if order[0] in updates[ic] and order[1] in updates[ic]:
					l_idx = updates[ic].index(order[0])
					r_idx = updates[ic].index(order[1])
					if l_idx > r_idx:
						updates[ic][l_idx], updates[ic][r_idx] = updates[ic][r_idx], updates[ic][l_idx]
			ordered = is_correct(G, updates[ic])

	res = sum(updates[update_idx][len(updates[update_idx]) // 2] for update_idx in incorrect)
	print(res)
