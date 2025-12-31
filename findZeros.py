import numpy as np

arr_2d = np.array([[1, 0, 3], [0, 5, 6], [7, 8, 0]])

# Using np.argwhere()
zero_coordinates = np.argwhere(arr_2d == 0)

print("The array looks like this:")
print(arr_2d)
print("\nCoordinates of zero elements (NxD array):")
print(zero_coordinates)
print("\nAccessing coordinates:")
# The output is a 2D array: [[0, 1], [1, 0], [2, 2]]
for coords in zero_coordinates:
    print(f"Zero at coordinates: {coords}")
