import math
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def sphere(radius):
  """
  This function calculates the volume of a sphere.

  Args:
      radius: The radius of the sphere.

  Returns:
      The volume of the sphere.
  """
  # Use math.pi to access the pi constant
  volume = (4/3) * math.pi * (radius**3)
  return volume

def main():
  # Get radius input from the user with error handling
  while True:
    try:
      radius = float(input("Enter the radius of the sphere: "))
      if radius <= 0:
        print("Radius cannot be negative or zero. Please enter a positive value.")
      else:
        break
    except ValueError:
      print("Invalid input. Please enter a number.")

  # Calculate the volume
  volume = sphere(radius)

  # Display the volume
  print(f"The volume of the sphere with radius {radius} is: {volume:.2f}")

  # Optional visualization
  # Create a 3D plot using a 3D axes object
  fig = plt.figure()
  ax = fig.add_subplot(111, projection='3d')

  # Generate points for the sphere surface
  u = np.linspace(0, 2 * np.pi, 20)
  v = np.linspace(0, np.pi, 20)
  x = radius * np.outer(np.cos(u), np.sin(v))
  y = radius * np.outer(np.sin(u), np.sin(v))
  z = radius * np.outer(np.ones(np.size(u)), np.cos(v))

  # Plot the surface with color and transparency
  ax.plot_surface(x, y, z, color='b', alpha=0.5)

  # Set labels and title for the axes
  ax.set_xlabel('X')
  ax.set_ylabel('Y')
  ax.set_zlabel('Z')
  ax.set_title(f"Sphere with radius {radius}")

  # Show the plot
  plt.show()

if __name__ == "__main__":
  main()