import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import ConvexHull

# generates 2D data, add flags to make it 3D
def gen_data(number_of_points):
        points = np.random.rand(number_of_points, 2)
        return points, ConvexHull(points)
    
def get_hull(points):
    return ConvexHull(points)

def test_ground_truth(points, hull):
        plt.plot(points[:,0], points[:,1], 'o')
        for simplex in hull.simplices:
            plt.plot(points[simplex, 0], points[simplex, 1], 'k-')

        plt.plot(p[:, 0], p[:, 1], 'bo')
        plt.plot(p[h.vertices, 0], p[h.vertices, 1], 'r--', lw=1)
        plt.plot(p[h.vertices[0], 0], p[h.vertices[0], 1], 'go', lw=1) # to denote the starting point
        plt.show()

