class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preNum = {}
        
        for i in range(numCourses):
            preNum[i] = []
        for crs, pre in prerequisites:
            preNum[crs].append(pre)
        
        visited = set()
        def dfs(crs):
            if crs in visited:
                return False
            if preNum[crs] == []:
                return True
            
            visited.add(crs)
            for pre in preNum[crs]:
                if dfs(pre) == False:
                    return False
            visited.remove(crs)
            preNum[crs] = []
            return True
        
        for crs in range(numCourses):
            if dfs(crs) == False:
                return False
        return True