from collections import defaultdict, deque

class Twitter:
    def __init__(self):
       self.following_map = defaultdict(set)
       self.tweets = deque()

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets.appendleft((userId, tweetId))

    def getNewsFeed(self, userId: int) -> list[int]:
        feed = []
        following = self.following_map[userId] | {userId}
        for author, tweet in self.tweets:
            if author in following:
                feed.append(tweet)
            if len(feed) == 10:
                break
        return feed
        
    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.following_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.following_map[followerId].discard(followeeId)
        

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
