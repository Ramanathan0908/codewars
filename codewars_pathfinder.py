from math import isqrt
from collections import deque

mazed = [
    ['.', '.', 'W', '.', 'W', '.', '.', '.', '.', 'W', '.', '.', 'W', '.', '.'], 
    ['W', '.', '.', 'W', '.', '.', '.', '.', '.', 'W', '.', '.', '.', '.', 'W'], 
    ['.', '.', 'W', '.', '.', '.', 'W', '.', 'W', '.', 'W', '.', 'W', 'W', '.'], 
    ['.', 'W', 'W', '.', '.', '.', '.', '.', 'W', 'W', '.', '.', '.', '.', '.'], 
    ['.', 'W', '.', 'W', '.', '.', '.', '.', 'W', '.', '.', '.', '.', 'W', '.'], 
    ['.', '.', '.', '.', '.', 'W', '.', '.', '.', '.', '.', 'W', 'W', '.', '.'], 
    ['W', 'W', '.', '.', 'W', '.', 'W', '.', '.', 'W', 'W', 'W', '.', '.', '.'], 
    ['.', '.', '.', '.', '.', 'W', '.', '.', '.', 'W', 'W', 'W', '.', 'W', '.'], 
    ['.', '.', '.', '.', 'W', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'], 
    ['W', '.', 'W', '.', '.', '.', '.', '.', '.', '.', 'W', '.', '.', '.', '.'], 
    ['W', '.', 'W', '.', '.', '.', '.', 'W', '.', '.', 'W', 'W', '.', '.', '.'], 
    ['.', '.', '.', '.', '.', '.', '.', 'W', '.', '.', '.', 'W', '.', '.', 'W'], 
    ['.', '.', 'W', 'W', '.', '.', '.', 'W', '.', 'W', 'W', '.', '.', '.', 'W'], 
    ['.', '.', 'W', 'W', '.', '.', '.', '.', '.', '.', 'W', '.', '.', 'W', '.'], 
    ['.', '.', '.', '.', 'W', '.', '.', '.', '.', '.', '.', 'W', 'W', '.', '.']
]

a = "\n".join([
          ".W...",
          ".W...",
          ".W.W.",
          "...W.",
          "...W."])
"""
#my own path finding solution, works but max recurrsion dept is reached in code wars

state = 0

def path_finder(strn_maze):
    arr_maze= [[] for i in range(isqrt(len(strn_maze)))]
    a = strn_maze.replace('\n', '')

    for index, char in enumerate(a):
        arr_maze[index // isqrt(len(a))].append(char)
    
    prev_list = []

    def recurr(maze, pt):
        if pt == [len(maze) - 1, len(maze) - 1]:
            print(pt)
            return True

        adj = []
        prev_list.append(pt)
        global state

        for i in [1, -1]:
            if state == 0:
                if pt[1] + i >= 0 and pt[1] + i < len(maze):
                    if maze[pt[0]][pt[1] + i] != 'W' and maze[pt[0]][pt[1] + i] != 'w' and [pt[0], pt[1] + i] not in prev_list:
                        adj.append([pt[0], pt[1] + i])
                if pt[0] + i >= 0 and pt[0] + i < len(maze):
                    if maze[pt[0] + i][pt[1]] != 'W' and maze[pt[0] + i][pt[1]] != 'w' and [pt[0] + i, pt[1]] not in prev_list:
                        adj.append([pt[0] + i, pt[1]])
                state = 1
            else:
                if pt[0] + i >= 0 and pt[0] + i < len(maze):
                    if maze[pt[0] + i][pt[1]] != 'W' and maze[pt[0] + i][pt[1]] != 'w' and [pt[0] + i, pt[1]] not in prev_list:
                        adj.append([pt[0] + i, pt[1]])
                if pt[1] + i >= 0 and pt[1] + i < len(maze):
                    if maze[pt[0]][pt[1] + i] != 'W' and maze[pt[0]][pt[1] + i] != 'w' and [pt[0], pt[1] + i] not in prev_list:
                        adj.append([pt[0], pt[1] + i])
                state = 0

        for point in adj:
            if recurr(maze, point):
                return True

        return False
    return recurr(arr_maze, [0, 0])

print(path_finder(a))
"""

"""
closed_nodes = []
open_nodes = []

def path_finder(strn_maze):
    maze= [[] for i in range(isqrt(len(strn_maze)))]
    a = strn_maze.replace('\n', '')

    for index, char in enumerate(a):
        maze[index // isqrt(len(a))].append(char)

    end = [len(maze) - 1, len(maze) - 1]
    open_nodes.append([0, 0])
    bool = True
    while bool:
        for node in open_nodes:
            for i in [1, -1]:
                if node[1] + i >= 0 and node[1] + i < len(maze):
                    if maze[node[0]][node[1] + i] != 'W' and maze[node[0]][node[1] + i] != 'w' and [node[0], node[1] + i] not in closed_nodes:
                        open_nodes.append([node[0], node[1] + i])
                if node[0] + i >= 0 and node[0] + i < len(maze):
                    if maze[node[0] + i][node[1]] != 'W' and maze[node[0] + i][node[1]] != 'w' and [node[0] + i, node[1]] not in closed_nodes:
                        open_nodes.append([node[0] + i, node[1]])

            closed_nodes.append(node)
            open_nodes.remove(node)
        if end in closed_nodes:
            return True
        if len(open_nodes) == 0 and end not in closed_nodes:
            bool = False
            break
    return False

print(path_finder(a))
"""
"""
def cost(prev_cost, end, pt):
    g_cost = prev_cost + 1
    h_cost = end[0] - pt[0] + end[1] - pt[1]

    return g_cost + h_cost

def path_finder(strn_maze):
    maze= [[] for i in range(isqrt(len(strn_maze)))]
    a = strn_maze.replace('\n', '')

    for index, char in enumerate(a):
        maze[index // isqrt(len(a))].append(char)
    end = [len(maze) - 1, len(maze) - 1]

    #open_nodes = {[0, 0]: 0, }
    open_nodes_pts = [[0, 0]]
    open_nodes_costs = [0]
    closed_nodes = []

    current_pt = [0, 0]

    while current_pt != end:
        cp_cost = open_nodes_costs[open_nodes_pts.index(current_pt)]
        for i in [1, -1]:
            if current_pt[1] + i >= 0 and current_pt[1] + i < len(maze):
                if maze[current_pt[0]][current_pt[1] + i] != 'W' and maze[current_pt[0]][current_pt[1] + i] != 'w' and [current_pt[0], current_pt[1] + i] not in closed_nodes:
                    #open_nodes[[current_pt[0], current_pt[1] + i]] = cost(open_nodes[current_pt], end, [current_pt[0], current_pt[1] + i])
                    open_nodes_pts.append([current_pt[0], current_pt[1] + i])
                    open_nodes_costs.append(cost(cp_cost, end, [current_pt[0], current_pt[1] + i]))
            if current_pt[0] + i >= 0 and current_pt[0] + i < len(maze):
                if maze[current_pt[0] + i][current_pt[1]] != 'W' and maze[current_pt[0] + i][current_pt[1]] != 'w' and [current_pt[0] + i, current_pt[1]] not in closed_nodes:
                    #open_nodes[[current_pt[0] + i, current_pt[1]]] = cost(open_nodes[current_pt], end, [current_pt[0] + i, current_pt[1]])
                    open_nodes_pts.append([current_pt[0] + i, current_pt[1]])
                    open_nodes_costs.append(cost(cp_cost, end, [current_pt[0] + i, current_pt[1]]))
        closed_nodes.append(current_pt)
        open_nodes_costs.pop(open_nodes_pts.index(current_pt))
        open_nodes_pts.remove(current_pt)
        if len(open_nodes_pts) == 0:
            return False
        current_pt = open_nodes_pts[open_nodes_costs.index(min(open_nodes_costs))]
    
    return True

print(path_finder(a))
"""
b = "\n".join([
          ".......W..",
          "W.W......W",
          ".......W..",
          ".WWW.W..W.",
          "....W.W..W",
          ".W.....WWW",
          ".W.W.WW...",
          ".....W.W..",
          ".......W..",
          ".W.W......"])
"""
def path_finder(strmaze):
    #maze= [[] for i in range(isqrt(len(strn_maze)))]
    maze = strmaze.replace('\n', '')

    #for index, char in enumerate(a):
        #maze[index // isqrt(len(a))].append(char)

    prev_list = []
    le = isqrt(len(maze))
    end = len(maze) - 1

    def next_pts(adj):
        if end in adj:
            return True

        prev_list.extend(adj)
        new_adj = []
        for point in adj:
            i = point // le
            j = point % le
            for k in [1, -1]:
                i2 = (i + k) * le + j
                j2 = i * le + j + k
                if i + k >= 0 and i + k < le:
                    if maze[i2] != 'W' and maze[i2] != 'w' and i2 not in prev_list and i2 not in new_adj:
                        new_adj.append(i2)
                if j + k >= 0 and j + k < le:
                    if maze[j2] != 'W' and maze[j2] != 'w' and j2 not in prev_list and j2 not in new_adj:
                        new_adj.append(j2)

        if len(new_adj) == 0:
            return False

        if next_pts(new_adj):
            return True
        else:
            return False

    return next_pts([0])
"""
"""
def path_finder(strmaze):
    maze = strmaze.replace('\n', '')

    prev_list = []
    le = isqrt(len(maze))
    end = len(maze) - 1
    adj = [0]

    while end not in prev_list:
        prev_list.extend(adj)
        new_adj = []
        for point in adj:
            i = point // le
            j = point % le
            for k in [1, -1]:
                i2 = (i + k) * le + j
                j2 = i * le + j + k
                if i + k >= 0 and i + k < le:
                    if maze[i2] != 'W' and maze[i2] != 'w' and i2 not in prev_list and i2 not in new_adj:
                        new_adj.append(i2)
                if j + k >= 0 and j + k < le:
                    if maze[j2] != 'W' and maze[j2] != 'w' and j2 not in prev_list and j2 not in new_adj:
                        new_adj.append(j2)

        adj = new_adj[:]
        if len(new_adj) == 0:
            return False
        if end in new_adj:
            return True


print(path_finder(b))
"""

def path_finder(maze):
    size = isqrt(len(maze))
    end = len(maze) - 1
    prev_list = deque([0])
    pt = 0
    visited = [False for i in range(len(maze))]

    while True:
        for i in [1, -1]:
            if prev_list[pt] + i >= 0 and prev_list[pt] + i <= end:
                j = maze[prev_list[pt] + i]
                if j != 'W' and j != '\n' and not visited[prev_list[pt] + i]:
                    prev_list.append(prev_list[pt] + i)
                    visited[prev_list[pt] + i] = True
            if prev_list[pt] + i * size + i * 1 >= 0 and prev_list[pt] + i * size + i * 1 <= end:
                k = maze[prev_list[pt] + i * size + i * 1]
                if k != 'W' and k != '\n' and not visited[prev_list[pt] + i * size + i * 1]:
                    prev_list.append(prev_list[pt] + i * size + i * 1)
                    visited[prev_list[pt] + i * size + i * 1] = True
        pt += 1

        if visited[end]:
            return True

        if pt == len(prev_list):
            print(prev_list)
            return False

    return True


print(path_finder(b))