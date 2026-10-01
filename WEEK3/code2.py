import pandas as pd
import numpy as np
from scipy.spatial import distance

pointA = [1, 2, 3]
pointB = [4, 5, 6]

# p = 1 → Manhattan Distance
d1 = distance.minkowski(pointA, pointB, p=1)
s1 = 1 / (1 + d1)

# p = 2 → Euclidean Distance
d2 = distance.minkowski(pointA, pointB, p=2)
s2 = 1 / (1 + d2)

# p = 3 → Minkowski Distance
d3 = distance.minkowski(pointA, pointB, p=3)
s3 = 1 / (1 + d3)

print("p=1 Distance:", d1)
print("p=1 Similarity:", s1)

print("p=2 Distance:", d2)
print("p=2 Similarity:", s2)

print("p=3 Distance:", d3)
print("p=3 Similarity:", s3)

# Euclidean Distance
euclidean_dist = distance.euclidean(pointA, pointB)
print("Euclidean Distance:", euclidean_dist)

# Euclidean Similarity
euclidean_similarity = 1 / (1 + euclidean_dist)
print("Euclidean Similarity:", euclidean_similarity)

# Manhattan Distance
manhattan_dist = distance.cityblock(pointA, pointB)
print("Manhattan Distance:", manhattan_dist)