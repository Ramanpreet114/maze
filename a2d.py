class Graph:                      

    
    def __init__(self,number_of_verts):                          
        self.graph  = [[] for i  in range(number_of_verts)]
        self. number_of_edges = 0                             
        self.number_of_verts = number_of_verts                   
    

    def add_vertex(self):                                         
        new_graph = [[] for i  in range(self.number_of_verts  + 1)]
        self.number_of_verts += 1
        for i in range(self.number_of_verts - 1):
            new_graph[i] = self.graph[i]
        self.graph = new_graph
        
    def num_edges(self):               
        return self.number_of_edges
    
    def num_verts(self):               
        return self.number_of_verts
    
    def add_edge(self, from_idx, to_idx, weight=1):      
        if from_idx < 0 or from_idx >= self.num_verts() or to_idx < 0 or to_idx >= self.num_verts() :
            return False
        for edge in self.graph[from_idx]:
                if edge[0] == to_idx:
                    return False
        self.graph[from_idx].append((to_idx, weight))
        self. number_of_edges += 1
        return True

    def has_edge(self, from_idx, to_idx):                 
        if from_idx >= 0 and from_idx < self.num_verts() and to_idx >= 0 and to_idx < self.num_verts() :
            for edge in self.graph[from_idx]:
                if edge[0] == to_idx:
                    return True
        return False
    
    def edge_weight(self, from_idx, to_idx):             
        if self.has_edge(from_idx, to_idx):
            for edge in self.graph[from_idx]:
                if edge[0] == to_idx:
                    return edge[1]
        return None
    
    def get_connected(self, v):                        
        if v < 0 or v >= self.num_verts():
            return []
        return self.graph[v]
            

     



                     
        
	

		
