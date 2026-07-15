class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        redudant_edges=[]

        parent=[i for i in range(len(edges)+1)]
        print(parent)

        def find(x):

            if parent[x]!=x:
                parent[x]=find(parent[x])
            
            return parent[x]
        

        def union(x,y):
            print(x,y)
            parentx=find(x)
            parenty=find(y)

            if parentx==parenty:
                return False
            
            parent[parentx]=parenty

            return True
        

        n=len(edges)+1

        for edge in edges:
            u,v=edge
            if not union(u,v):
                redudant_edges.append([u,v])
        
        return redudant_edges[-1]
