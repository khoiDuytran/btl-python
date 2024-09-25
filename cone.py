import numpy as np
import matplotlib.pyplot as plt

# Set up the figure and axis
fig, ax = plt.subplots()

# Set background color
fig.patch.set_facecolor('white')  # Set the figure background to white
ax.set_facecolor('white')  # Set the plot (axes) background to white

# Define the cone parameters
height = 5  # Height of the cone
radius = 3  # Radius of the cone's base

# Fill the sides of the cone (triangle)
x_triangle = [-radius, 0, radius]  # x coordinates of the triangle (base and top)
y_triangle = [0, height, 0]  # y coordinates of the triangle (base and top)
ax.fill(x_triangle, y_triangle, 'b', alpha=0.7)  # Fill the triangle with blue color

# Draw the base of the cone (arc)
theta = np.linspace(-np.pi, 0, 100)  # Angle for the arc (half-circle)
x_base = radius * np.cos(theta)  # x coordinates of the arc
y_base = radius * np.sin(theta)  # y coordinates of the arc
ax.fill_between(x_base, y_base, color='b', alpha=0.7)  # Fill the base with blue color

# Remove axes and surrounding elements
ax.set_xticks([])  # Remove x-axis ticks
ax.set_yticks([])  # Remove y-axis ticks
ax.spines['top'].set_visible(False)  # Hide top axis line
ax.spines['right'].set_visible(False)  # Hide right axis line
ax.spines['left'].set_visible(False)  # Hide left axis line
ax.spines['bottom'].set_visible(False)  # Hide bottom axis line

# Set equal scaling and limit the view to the cone's area
ax.set_aspect('equal')
ax.set_xlim([-radius - 1, radius + 1])
ax.set_ylim([-radius - 1, height + 1])

# Show the plot
plt.title('Filled 2D Cone', pad=20)
plt.show()
