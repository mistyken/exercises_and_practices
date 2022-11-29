
"""
# https://stackoverflow.com/questions/63999102/balanced-system-files-partition-coding-challenge
parent = [-1,0,0,1,1,2]
files_size = [1,2,2,1,1,1]
Cut the branches between directories 1 and 0.
The partition {0,2,5} has size files_size[0] + files_size[2] + files_size[5] = 1 + 2 + 1 = 4.
The partition {1,3,4} has size files_size[1] + files_size[3] + files_size[4] = 2 + 1 + 1 = 4.
The absolute difference between the sizes of the two new trees is 4 - 4 = 0.
Since no other partition can have a smaller absolute difference, the final answer is 0.

Function Description
Complete the function mostBalancedPartition in the editor below.

The function has the following parameter(s):
int parent[n]: each parent[i] is the parent directory of directory i
int files_size[n]: each file_sizes[i] is the sum of file sizes in directory i

Returns
int: the minimum absolute difference in the size of content between two subtrees

Sample Input
parent = [ -1, 0, 1, 2, 1, 0, 5, 2, 0, 0 ]
files_size = [ 8475, 6038, 8072, 7298, 5363, 9732, 3786, 5521, 8295, 6186 ]
Sample Output
4182

Sample Input
parent = [ -1, 0, 0, 0, 0, 3, 4, 6, 0, 3 ]
files_size = [ 298, 2187, 5054, 266, 1989, 6499, 5450, 2205, 5893, 8095 ]
Sample Output
8216
"""
def mostBalancedPartition(parent, files_size):
    # Write your code here
    def helper(node, adj, files_size):
        queue = [node]
        weight = 0
        while queue:
            index = queue.pop()
            weight += files_size[index]
            if index in adj:
              queue.extend(adj[index])
        return weight

    adj = {}
    edges = []
    for index, p in enumerate(parent):
        edges.append((p, index))
        if p in adj:
            adj[p].append(index)
        else:
            adj[p] = [index]
    
    print(adj, edges)
    total_weight = sum(files_size)
    min_diff = sum(files_size)
    for e in edges:
        p,c = e
        adj[p].remove(c)
        w1 = helper(c, adj, files_size)
        min_diff = min(min_diff, abs(total_weight - 2*w1))
        adj[p].append(c)

    return min_diff

parent = [-1,0,0,1,1,2]
files_size = [1,2,2,1,1,1]
print(mostBalancedPartition(parent, files_size))