""" Program to visualize a network with provided boundary nodes """

import matplotlib.pyplot as plt

def display_points(points, hull, filename):
        plt.plot(points[:,0], points[:,1], 'o')
        for simplex in hull.simplices:
            plt.plot(points[simplex, 0], points[simplex, 1], 'k-')

        plt.plot(points[:, 0], points[:, 1], 'bo')
        plt.plot(points[hull.vertices, 0], points[hull.vertices, 1], 'r--', lw=1)
        plt.plot(points[hull.vertices[0], 0], points[hull.vertices[0], 1], 'go', lw=1) # to denote the starting point
        plt.savefig(filename)

