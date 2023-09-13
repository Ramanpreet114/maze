from a3_maze import Maze
# a1_partd.py
def find_path(the_maze, from_cell, to_cell):
    # Mark the current cell as visited
    the_maze.mark_cell(from_cell)

    # Start with a path containing only the current cell
    path = [from_cell]

    # If the current cell is the target cell, return the path
    if from_cell == to_cell:
        return path

    # Check the left cell
    left_cell = the_maze.get_left(from_cell)
    if left_cell != -1 and not the_maze.get_is_marked(left_cell):
        # Recursively find a path from the left cell to the target cell
        path += find_path(the_maze, left_cell, to_cell)
        if path[-1] == to_cell:
            return path

    # Check the right cell
    right_cell = the_maze.get_right(from_cell)
    if right_cell != -1 and not the_maze.get_is_marked(right_cell):
        # Recursively find a path from the right cell to the target cell
        path += find_path(the_maze, right_cell, to_cell)
        if path[-1] == to_cell:
            return path

    # Check the up cell
    up_cell = the_maze.get_up(from_cell)
    if up_cell != -1 and not the_maze.get_is_marked(up_cell):
        # Recursively find a path from the up cell to the target cell
        path += find_path(the_maze, up_cell, to_cell)
        if path[-1] == to_cell:
            return path

    # Check the down cell
    down_cell = the_maze.get_down(from_cell)
    if down_cell != -1 and not the_maze.get_is_marked(down_cell):
        # Recursively find a path from the down cell to the target cell
        path += find_path(the_maze, down_cell, to_cell)
        if path[-1] == to_cell:
            return path

    # If none of the neighboring cells leads to the target cell,
    # unmark the current cell and remove it from the path
    the_maze.unmark_cell(from_cell)
    path.pop()  # Remove current cell from path

    return path
