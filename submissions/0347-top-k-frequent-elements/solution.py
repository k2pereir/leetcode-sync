class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency = dict()
        for i in nums:
            if i in frequency:
                frequency[i] += 1
            else:
                frequency[i] = 1
        
        freq = sorted(frequency.items(), key=lambda item: item[1], reverse=True)

        return [item[0] for item in freq[:k]]

