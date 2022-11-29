'''

Snakes may now move in any of four directions - up, down, left, or right - one square at a time, but they will never return to a square that they've already visited.  If a snake enters the board on an edge square, we want to catch it at a different exit square on the board's edge.

The snake is familiar with the board and will take the route to the nearest reachable exit, in terms of the number of squares it has to move through to get there. Note that there may not be a reachable exit.

Here is an example board:

    col-->        0  1  2  3  4  5  6  7  8
               +---------------------------
    row      0 |  +  +  +  +  +  +  +  0  0
     |       1 |  +  +  0  0  0  0  0  +  +
     |       2 |  0  0  0  0  0  +  +  0  +
     v       3 |  +  +  0  +  +  +  +  0  0
             4 |  +  +  0  0  0  0  0  0  +
             5 |  +  +  0  +  +  0  +  0  +

Write a function that takes a rectangular board with only +'s and 0's, along with a starting point on the edge of the board, and returns the coordinates of the nearest exit to which it can travel.  If there is a tie, return any of the nearest exits.


Example: 
findExit(board1, [2,0]) => [5,2]

All test cases:
findExit(board1, start1_1) => [5, 2]
findExit(board1, start1_2) => [0, 8]
findExit(board1, start1_3) => [2, 0] or [5, 5]
findExit(board1, start1_4) => [5, 7]
findExit(board2, start2_1) => null (or a special value representing no possible exit)
findExit(board2, start2_2) => null
findExit(board3, start3_1) => [1, 0]
findExit(board3, start3_2) => [3, 0]
findExit(board3, start3_3) => [1, 4]
findExit(board3, start3_4) => [3, 4]
findExit(board4, start4_1) => [0, 1]
findExit(board4, start4_2) => [0, 3]
findExit(board4, start4_3) => [4, 1]
findExit(board4, start4_4) => [4, 3]
findExit(board5, start5_1) => [0, 2]


'''

board_1 = [['+', '+', '+', '+', '+', '+', '+', '0', '0'],
           ['+', '+', '0', '0', '0', '0', '0', '+', '+'],
           ['0', '0', '0', '0', '0', '+', '+', '0', '+'],
           ['+', '+', '0', '+', '+', '+', '+', '0', '0'],
           ['+', '+', '0', '0', '0', '0', '0', '0', '+'],
           ['+', '+', '0', '+', '+', '0', '+', '0', '+']]

start_1_1 = (2, 0) # Expected output = (5, 2) 
start_1_2 = (0, 7) # Expected output = (0, 8)
start_1_3 = (5, 2) # Expected output = (2, 0) or (5, 5)
start_1_4 = (5, 5) # Expected output = (5, 7)

board_2 = [['+', '+', '+', '+', '+', '+', '+'],
           ['0', '0', '0', '0', '+', '0', '+'],
           ['+', '0', '+', '0', '+', '0', '0'],
           ['+', '0', '0', '0', '+', '+', '+'],
           ['+', '+', '+', '+', '+', '+', '+']]


start_2_1 = (1, 0) # Expected output = null (or a special value representing no possible exit)
start_2_2 = (2, 6) # Expected output = null 

board_3 = [['+', '0', '+', '0', '+',],
           ['0', '0', '+', '0', '0',],
           ['+', '0', '+', '0', '+',],
           ['0', '0', '+', '0', '0',],
           ['+', '0', '+', '0', '+']]

start_3_1 = (0, 1) # Expected output = (1, 0)
start_3_2 = (4, 1) # Expected output = (3, 0)
start_3_3 = (0, 3) # Expected output = (1, 4)
start_3_4 = (4, 3) # Expected output = (3, 4)

board_4 = [['+', '0', '+', '0', '+',],
           ['0', '0', '0', '0', '0',],
           ['+', '+', '+', '+', '+',],
           ['0', '0', '0', '0', '0',],
           ['+', '0', '+', '0', '+']]

start_4_1 = (1, 0) # Expected output = (0, 1)
start_4_2 = (1, 4) # Expected output = (0, 3)
start_4_3 = (3, 0) # Expected output = (4, 1)
start_4_4 = (3, 4) # Expected output = (4, 3)

board_5 = [['+', '0', '0', '0', '+',],
           ['+', '0', '+', '0', '+',],
           ['+', '0', '0', '0', '+',],
           ['+', '0', '+', '0', '+']]

start_5_1 = (0, 1) # Expected output = (0, 2)
start_5_2 = (3, 1) # Expected output = (0, 1)




def find_passable_lanes(board):
    rows = []
    columns = []
    # O(R)
    for i in range(len(board)):
        if '+' not in board[i]:
            rows.append(i)
    
    # O(C^R) #O(n^2)
    for x in range(len(board[0])):
        holder = []
        # O(R)
        for y in range(len(board)):
            holder.append(board[y][x])
        if '+' not in holder:
            columns.append(x)
        print(holder)
    return rows, columns


def findExit(board, starting_point):
    queue = [(starting_point[0], starting_point[1])]
    visited = set()
    starting = True
    while queue:
        visiting_node = queue.pop(0)
        visited.add(visiting_node)
        
        top = (visiting_node[0] - 1,visiting_node[1])
        down = (visiting_node[0] + 1,visiting_node[1])
        left = (visiting_node[0],visiting_node[1] - 1)
        right = (visiting_node[0],visiting_node[1] + 1)
        
        # check bound
        # 
        if (top[0] < 0):
            if not starting:
                return (top[0] + 1, top[1])
        else:
            if top not in visited and board[top[0]][top[1]] == '0':
                queue.append(top)
        
        if (down[0] > len(board) - 1):
            if not starting:
                return (down[0] - 1, down[1])
        else:
            if down not in visited and board[down[0]][down[1]] == '0':
                queue.append(down)
                
        if (left[1] < 0):
            if not starting:
                return (left[0], left[1] + 1)
        else:
            if left not in visited and board[left[0]][left[1]] == '0':
                queue.append(left)
                
        if (right[1] > len(board[0]) - 1):
            if not starting:
                return (right[0], right[1] - 1)
        else:
            if right not in visited and board[right[0]][right[1]] == '0':
                queue.append(right)
        
        starting = False
    return ()


print(findExit(board_5, start_5_1))

# print(find_passable_lanes(straight_board_4))