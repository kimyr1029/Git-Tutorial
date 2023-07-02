from collections import defaultdict

def dfs(graph,path,visited):
    if path:
        top = path[-1] #stack top
        if graph[top] :
            path.append(graph[top].pop(0))
        else: #더이상 갈곳이없음
            visited.append(path.pop())
        dfs(graph,path,visited)
    return visited[::-1]


def solution(tickets):
    graph=defaultdict(list)
    for a,b in tickets: #인접그래프
        graph[a].append(b)
    for key in graph.keys(): #정렬
        graph[key].sort()
    return dfs(graph,["ICN"],[])

