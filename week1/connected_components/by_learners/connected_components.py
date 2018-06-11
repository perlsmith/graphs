#Uses python3

import sys, pdb


def number_of_components(adj):
	# list of lists of ints (node indices) --> int
	result = 0
	#write your code here
	clique_list = []
	clq_counter = -1	# only gets used after an increment
	for node, adj_list in enumerate(adj) :
		if not node in [y for x in clique_list for y in x ] :
		# that is, this node is not part of a connected set already..
			clq_counter += 1
			clique_list.append([])
			explore_node( adj, node, clique_list, clq_counter )

	return len(clique_list )

def explore_node( adj, node, clique_list, clq_counter ) :
	# adjacency list (list of lists of ints), int, list of lists of ints, int --> nothing
	# side effect is that clique_list gets updated

	# because we have already stepped into this rabbit hole
	clique_list[clq_counter].append(node)
	
	for neighbour in adj[node] :
		if not neighbour in [y for x in clique_list for y in x ] :
			explore_node( adj, neighbour, clique_list, clq_counter )
			

	
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    # pdb.set_trace()
    print(number_of_components(adj))
