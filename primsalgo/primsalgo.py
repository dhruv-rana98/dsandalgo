from cmath import cos
import heapq


def minCostConnectPoints(points):
    N = len(points)

    adj = { i:[] for i in range(N) } #initialize adjaceny list , would have i : [cost, node]
    # print(adj)
    #building the adjacency list with points to find the disanc
    for i in range(N):
        x1, y1 = points[i]
        for j in range(i+1, N):  #starting from next point of i till end
            x2, y2 = points[j]
            dist = abs(x1-x2) + abs(y1-y2)
            adj[i].append([dist, j]) #neighbour distance from i 
            adj[j].append([dist, i]) #neighbour distance from j
    # print(adj)
    #prims algo

    res = 0
    visit = set()  #creating a hashset
    minH = [[0, 0]]  #[cost, point]

    while len(visit) < N: #termination statement to stop the loop when all the nodes are visited
        cost, i = heapq.heappop(minH)
        if i in visit:  
            continue #skip the remaining part of the loop if node already visited  
        res += cost
        visit.add(i)
        # pushing to minheap the adj nodes of i i.e current point added to visited after i
        for neiCost, nei in adj[i]:  #i has two values i: [cost, point]
            heapq.heappush(minH, [neiCost, nei]) #push to minheap
    return res

print(minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))

