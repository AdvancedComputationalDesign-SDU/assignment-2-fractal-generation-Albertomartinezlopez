import matplotlib.pyplot as plt
import math
import random
from shapely.geometry import LineString

def generate_edgy_coral(point, angle, length, depth, max_depth, branch_width):
    """
    Recursive function to generate a coral-like fractal pattern with separated branches
    and a color gradient.

    Parameters:
    - point: Tuple (x, y), starting coordinate of the branch.
    - angle: Float, angle in degrees for the current branch direction.
    - length: Float, length of the current branch.
    - depth: Int, current depth in the recursion (used for color and termination).
    - max_depth: Int, maximum recursion depth to control the fractal's complexity.
    - branch_width: Float, width of each branch to simulate the coral outline.
    """
    if depth > max_depth or branch_width < 0.1:  
        return

    # Define curve points to create slight curvature in the branch
    midpoint_angle = angle + random.uniform(-10, 10)  # Random midpoint for curvature
    midpoint_x = point[0] + (length / 2) * math.cos(math.radians(midpoint_angle))
    midpoint_y = point[1] + (length / 2) * math.sin(math.radians(midpoint_angle))
    end_x = point[0] + length * math.cos(math.radians(angle))
    end_y = point[1] + length * math.sin(math.radians(angle))
    end_point = (end_x, end_y)

    # Create the branch as a LineString with a midpoint for a slight curve
    branch_line = LineString([point, (midpoint_x, midpoint_y), end_point])
    branch_polygon = branch_line.buffer(branch_width, cap_style=2)  

    # Color gradient based on depth
    color = plt.cm.plasma(depth / max_depth)

    # Plot the branch using matplotlib's fill function if the polygon is valid and has an exterior
    if branch_polygon.is_valid and not branch_polygon.is_empty:
        x, y = branch_polygon.exterior.xy  
        plt.fill(x, y, facecolor=color, edgecolor=color, alpha=0.8)

    # Reduce length and width smoothly to create a tapered, natural effect
    new_length = length * 0.9
    new_branch_width = branch_width * 0.7

    # Small randomized branching angles for organic effect
    angle_variation = random.uniform(-10, 10)

    # Recursive calls for organic branches
    generate_edgy_coral(end_point, angle + 25 + angle_variation, new_length, depth + 1, max_depth, new_branch_width)
    generate_edgy_coral(end_point, angle - 25 + angle_variation, new_length, depth + 1, max_depth, new_branch_width)

# Main execution
start_point = (0, 0)      
initial_angle = 90        
initial_length = 100      
max_depth = 6             
initial_branch_width = 8  

plt.figure(figsize=(8, 8))  
generate_edgy_coral(start_point, initial_angle, initial_length, 0, max_depth, initial_branch_width)
plt.axis('equal')
plt.axis('off') 
plt.show()       
