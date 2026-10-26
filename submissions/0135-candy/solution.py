class Solution:
    def candy(self, ratings: list[int]) -> int:
        length = len(ratings)
        candies = [1] * length # each child will get at least 1 candy

        indicies = sorted(range(length), key=lambda i: ratings[i])

        for i in indicies:
            if i > 0 and ratings[i] > ratings[i - 1]:
                candies[i] = max(candies[i], candies[i - 1] + 1)
            if i < length - 1 and ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)
