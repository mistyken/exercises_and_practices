"""
After catching your classroom students cheating before, you realize your students are getting craftier and hiding words in 2D grids of letters. The word may start anywhere in the grid, and consecutive letters can be either immediately below or immediately to the right of the previous letter.

Given a grid and a word, write a function that returns the location of the word in the grid as a list of coordinates. If there are multiple matches, return any one.

grid1 = [
	['c', 'c', 'c', 't', 'i', 'b'],
	['c', 'c', 'a', 't', 'n', 'b'],
	['a', 'c', 'n', 'n', 't', 'i'],
	['t', 'c', 's', 'i', 'p', 't'],
	['a', 'o', 'o', 'o', 'a', 'a'],
	['o', 'a', 'a', 'a', 'o', 'o'],
	['k', 'a', 'i', 'c', 'k', 'i'],
]
word1 = "catnip"
word2 = "cccc"
word3 = "s"
word4 = "bit"
word5 = "aoi"
word6 = "ki"
word7 = "aaa"
word8 = "ooo"

grid2 = [['a']]
word9 = "a"

find_word_location(grid, word1) => [ (0, 2), (1, 2), (1, 3), (2, 3), (3, 3), (3, 4) ]
find_word_location(grid, word2) =>
       [(0, 1), (1, 1), (2, 1), (3, 1)]
    OR [(0, 0), (1, 0), (1, 1), (2, 1)]
    OR [(0, 0), (0, 1), (1, 1), (2, 1)]
    OR [(1, 0), (1, 1), (2, 1), (3, 1)]
find_word_location(grid1, word3) => [(3, 2)]
find_word_location(grid1, word4) => [(1, 5), (2, 5), (3, 5)]
find_word_location(grid1, word5) => [(4, 5), (5, 5), (6, 5)]
find_word_location(grid1, word6) => [(6, 4), (6, 5)]
find_word_location(grid1, word7) => [(5, 1), (5, 2), (5, 3)]
find_word_location(grid1, word8) => [(4, 1), (4, 2), (4, 3)]
find_word_location(grid2, word9) => [(0, 0)]
"""
grid1 = [
	['c', 'c', 'c', 't', 'i', 'b'],#0
	['c', 'c', 'a', 't', 'n', 'b'],#1
	['a', 'c', 'n', 'n', 't', 'i'],#2
	['t', 'c', 's', 'i', 'p', 't'],#3
	['a', 'o', 'o', 'o', 'a', 'a'],#4
	['o', 'a', 'a', 'a', 'o', 'o'],#5
	['k', 'a', 'i', 'c', 'k', 'i']#6
    #0    #1   #2    #3   #4   #5
]

word1 = "catnip"
word2 = "cccc"
word3 = "s" 
word4 = "bit"
word5 = "aoi"
word6 = "ki"
word7 = "aaa"
word8 = "ooo"

grid2 = [['a']]
word9 = "a"

def find_word_location_2(grid, word):
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            result = gridDFS((y, x), grid, word, [])

            if result:
                return result

def gridDFS(cur_pos, grid, word, acc):
    if len(word) < 1:
        return acc
    
    if grid[cur_pos[0]][cur_pos[1]] == word[0]:
        acc.append(cur_pos)
        acc_len = len(acc)
        down = (cur_pos[0] + 1, cur_pos[1])
        right = (cur_pos[0], cur_pos[1] + 1)

        if down[0] <= len(grid) - 1:
            result = gridDFS(down, grid, word[1:], acc)
            if result:
                return result
            else:
                for _ in range(len(acc) - acc_len):
                    acc.pop()
        
        if right[1] <= len(grid[0]) - 1:
            result = gridDFS(right, grid, word[1:], acc)
            if result:
                return result
            else:
                for _ in range(len(acc) - acc_len):
                    acc.pop()

        if down[0] > len(grid) - 1 and right[1] > len(grid[0]) - 1 and len(word) - 1 < 1:
            return acc
    

def find_word_location(grid, word):
    for x in range(len(grid[0])):
        for y in range(len(grid)):
            if grid[y][x] == word[0]:
                # print("cur_pos{}".format((y,x)))
                i = 1
                result = []
                stack = [(y, x)]
                while stack:
                    cur_pos = stack.pop()
                    cur_stack_len = len(stack)
                    result.append(cur_pos)
                    down = (cur_pos[0] + 1, cur_pos[1])
                    right = (cur_pos[0], cur_pos[1] + 1)
                    if down[0] <= len(grid) - 1:
                        # within Y
                        c = grid[down[0]][down[1]]
                        if i <= len(word) - 1 and c == word[i]:
                            stack.append(down)
                    if right[1] <= len(grid[0]) - 1:
                        # within X
                        c = grid[right[0]][right[1]]
                        if i <= len(word) - 1 and c == word[i]:
                            stack.append(right)
                    
                    if len(result) == len(word):
                        return result

                    if len(stack) == cur_stack_len:
                        result.pop()
                    else:
                        i += 1


print(find_word_location_2(grid1, word1))
print(find_word_location_2(grid1, word2))
print(find_word_location_2(grid1, word3))
print(find_word_location_2(grid1, word4))
print(find_word_location_2(grid1, word5))
print(find_word_location_2(grid1, word6))
print(find_word_location_2(grid1, word7))
print(find_word_location_2(grid1, word8))

# def find_embedded_word(words, string):
#     word_map = {}
#     # O(len(string))
#     for c in string:
#         if c in word_map:
#             word_map[c] += 1
#         else:
#             word_map[c] = 1
    
#     # time = O(W*L)
#     # space = O(len(string))
#     for word in words:
#         map_copy = word_map.copy()
#         found = True
#         for c in word:
#             if c in map_copy and map_copy[c] > 0:
#                 map_copy[c] -= 1
#             else:
#                 found = False
#         if not found:
#             continue
#         else:
#             return word
#     return None

# print(find_embedded_word(words, string1))
# print(find_embedded_word(words, string2))
# print(find_embedded_word(words, string3))
# print(find_embedded_word(words, string4))
# print(find_embedded_word(words, string5))
# print(find_embedded_word(words, string6))

