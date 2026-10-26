class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        # solution will only exist if total gas > total cost
        if sum(gas) < sum(cost):
            return - 1
        
        fuel = 0
        best = 0

        for i in range(len(gas)):
            fuel += gas[i] - cost[i]
            # if wherever you started doesn't work then try the next
            if fuel < 0:
                fuel = 0
                best = i + 1
        return best
