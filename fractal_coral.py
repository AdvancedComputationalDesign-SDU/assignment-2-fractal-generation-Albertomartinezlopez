import matplotlib.pyplot as plt
import math
import random
from shapely.geometry import Polygon, LineString, MultiPolygon
from shapely.affinity import translate, rotate

def generate_coral_polygon(point, angle, length, depth, max_depth, branch_width):
    """
    Recursive function to generate a coral-like fractal pattern with filled shapes.
    
    Parameters:
    - point: Tuple (x, y), starting coordinate of the branch.
    - angle: Float, angle in degrees for the current branch direction.
    - length: Float, length of the current branch.
    - depth: Int, current depth in the recursion (used for color and termination).
    - max_depth: Int, maximum recursion depth to control the fractal's complexity.
    - branch_width: Float, width of each branch to simulate the coral outline.
    """
    if depth > max_depth:  
        return
    
    # Calculate the main branch line
    end_x = point[0] + length * math.cos(math.radians(angle))
    end_y = point[1] + length * math.sin(math.radians(angle))
    end_point = (end_x, end_y)
    
    # Create a filled polygon to simulate the branch shape
    main_line = LineString([point, end_point])
    branch_polygon = main_line.buffer(branch_width, cap_style=2)
    
    # Debugging output to check geometry status
    print(f"Depth {depth}: Geometry type: {branch_polygon.geom_type}, Is valid: {branch_polygon.is_valid}, Is empty: {branch_polygon.is_empty}")
    
    # Handle cases where the buffer may produce a MultiPolygon or empty geometry
    if branch_polygon.is_empty:
        return
    elif isinstance(branch_polygon, MultiPolygon):
        for poly in branch_polygon:
            if poly.exterior:
                x, y = poly.exterior.xy
                color = plt.cm.plasma(depth / max_depth)
                plt.fill(x, y, facecolor=color, edgecolor=color, alpha=0.8)
    elif isinstance(branch_polygon, Polygon):
        if branch_polygon.exterior:
            x, y = branch_polygon.exterior.xy
            color = plt.cm.plasma(depth / max_depth)
            plt.fill(x, y, facecolor=color, edgecolor=color, alpha=0.8)
    
    # Reduce length and apply random angle offset for the next branches
    new_length = length * 0.7
    random_offset = random.uniform(-15, 15)
    
    # Recursive calls with offsets for branching effect
    generate_coral_polygon(end_point, angle + 30 + random_offset, new_length, depth + 1, max_depth, branch_width * 0.8)
    generate_coral_polygon(end_point, angle - 30 + random_offset, new_length, depth + 1, max_depth, branch_width * 0.8)

# Main execution
start_point = (0, 0)     
initial_angle = 90       
initial_length = 100      
max_depth = 5             
initial_branch_width = 10 
plt.figure(figsize=(8, 8))  
generate_coral_polygon(start_point, initial_angle, initial_length, 0, max_depth, initial_branch_width)
plt.axis('equal')
plt.axis('off')  
plt.show()       
