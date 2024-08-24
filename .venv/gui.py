import tkinter as tk
from tkinter import ttk
import matplotlib
matplotlib.use('TkAgg')
from astar import astar_search, edge_costs
from visualisation import visualise_map
from coordinates import letter_to_coord

def display_path():
    # Get start and end points from input fields
    start = start_entry.get()
    goal = end_entry.get()
    
    # Perform A* search to find the path
    path = astar_search(edge_costs, start, goal)
    
    # Check if start or end points are invalid
    if start not in letter_to_coord or goal not in letter_to_coord:
        path_text.delete('1.0', tk.END)
        path_text.insert(tk.END, "Invalid start or end point")
        return
    
    # If path is found, display it and visualize it on the map
    if path:
        path_text.delete('1.0', tk.END)
        path_text.insert(tk.END, f"Path found: {', '.join(path)}")
        visualise_map(edge_costs, start, goal, path)
    else:
        # If no path is found, display message
        path_text.delete('1.0', tk.END)
        path_text.insert(tk.END, "No path found")

# Create the main application window
root = tk.Tk()
root.title("Wheelchair Navigation")

# Create input fields for start and end points
start_label = ttk.Label(root, text="Start:")
start_label.grid(row=0, column=0, padx=10, pady=10)
start_entry = ttk.Entry(root)
start_entry.grid(row=0, column=1, padx=10, pady=10)

end_label = ttk.Label(root, text="End:")
end_label.grid(row=1, column=0, padx=10, pady=10)
end_entry = ttk.Entry(root)
end_entry.grid(row=1, column=1, padx=10, pady=10)

# Create a button to display the path
display_button = ttk.Button(root, text="Find Path", command=display_path)
display_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Create a text area to display the path
path_text = tk.Text(root, height=5, width=50)
path_text.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
