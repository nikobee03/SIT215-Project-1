import heapq
from coordinates import letter_to_coord

class Node:
    def __init__(self, position, cost, heuristic):
        self.position = position
        self.cost = cost
        self.heuristic = heuristic
        self.parent = None  # Add a parent attribute to track the path

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def astar_search(edge_costs, start, goal):
    open_set = []
    closed_set = set()

    start_node = Node(start, 0, heuristic(start, goal))
    heapq.heappush(open_set, start_node)

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.position == goal:
            # Path found, reconstruct and return it
            path = []
            while current_node:
                path.insert(0, current_node.position)
                current_node = current_node.parent
            return path

        closed_set.add(current_node.position)

        for neighbor in edge_costs[current_node.position]:
            if neighbor not in closed_set:
                cost = current_node.cost + edge_costs[current_node.position][neighbor]
                heuristic_val = heuristic(neighbor, goal)
                new_node = Node(neighbor, cost, heuristic_val)
                new_node.parent = current_node

                # Check if the neighbor is already in the open set with a lower cost
                existing_node = next((node for node in open_set if node.position == neighbor), None)
                if existing_node and existing_node.cost <= cost:
                    continue

                heapq.heappush(open_set, new_node)

    return None  # No path found

# Manhattan heuristic
def heuristic(start, goal):
    node_coord = letter_to_coord.get(start)
    goal_coord = letter_to_coord.get(goal)

    if isinstance(node_coord, tuple) and isinstance(goal_coord, tuple):
        return abs(node_coord[0] - goal_coord[0]) + abs(node_coord[1] - goal_coord[1])
    else:
        return 0

# Cost of each edge
edge_costs = {
    'A': {'B': 65.5},
    'B': {'A': 65.5, 'C': 25.4, 'H': 37},
    'C': {'B': 25.4, 'D': 22.2, 'I': 43.5},
    'D': {'C': 22.2, 'E': 11.8, 'J': 36.8},
    'E': {'D': 11.8, 'F': 31.4, 'K': 26.7},
    'F': {'E': 31.4, 'G': 19.1},
    'G': {'F': 19.1, 'L': 43.3},
    'H': {'B': 37, 'I': 17},
    'I': {'H': 17, 'C': 43.5, 'J': 29.3},
    'J': {'I': 29.3, 'D': 36.8, 'K': 26.5},
    'K': {'J': 26.5, 'E': 26.7, 'L': 29},
    'L': {'K': 29, 'G': 43.3}
}