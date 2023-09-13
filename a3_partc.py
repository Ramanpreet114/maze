import random
from a2d import Graph
from a3_partb import minimum_spanning_tree


def generate_maze(number_of_rows, number_of_columns):
    
    maze_walls = []
    for rows in range(number_of_rows):
        for columns in range(number_of_columns):
            maze_cells = rows * number_of_columns + columns
            if columns != number_of_columns - 1:  
                maze_walls.append((maze_cells, maze_cells+1))
                
            if rows != number_of_rows - 1:  
                maze_walls.append((maze_cells, maze_cells+number_of_columns))

    graph = Graph(number_of_rows * number_of_columns)
    
    for wall in maze_walls:
        randomm = random.randint(1, 50) 
        graph.add_edge(wall[0], wall[1], randomm)
        graph.add_edge(wall[1], wall[0], randomm)
    path = minimum_spanning_tree(graph)
    maze_maze_walls = []
    index = 0

    while index < len(maze_walls):
        wall = maze_walls[index]
        if wall not in path and (wall[1], wall[0]) not in path:
            maze_maze_walls.append(wall)
        index += 1

    return maze_maze_walls
