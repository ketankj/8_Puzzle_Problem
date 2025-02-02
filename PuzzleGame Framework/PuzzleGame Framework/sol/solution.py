#This is the only file you need to work on. You do NOT need to modify other files

# Below are the functions you need to implement. For the first project, you only need to finish implementing iddfs() 
# ie iterative deepening depth first search


# here you need to implement the Iterative Deepening Search Method

# Function to perform Iterative Deepening Depth First Search on a given puzzle
def iterativeDeepening(puzzle):
    # Set to keep track of visited states during the search
    visited = set()
    # Goal state of the puzzle (sorted order)
    goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    
    # Maximum depth for the search
    max_depth = 20 
    
    # Loop through depth limits from 1 to max_depth
    for depth_limit in range(1, max_depth + 1):
        # Call depth_first_search with the current depth limit
        result = depth_first_search(puzzle, depth_limit, [puzzle], goal_state, visited)
        # If a solution is found, return the result
        if result:
            return result
    
    # If no solution is found within the depth limit, return an empty list
    return []


# Function to find valid neighbors for a given puzzle state
def neighbours(node):
    # Find the index of the empty tile (represented by 8 in the puzzle)
    empty_index = node.index(8)
    
    # Calculate the row and column of the empty tile in a 3x3 puzzle
    row = int(empty_index / 3)
    col = int(empty_index % 3)
    
    # Possible moves (up, down, left, right)
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    # List to store valid neighbor states
    valid_neighbors = []
    
    # Check each possible move
    for move in moves:
        new_row = row + move[0]
        new_col = col + move[1]

        # Check if the new position is within the bounds of a 3x3 puzzle
        if (0 <= new_row < 3) and (0 <= new_col < 3):
            # Calculate the new index of the empty tile after the move
            new_index = new_row * 3 + new_col
            # Create a new puzzle state by swapping the empty tile with the adjacent tile
            new_node = node[:]
            new_node[empty_index], new_node[new_index] = new_node[new_index], new_node[empty_index]
            # Add the new state to the list of valid neighbors
            valid_neighbors.append(new_node)
    
    # Return the list of valid neighbors
    return valid_neighbors

# Depth First Search function
def depth_first_search(current_state, depth, path, goal_state, visited):
    # If the current state is the goal state at the desired depth, return the path
    if depth == 0 and current_state == goal_state:
        # Extract and print the sequence of empty tile positions from the path
        swap_list = []
        for i in path[1:]:
            swap_list.append(i.index(8))
        print("Final Path:", swap_list)
        return swap_list
    
    # If the desired depth is not reached, continue the search
    elif depth > 0:
        # Iterate through valid neighbors of the current state
        for neighbor in neighbours(current_state):
            # Check if the neighbor state has not been visited
            if tuple(neighbor) not in visited:
                # Mark the neighbor state as visited
                visited.add(tuple(neighbor))
                # Recursively call depth_first_search with the neighbor state
                result = depth_first_search(neighbor, depth - 1, path + [neighbor], goal_state, visited)
                # If a solution is found in the recursive call, return the result
                if result:
                    return result
                # Remove the neighbor state from the set of visited states (backtrack)
                visited.remove(tuple(neighbor))
    
    # If no solution is found at the current depth, return an empty list
    return []



# This will be for next project
# A* algorithm for solving the 8-puzzle problem
def astar(puzzle):
    # Goal state of the puzzle (sorted order)
    goal_state = [0, 1, 2, 3, 4, 5, 6, 7, 8]

    # Heuristic function to estimate the cost from the current state to the goal state
    def heuristic(state):
        # A simple heuristic: count the number of misplaced tiles
        return sum(1 for i, j in zip(state, goal_state) if i != j)

    # Set to keep track of visited states during the search
    visited = set()

    # Initialize the start node with the heuristic value, cost, current state, and an empty path
    start_node = (heuristic(puzzle), 0, puzzle, [])
    
    # Priority queue to store nodes based on their priority value
    priority_queue = [start_node]

    # Main A* loop
    while priority_queue:
        # Extract the node with the minimum priority value from the priority queue
        _, cost, current_state, path = min(priority_queue)
        priority_queue.remove((_, cost, current_state, path))

        # Check if the current state is the goal state
        if current_state == goal_state:
            # Print the final path and return it
            print("Final Path:", path)
            return path

        # Check if the current state has already been visited
        if tuple(current_state) in visited:
            continue

        # Mark the current state as visited
        visited.add(tuple(current_state))

        # Find the index of the empty tile in the current state
        empty_index = current_state.index(8)

        # Define possible neighbors and their corresponding move directions
        neighbors = [(empty_index - 1, "Left"), (empty_index + 1, "Right"),
                     (empty_index - 3, "Up"), (empty_index + 3, "Down")]

        # Explore each neighbor
        for neighbor_index, move_direction in neighbors:
            # Check if the neighbor index is within the valid range (0 to 8)
            if 0 <= neighbor_index < 9:
                # Create a new state by swapping the empty tile with the neighbor tile
                new_state = current_state.copy()
                new_state[empty_index], new_state[neighbor_index] = new_state[neighbor_index], new_state[empty_index]
                # Create a new node for the neighbor with updated cost, heuristic, state, and path
                neighbor_node = (cost + 1 + heuristic(new_state), cost + 1, new_state, path + [neighbor_index])
                # Add the neighbor node to the priority queue
                priority_queue.append(neighbor_node)

    # If no solution is found within the loop, return an empty list
    return []

