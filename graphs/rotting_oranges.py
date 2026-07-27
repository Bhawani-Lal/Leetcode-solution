from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        fresh_oranges = 0

        # Find all rotten oranges and count fresh oranges
        for row in range(rows):
            for col in range(cols):

                if grid[row][col] == 2:
                    queue.append((row, col))

                elif grid[row][col] == 1:
                    fresh_oranges += 1

        # No fresh oranges at the beginning
        if fresh_oranges == 0:
            return 0

        minutes = 0

        directions = [
            (-1, 0),  # Up
            (1, 0),   # Down
            (0, -1),  # Left
            (0, 1)    # Right
        ]

        while queue and fresh_oranges > 0:

            # All oranges currently in the queue
            # spread rot during the same minute
            for _ in range(len(queue)):

                row, col = queue.popleft()

                for dr, dc in directions:
                    new_row = row + dr
                    new_col = col + dc

                    if (
                        0 <= new_row < rows
                        and 0 <= new_col < cols
                        and grid[new_row][new_col] == 1
                    ):
                        # Make the fresh orange rotten
                        grid[new_row][new_col] = 2

                        fresh_oranges -= 1

                        queue.append((new_row, new_col))

            # One full minute has passed
            minutes += 1

        if fresh_oranges == 0:
            return minutes

        return -1
