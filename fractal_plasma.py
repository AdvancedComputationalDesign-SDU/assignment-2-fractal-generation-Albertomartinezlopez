import matplotlib.pyplot as plt
import math
import random

def generate_coral_fractal(point, angle, length, depth, max_depth):
    """
    Recursive function to generate a coral-like fractal with random offsets and color gradient.
    
    Parameters:
    - point: Tuple (x, y), starting coordinate.
    - angle: Float, angle in degrees for the current branch direction.
    - length: Float, length of the current branch.
    - depth: Int, current depth in the recursion (used for color and termination).
    - max_depth: Int, maximum recursion depth to control the fractal's complexity.
    """
    if depth > max_depth:  # Stop recursion
        return
    
    # Calculate the end point of the branch
    end_x = point[0] + length * math.cos(math.radians(angle))
    end_y = point[1] + length * math.sin(math.radians(angle))
    end_point = (end_x, end_y)
    
    # Plot the line with color fading from deep purple to light yellow
    plt.plot([point[0], end_x], [point[1], end_y], color=plt.cm.plasma(depth / max_depth), linewidth=1)

    # Reduce length slightly for the next branches and add random offset
    new_length = length * 0.75
    offset = random.uniform(-10, 10)  # Random angle offset to create organic look
    
    # Recursive calls with random offsets for branching effect
    generate_coral_fractal(end_point, angle + 30 + offset, new_length, depth + 1, max_depth)
    generate_coral_fractal(end_point, angle - 30 + offset, new_length, depth + 1, max_depth)

# Main execution
start_point = (0, 0) 
initial_angle = 90   
initial_length = 100 
max_depth = 7        

plt.figure(figsize=(8, 8))  # Plot size
generate_coral_fractal(start_point, initial_angle, initial_length, 0, max_depth)
plt.axis('off')  # Hide axis
plt.show()       
