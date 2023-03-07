# #노드, 간선, 시작점, 비용
# #연결 graph
# #초기 비용은 무한초기화
# import heapq
# import sys
# input=sys.stdin.readline
# INF=int(1e9)

# #v,e,c
# v,e=map(int,input().split())
# start=int(input())

# graph=[[] for _ in range(v+1)]
# distance=[INF]*(v+1)

# for _ in range(e):
#     a,b,c=map(int,input().split())
#     #a->b = c
#     graph[a].append((b,c))

# def dijkstra(strat):
#     q=[]
#     heapq.heappush(q,(0,start))
#     distance[start]=0

#     while q:
#         dist,now=heapq.heappop(q)
#         if distance[now]<dist:
#             continue
#         for i in graph[now]: #인접
#             cost = dist+i[1]
#             if cost<distance[i[0]]:
#                 distance[i[0]]=cost
# dijkstra(start)
# for i in range(1,n+1):
#     if distance[i]==INF:
#         print('INFINITY')
#     else:
#         print(distance[i])
import heapq
import sys

input=sys.stdin.readline
v,e=map(int,input().split())
start=int(input())
INF=int(1e9)
graph=[[] for _ in range(v+1)]
distance=[INF]*(v+1)

for i in range(e):
    a,b,c=map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0
    while q:
        dist,now=heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i in graph[now]: #인접
            node,cost=i[0],i[1]
            cost=cost+dist #거리합
            if cost<distance[node]: #최단경로
                distance[node]=cost
                heapq.heappush(q,(cost,node)) #heap 추가

dijkstra(start)
for i in range(v+1):
    if distance[i]==INF:
        print('INF')
    else:
        print(distance[i])
