from a2d import Graph


def minimum_spanning_tree(graph):
    
    num_verts = graph.num_verts
    
    initial_vertx = 0
    
    list = [(weight, initial_vertx, to_idx) for to_idx, weight in graph.get_connected(initial_vertx)]
    
    # This code will heapify in upward  
    def Sort_upward(passed):
        parent = (passed - 1) // 2
        while passed > 0 and list[passed][0] < list[parent][0]:   # While loop 
            list[parent], list[passed]= list[passed], list[parent]
            passed = parent
            parent = (passed - 1) // 2

    def Sort_downward(passed):
        right_child = 2 * passed + 2
        left_child = 2 * passed + 1
        smallest = passed

        if left_child < len(list) and list[left_child][0] < list[smallest][0]:
            smallest = left_child
        if right_child < len(list) and list[right_child][0] < list[smallest][0]:
            smallest = right_child

        if smallest != passed:
            list[passed], list[smallest] = list[smallest], list[passed]
            Sort_downward(smallest)

    vertices = {initial_vertx}
    edges = []

    while list and len(vertices) < num_verts():
        
        #variable initialise
        weight, from_idx, to_idx = list[0]
        list[0] = list.pop()
        Sort_downward(0)

        while to_idx not in vertices:
            edges.append((from_idx, to_idx))
            vertices.add(to_idx)
            
            
            for to_idx_next, weight_next in graph.get_connected(to_idx):
                if to_idx_next not in vertices:
                    list.append((weight_next, to_idx, to_idx_next))
                    Sort_upward(len(list) - 1)

    return edges
