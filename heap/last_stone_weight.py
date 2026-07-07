class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
                # Convert to Max Heap
        stones = [-stone for stone in stones]
        heapq.heapify(stones)

        while len(stones) > 1:

            first = -heapq.heappop(stones)
            second = -heapq.heappop(stones)

            if first != second:
                heapq.heappush(stones, -(first - second))

        if stones:
            return -stones[0]

        return 0
