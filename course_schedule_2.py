from typing import List
from collections import deque

class Solution:
    def findOrder(
        self,
        numCourses: int,
        prerequisites: List[List[int]]
    ) -> List[int]:

        # Create adjacency list
        graph = [[] for _ in range(numCourses)]

        # indegree[i] stores how many prerequisites course i has
        indegree = [0] * numCourses

        # Build the graph
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1

        queue = deque()

        # Add all courses having no prerequisites
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        order = []

        while queue:
            current_course = queue.popleft()

            # Add completed course to the answer
            order.append(current_course)

            # Remove this prerequisite from dependent courses
            for next_course in graph[current_course]:
                indegree[next_course] -= 1

                # All prerequisites are now completed
                if indegree[next_course] == 0:
                    queue.append(next_course)

        # If all courses were completed, return the order
        if len(order) == numCourses:
            return order

        # Otherwise, a cycle exists
        return []
