class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        
        parent=[i for i in range(n)]
        def find(x):
            
            if parent[x]!=x:
                parent[x]=find(parent[x])

            return parent[x]

        
        def union(x,y):

            parentx=find(x)
            parenty=find(y)

            if parentx==parenty:
                return False
            
            parent[parentx]=parenty
            return True
        

        for edge in edges:
            u,v=edge
            union(u,v)
            print(parent)
        
        count=len(set(find(x) for x in range(n)))
        return count