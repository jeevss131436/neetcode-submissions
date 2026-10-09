class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {}
        for i in range(numCourses):
            preMap[i] = []
        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        output = []
        visited = set()
        cycle = set()

        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            
            visited.add(crs)
            cycle.add(crs)
            
            for pre in preMap[crs]:
                if dfs(pre) == False:
                    return False
            
            output.append(crs)
            cycle.remove(crs)
            preMap[crs] = []
            return True

        for crs in preMap:
            if dfs(crs) == False:
                return []
        return output