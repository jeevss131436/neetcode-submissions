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
            for nei in node.neighbors:
                new_val.neighbors.append(dfs(nei))
            return new_val
        return dfs(node) if node else None