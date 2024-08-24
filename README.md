# SIT215-Project-1
# Wheelchair Navigation System

## Overview

The Wheelchair Navigation System project focuses on developing a route-planning application specifically designed for wheelchair users. This application aims to optimize navigation by considering critical factors such as path width, terrain, and slope, which are often overlooked by standard navigation tools. The project utilizes computational intelligence concepts and problem-solving techniques to create a more accessible routing solution.

## Key Features

- **Route Optimization**: Calculates the most accessible path for wheelchair users, considering distance, path width, terrain, and slope.
- **Path Cost Categories**: Implements a points system to evaluate paths based on accessibility criteria, ensuring routes are not only the shortest but also the safest.
- **User-Friendly Interface**: Provides a graphical user interface (GUI) that allows users to input start and end points easily and view the calculated path visually.
- **Data Collection and Analysis**: Utilizes both computer applications and physical surveys to gather data on path conditions and accessibility.

## Technologies

- Python
- Tkinter (for GUI)
- OSMnx and Matplotlib (for map visualization)
- Google Earth Pro (for terrain analysis)

## Usage

1. **Install the required dependencies**:
   - Python
   - Tkinter
   - OSMnx
   - Matplotlib

2. **Run the `main_app.py` script**:
   ```bash
   python main_app.py
   ```

3. **Enter the start and end points in the GUI**:
   - The GUI will display the calculated path and its accessibility score.

4. **View the path on the map**:
   - The GUI will also display a visual representation of the calculated path on a map.

## Example Code

```python
def calculate_path_cost(distance, width, terrain, slope):
    cost = 0
    cost += distance / 10  # 1 point for every 10 m
    if width < 1.2:
        cost += 10  # Points for narrow paths
    cost += terrain * 2  # Points for terrain issues
    if slope > 5:
        cost += 15  # Points for steep slopes
    return cost
```

This function calculates the total cost of a path based on various accessibility factors, allowing the system to evaluate and compare different routes effectively.

## License

This project is licensed under the [MIT License](LICENSE).

Citations:
[1] https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/17452009/4082166e-a297-469e-ac7a-fbf3b1ecc1bb/Assignment-1.pdf
