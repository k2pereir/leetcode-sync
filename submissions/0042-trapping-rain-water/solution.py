class Solution:
    def trap(self, height: list[int]) -> int:
        # if there's nothing there, then no water will be collected
        if not height:
            return 0

        length = len(height)
        lmax = [0] * length
        rmax = [0] * length
        total = 0
        lmax[0] = height[0]
        for i in range(1, length):
            lmax[i] = max(lmax[i - 1], height[i])
        rmax[length - 1] = height[length - 1]
        for i in range(length - 2, -1, -1):
            rmax[i] = max(rmax[i + 1], height[i])
        
        for i in range(length):
            water_level = min(lmax[i], rmax[i])
            total += water_level - height[i]
        
        return total
