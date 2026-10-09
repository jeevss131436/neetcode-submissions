class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {}
        for i in range(numCourses):
            preMap[i] = []
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        visited = set()
        path = set()
        
        def dfs(crs):
            if crs in visited:
                return False
            if preMap[crs] == []:
                return True
            
            visited.add(crs)

            for pre in preMap[crs]:
                if dfs(pre) == False:
                    return False
            visited.remove(crs)
            preMap[crs] = []
            return True
        
        for crs in preMap:
            if dfs(crs) == False:
                return False
        return True