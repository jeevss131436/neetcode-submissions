class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = {}
        for i in range(numCourses):
            pre[i] = []

        for course, prereq in prerequisites:
            pre[course].append(prereq) 

        visited = set()

        def dfs(crs):
            if crs in visited:
                return False
            if pre[crs] == []:
                return True
            
            visited.add(crs)
            for pr in pre[crs]:
                if not dfs(pr): return False
            visited.remove(crs)
            pre[crs] = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        
        return True
