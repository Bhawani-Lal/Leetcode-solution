from typing import List
from collections import deque

class Solution:
    def canFinish(
        self,
        numCourses: int,
        prerequisites: List[List[int]]
    ) -> bool:

        # Graph adjacency list
        graph = [[] for _ in range(numCourses)]

        # indegree[i] tells how many prerequisites course i has
        indegree = [0] * numCourses

        # Build the graph
        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)
            indegree[course] += 1

        queue = deque()

        # Courses with no prerequisites can be taken immediately
        for course in range(numCourses):
            if indegree[course] == 0:
                queue.append(course)

        completed_courses = 0

        while queue:
            current_course = queue.popleft()

            # We have completed this course
            completed_courses += 1

            # Check all courses depending on current_course
            for next_course in graph[current_course]:
                indegree[next_course] -= 1

                # All prerequisites of next_course are completed
                if indegree[next_course] == 0:
                    queue.append(next_course)

        return completed_courses == numCourses
        
