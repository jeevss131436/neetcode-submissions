
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        node_dict = {}

        def dfs(node):
            if node in node_dict:
                return node_dict[node]
            new_val = Node(node.val)
            node_dict[node] = new_val
            for neighbor in node.neighbors:
                new_val.neighbors.append(dfs(neighbor))
            return new_val
            
        if node:
            return dfs(node)
        else:
            return None