# Assignment 2: Fractal Generation Documentation

## Table of Contents

- [Pseudo-Code](#pseudo-code)
- [Technical Explanation](#technical-explanation)
- [Results](#results)
- [Challenges and Solutions](#challenges-and-solutions)
- [References](#references)

---

## Pseudo-Code


1. Import necessary libraries: matplotlib, math, random, and shapely.

2. Define a function `generate_edgy_coral` with parameters:
   - `point`: Starting coordinate of the branch.
   - `angle`: Initial direction of the branch in degrees.
   - `length`: Length of the current branch.
   - `depth`: Current recursion level.
   - `max_depth`: Maximum recursion level allowed.
   - `branch_width`: Width of the branch.

3. Check if `depth` exceeds `max_depth` or if `branch_width` is less than a threshold.
   - If so, stop further recursion.

4. Define control points for creating a curved path:
   - Start with `point` as the first control point.
   - Calculate additional control points based on `angle`, `length`, and small random variations.
   - Calculate the final endpoint with a small angle variation.
   
5. Create a line for the branch using `LineString` with the control points.
   - Create a polygon outline around this line with `branch_width`.

6. Set branch color based on the `depth` to create a color gradient effect.

7. If the polygon is valid, plot it using `matplotlib` with filled color.

8. Reduce `length` and `branch_width` for tapering effect:
   - Calculate `new_length` as `length * 0.9`.
   - Calculate `new_branch_width` as `branch_width * 0.7`.

9. Apply a small random angle variation for natural appearance.

10. Recursively call `generate_edgy_coral` twice to create two new branches:
    - One at `angle + 25 + angle_variation`.
    - Another at `angle - 25 + angle_variation`.

11. In the main execution:
    - Set the starting point, initial angle, initial branch length, max depth, and branch width.
    - Initialize a plotting area with `matplotlib`.
    - Call `generate_edgy_coral` with initial parameters.
    - Display the plot.


---

## Technical Explanation

To create the coral pattern, I began by defining a recursive function, generate_edgy_coral, that took in several parameters: point for the starting position, angle for direction, length, depth level, max_depth for recursion limit, and branch_width. At the start of each call, I checked if the depth exceeded max_depth or if the branch_width was too narrow (less than 0.1); if either condition was met, I used a return statement to stop further recursion.

Within each branch creation, I defined multiple control points by iterating through num_midpoints and adding slight random angle adjustments. I calculated each midpoint using trigonometric functions (math.cos and math.sin) for realistic curvature, appending each point to a list, control_points. After adding the endpoint with a small angle variation, I used LineString(control_points) from Shapely to create a curved line that represented the branch’s path. Using branch_line.buffer(branch_width, cap_style=2), I wrapped this line in a polygon outline.

For visual depth, I applied a color gradient from plt.cm.plasma based on the depth divided by max_depth, and filled each branch using plt.fill. If branch_polygon was valid and non-empty, I retrieved its exterior.xy to extract the x and y coordinates for plotting.

Next, I adjusted length and branch_width by multiplying each by a constant (0.9 and 0.7, respectively) for a natural tapering effect. I also used a random angle variation with random.uniform(-10, 10) to create two recursive calls for the left and right branches with adjusted angles.

In the main code, I initialized parameters like start_point, initial_angle, initial_length, max_depth, and initial_branch_width. I set up a plotting area with plt.figure, called generate_edgy_coral to start the recursive pattern, and used plt.show() to display the resulting fractal, which featured organic, branching coral shapes with smooth color gradients and tapered branches.

---

## Results

*(Include images of your generated fractal patterns, and discuss any observations or interesting findings.)*

Example:

### Fractal Pattern 1: Basic Fractal Tree

![Fractal Tree](images/example.png)

- **Parameters**:
  - `angle_change`: 30°
  - `length_scaling_factor`: 0.7
  - `recursion_depth`: 5
- **Observations**:
  - The fractal tree exhibits symmetry and balance.
  - As the recursion depth increases, the level of detail in the branches increases.

*(Repeat for other fractal patterns.)*

---

## Challenges and Solutions

*(Discuss any challenges you faced during the assignment and how you overcame them.)*

Example:

- **Challenge**: Managing the growing number of line segments and ensuring they are correctly plotted.
  - **Solution**: Stored all line segments in a list and plotted them after the recursion completed.

- **Challenge**: Implementing randomness without losing the overall structure.
  - **Solution**: Introduced randomness within controlled bounds for angles and lengths.

---

## References

*(List any resources you used or found helpful during the assignment.)*

- **Shapely Manual**: [https://shapely.readthedocs.io/en/stable/manual.html](https://shapely.readthedocs.io/en/stable/manual.html)
- **Matplotlib Pyplot Tutorial**: [https://matplotlib.org/stable/tutorials/introductory/pyplot.html](https://matplotlib.org/stable/tutorials/introductory/pyplot.html)

---

*(Feel free to expand upon these sections to fully capture your work and learning process.)*