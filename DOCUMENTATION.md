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

*(Provide a concise explanation of your code, focusing on recursion and geometric manipulations. Discuss how your approach generates the final fractal pattern and the mathematical principles involved.)*

Example:

In my implementation, the `generate_fractal` function recursively draws line segments representing branches of a fractal tree. The function calculates the end point of each line using trigonometric functions based on the current angle and length.

At each recursion step, the function:

- Decreases the `length` by multiplying it with `length_scaling_factor`.
- Adjusts the `angle` by adding or subtracting `angle_change` to create branching.
- Calls itself recursively for each branch until the `recursion_depth` reaches zero.

This approach creates a self-similar pattern characteristic of fractals, where each branch splits into smaller branches in a consistent manner.

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