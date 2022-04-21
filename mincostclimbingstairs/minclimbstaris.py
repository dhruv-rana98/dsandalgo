def minCostClimbingStairs(cost) -> int:
        cost.append(0)
        for i in range(len(cost)-3, -1, -1):
            cost[i] = cost[i] + min(cost[i+1], cost[i+2])
        return min(cost[0], cost[1])

print(minCostClimbingStairs([12,14,60,24,56,11]))