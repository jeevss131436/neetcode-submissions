class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {}
        for i in range(numCourses):
            preMap[i] = []
        for crs, pre in prerequisites:
            preMap[crs].append(pre)
    
        output = []
        path = set()
        visited = set()

        def dfs(crs):
            if crs in path:
                return False
            if crs in visited:
                return True

            path.add(crs)
            for pre in preMap[crs]:
                if dfs(pre) == False:
                    return False
            path.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True
        
        for pre in range(numCourses):
            if dfs(pre) == False:
                return []
        return output   