#2022-04-15
'''
arr = [[0,1,1,1,0,1],[1,0,0,0,0,0],[1,0,0,1,1,0],[1,0,1,0,0,0],[0,0,1,0,0,1],[1,0,0,0,1,0]]
'''

'''
def dfs(graph,v,visited):
    visited[v] = 1
    print(v,end=' ')

    for i in range(len(graph[v])):
        if graph[v][i] == 1:
            if visited[i] == 0:
                dfs(graph,i,visited)

graph = [[0,1,1,1,0,1],[1,0,1,0,0,0],[1,1,0,0,1,0],[1,0,0,0,1,1],[0,0,1,1,0,0],[1,0,0,1,0,0]]

visited = [0]*len(graph)
dfs(graph,0,visited)
'''

'''
from collections import deque

def bfs(graph,v,visited):
    queue = deque([v])
    visited[v] = 1

    while queue:
        node = queue.popleft()
        print(node,end = ' ')

        for i in range(len(graph[node])):
            if graph[node][i] == 1:
                if visited[i] == 0:
                    queue.append(i)
                    visited[i] = 1

graph = [[0,1,1,1,0,1],[1,0,1,0,0,0],[1,1,0,0,1,0],[1,0,0,0,1,1],[0,0,1,1,0,0],[1,0,0,1,0,0]]

visited = [0]*len(graph)
bfs(graph,0,visited)


