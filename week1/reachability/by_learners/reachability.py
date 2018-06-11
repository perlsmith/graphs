#Uses python3

import sys, pdb

def reach(adj, x, y):
	# (list of list of ints(which are indices) , int, int ) --> 0 or 1
	#write your code here
	done_set = []
	if rec_reach( adj, x, y, done_set ) :
		return 1
	else :
		return 0

def rec_reach( adj, x, y, done_keeper ) :
	if y in adj[x] :
		return True
	else :
		for neighbour in adj[x] :
			if not neighbour in done_keeper :
				done_keeper.append( neighbour )
				if rec_reach( adj, neighbour, y , done_keeper ) :
					return True
		return False
	
if __name__ == '__main__':
    input = sys.stdin.read()
    # pdb.set_trace()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1		# coz input data is 1-indexed
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))

# what I will learn from this one - how to handle the base
# case for this recursive implementation in an elegant way
# i.e., without recourse to a global..