
from collections import defaultdict
import heapq

class Twitter:

    def __init__(self):

        self.time = 0
        self.tweets = defaultdict(list)
        self.following = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:

        self.time += 1

        self.tweets[userId].append((self.time, tweetId))

    def getNewsFeed(self, userId: int):

        heap = []

        users = self.following[userId].copy()
        users.add(userId)

        for user in users:

            for time, tweet in self.tweets[user]:

                heapq.heappush(heap, (-time, tweet))

        answer = []

        while heap and len(answer) < 10:

            answer.append(heapq.heappop(heap)[1])

        return answer

    def follow(self, followerId: int, followeeId: int) -> None:

        self.following[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:

        self.following[followerId].discard(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
