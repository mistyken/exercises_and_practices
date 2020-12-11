class Solution:
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
    print(answer.longestCommonPrefix([1, 1, 2, 2, 3, 4, 1, 6], [2, 3, 3, 4, 4, 5, 6, 5]))
    # print(answer.longestCommonPrefix([7,2,3,5,1], [4,1,6,1,7]))
    # print(answer.longestCommonPrefix([1,2,3], [2,3,1]))
    # print(answer.longestCommonPrefix([1,2,2,3,4,5], [2,4,5,5,5,6]))