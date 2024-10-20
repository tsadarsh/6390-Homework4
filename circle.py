import math

def generate_circle_points_and_weights(diameter):
    radius = diameter // 2
    cx, cy = radius, radius
    points = []
    weights = []
    
    # Maximum possible distance from the center (i.e., the radius)
    max_distance = math.sqrt(2 * (radius**2))
    
    # Loop over a square that bounds the circle
    for y in range(diameter + 1):
        for x in range(diameter + 1):
            dist_from_center = math.sqrt((x - cx)**2 + (y - cy)**2)
            if dist_from_center <= radius:
                # Append point (x, y, z)
                points.append([x, y, 0])
                # Calculate and append weight
                weight = 1 - (dist_from_center / max_distance)
                weights.append(round(weight, 2))  # Weight rounded to 2 decimal places
    
    return points, weights
