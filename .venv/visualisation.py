import osmnx as ox
import matplotlib.pyplot as plt
from coordinates import letter_to_coord
#from gui import start_entry, end_entry

def visualise_map(graph, start, goal, path):
    # Create a map from coordinates
    centre_point = (-37.853469, 145.123745)
    G = ox.graph_from_point(centre_point, dist=750, retain_all=False)
    fig, ax = ox.plot_graph(G, show=False, close=False, node_color="grey")

    # Plot each node on the map & label them
    for node, coord in letter_to_coord.items():
        x = coord[0]
        y = coord[1]
        ax.scatter(x, y, c='red')
        ax.annotate(node, (x,y), fontsize=12, c='white', weight='bold')

    # Show the calculated path
    if path:
        for i in range(len(path) - 1):
            start_node = path[i]
            end_node = path[i + 1]
            start_coord = letter_to_coord[start_node]
            end_coord = letter_to_coord[end_node]
            ax.plot([start_coord[0], end_coord[0]], [start_coord[1], end_coord[1]], color='green', linewidth=3)

    plt.show()