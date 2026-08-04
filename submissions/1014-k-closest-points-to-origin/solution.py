class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import math
        import heapq
        distances = []
        for x, y in points:
            distances.append([math.sqrt(x**2 + y**2), x, y])
        heapq.heapify(distances)
        output = []
        while k > 0:
            distance, x, y = heapq.heappop(distances)
            output.append([x, y])
            k -= 1
        return output
