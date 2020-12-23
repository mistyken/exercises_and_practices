class Solution:
    def longestCommonPrefix2(self, nodes_from, nodes_to):
        vectors = zip(nodes_from, nodes_to)
        
        vector_map = {}
        for fr, to in vectors:
            if fr < to:
                node_set = vector_map.get(fr, set())
                node_set.add(to)
                vector_map[fr] = node_set
        
        cycles = []
        for node_one, set_one in vector_map.items():
            for node_two in set_one:
                set_two = vector_map.get(node_two, set())
                intersection = set_one.intersection(set_two)
                for node_three in intersection:
                    cycles.append([node_one, node_two, node_three])

        print(vector_map)
        print(cycles)


    def longestCommonPrefix(self, nodes_from, nodes_to):
        # the function accepts 2 list of vertices
        # for example [1,2,3] [2,3,1] is a triangle
        # it will find trios of all the nodes and find minimum related node from the group of 3

        related_nodes = {}
        trios = []
        result = 999999999
        for fr, to in zip(nodes_from, nodes_to):
            if fr not in related_nodes:
                related_nodes[fr] = []
            if to not in related_nodes:
                related_nodes[to] = []
            
            if to not in related_nodes[fr]:
                related_nodes[fr].append(to)
            if fr not in related_nodes[to]:
                related_nodes[to].append(fr)

            for node in related_nodes:
                if fr in related_nodes[node] and to in related_nodes[node]:
                    trios.append([node, fr, to])
        
        print(related_nodes)
        print(trios)
        
        for trio in trios:
            holder = 0
            seem = []
            for node in trio:
                for x in related_nodes[node] + [node]:
                    if x not in trio and x not in seem:
                        holder += 1
                        seem.append(x)
            
            if holder < result:
                result = holder

        return result if trios else -1


if __name__ == "__main__":
    answer = Solution()
    print(answer.longestCommonPrefix2([1, 1, 2, 2, 3, 4, 1, 6], [2, 3, 3, 4, 4, 5, 6, 5]))
    # print(answer.longestCommonPrefix([7,2,3,5,1], [4,1,6,1,7]))
    # print(answer.longestCommonPrefix([1,2,3], [2,3,1]))
    # print(answer.longestCommonPrefix([1,2,2,3,4,5], [2,4,5,5,5,6]))