import math

# Function to calculate Euclidean distance between two points
def euclidean_distance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# List of points (coordinates)
points = [(2, 3), (5, 7), (8, 1), (4, 6)]

# Calculate Euclidean distance between each pair of points
for i in range(len(points)):
    for j in range(i+1, len(points)):
        distance = euclidean_distance(points[i], points[j])
        print(f"Distance between {points[i]} and {points[j]} is: {distance}")
