from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        rows = len(heights)
        cols = len(heights[0])

        # Cells that can reach each ocean
        pacific = set()
        atlantic = set()

        def dfs(row, col, visited, previous_height):
            
            # Check whether the cell is outside the grid
            if row < 0 or row >= rows or col < 0 or col >= cols:
                return

            # Avoid visiting the same cell again
            if (row, col) in visited:
                return

            # Moving backwards:
            # current cell must be greater than or equal to previous cell
            if heights[row][col] < previous_height:
                return

            visited.add((row, col))

            current_height = heights[row][col]

            # Visit four directions
            dfs(row - 1, col, visited, current_height)  # Up
            dfs(row + 1, col, visited, current_height)  # Down
            dfs(row, col - 1, visited, current_height)  # Left
            dfs(row, col + 1, visited, current_height)  # Right

        # Start from left and right borders
        for row in range(rows):
            dfs(row, 0, pacific, heights[row][0])
            dfs(row, cols - 1, atlantic, heights[row][cols - 1])

        # Start from top and bottom borders
        for col in range(cols):
            dfs(0, col, pacific, heights[0][col])
            dfs(rows - 1, col, atlantic, heights[rows - 1][col])

        result = []

        # Find cells present in both sets
        for row in range(rows):
            for col in range(cols):
                if (row, col) in pacific and (row, col) in atlantic:
                    result.append([row, col])

        return result
