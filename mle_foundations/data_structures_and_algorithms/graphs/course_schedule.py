class Solution:
    @staticmethod
    def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}

        for course, prerequisite in prerequisites:
            preMap[course].append(prerequisite)

        visited = set() #dfs path
        def dfs(course):
            if course in visited:
                return False
            if preMap[course] == []:
                return True
            visited.add(course)
            for pre in preMap[course]:
                if not dfs(pre):
                    return False
            visited.remove(course)
            preMap[course] = []
            return True  

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True  
                

