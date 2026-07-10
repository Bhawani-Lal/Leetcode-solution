import heapq
from collections import Counter, deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        frequency = Counter(tasks)

        maxHeap = [-count for count in frequency.values()]
        heapq.heapify(maxHeap)

        waiting = deque()
        time = 0

        while maxHeap or waiting:

            time += 1

            if maxHeap:
                count = heapq.heappop(maxHeap) + 1

                if count < 0:
                    waiting.append((count, time + n))

            if waiting and waiting[0][1] == time:
                count, availableTime = waiting.popleft()
                heapq.heappush(maxHeap, count)

        return time
