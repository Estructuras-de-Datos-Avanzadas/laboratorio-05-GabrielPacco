# MTree Implementation

import sys
import os
import math
import random
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation
from matplotlib import rc
from matplotlib import rcParams

# Global Variables
# Number of dimensions
D = 2
# Number of points
N = 100
# Number of clusters
K = 3
# Number of iterations
I = 100
# Number of points per cluster
Nk = N/K

# Generate random points
def generatePoints():
    # Generate random points
    points = np.random.rand(N,D)
    # Assign points to clusters
    for i in range(0,N):
        points[i] = points[i] + (i/Nk)*np.ones(D)
    return points

# Generate random centroids
def generateCentroids():
    # Generate random centroids
    centroids = np.random.rand(K,D)
    # Assign centroids to clusters
    for i in range(0,K):
        centroids[i] = centroids[i] + i*np.ones(D)
    return centroids

# Calculate distance between two points
def distance(p1,p2):
    return np.linalg.norm(p1-p2)

# Calculate distance between a point and a centroid
def distanceToCentroid(p,c):
    return distance(p,c)

# Calculate distance between two centroids

def distanceBetweenCentroids(c1,c2):
    return distance(c1,c2)

# Calculate distance between a point and a cluster
def distanceToCluster(p,cluster):
    minDist = sys.maxint
    for c in cluster:
        dist = distanceToCentroid(p,c)
        if dist < minDist:
            minDist = dist
    return minDist

# Function to Insert a point into Mtree
def insertPoint(p,mtree):
    # Find the closest centroid
    minDist = sys.maxint
    minCentroid = 0
    for i in range(0,K):
        dist = distanceToCentroid(p,centroids[i])
        if dist < minDist:
            minDist = dist
            minCentroid = i
    # Insert point into the cluster
    mtree[minCentroid].append(p)
    return mtree

# Function to Insert a centroid into Mtree
def insertCentroid(c,mtree):
    # Insert centroid into the cluster
    mtree.append(c)
    return mtree

# Function to Search for a point in Mtree
def searchPoint(p,mtree):
    # Find the closest centroid
    minDist = sys.maxint
    minCentroid = 0
    for i in range(0,K):
        dist = distanceToCentroid(p,centroids[i])
        if dist < minDist:
            minDist = dist
            minCentroid = i
    # Search point in the cluster
    for c in mtree[minCentroid]:
        if np.array_equal(c,p):
            return True
    return False

# Function to Search for a centroid in Mtree
def searchCentroid(c,mtree):
    # Search centroid in the cluster
    for c1 in mtree:
        if np.array_equal(c1,c):
            return True
    return False

# Function to Delete a point from Mtree
def deletePoint(p,mtree):
    # Find the closest centroid
    minDist = sys.maxint
    minCentroid = 0
    for i in range(0,K):
        dist = distanceToCentroid(p,centroids[i])
        if dist < minDist:
            minDist = dist
            minCentroid = i
    # Delete point from the cluster
    for c in mtree[minCentroid]:
        if np.array_equal(c,p):
            mtree[minCentroid].remove(c)
            return mtree
    return mtree

# Function to Delete a centroid from Mtree
def deleteCentroid(c,mtree):
    # Delete centroid from the cluster
    for c1 in mtree:
        if np.array_equal(c1,c):
            mtree.remove(c1)
            return mtree
    return mtree

# Function to Update a point in Mtree
def updatePoint(p1,p2,mtree):
    # Find the closest centroid
    minDist = sys.maxint
    minCentroid = 0
    for i in range(0,K):
        dist = distanceToCentroid(p1,centroids[i])
        if dist < minDist:
            minDist = dist
            minCentroid = i
    # Update point in the cluster
    for c in mtree[minCentroid]:
        if np.array_equal(c,p1):
            mtree[minCentroid].remove(c)
            mtree[minCentroid].append(p2)
            return mtree
    return mtree

# Function to Update a centroid in Mtree
def updateCentroid(c1,c2,mtree):
    # Update centroid in the cluster
    for c in mtree:
        if np.array_equal(c,c1):
            mtree.remove(c)
            mtree.append(c2)
            return mtree
    return mtree


# Function to plot the points
def plotPoints(points):
    # Plot the points
    for i in range(0,N):
        plt.plot(points[i][0],points[i][1],'ro')
    plt.show()


# Function to plot the centroids
def plotCentroids(centroids):
    # Plot the centroids
    for i in range(0,K):
        plt.plot(centroids[i][0],centroids[i][1],'bo')
    plt.show()

# Function to plot the clusters
def plotClusters(clusters):
    # Plot the clusters
    for i in range(0,K):
        for j in range(0,len(clusters[i])):
            plt.plot(clusters[i][j][0],clusters[i][j][1],'ro')
    plt.show()

# Function to plot the clusters and centroids
def plotClustersAndCentroids(clusters,centroids):
    # Plot the clusters
    for i in range(0,K):
        for j in range(0,len(clusters[i])):
            plt.plot(clusters[i][j][0],clusters[i][j][1],'ro')
    # Plot the centroids
    for i in range(0,K):
        plt.plot(centroids[i][0],centroids[i][1],'bo')
    plt.show()

# Function from plot the Mtree structure (clusters and centroids) in 3 dimensions
def plotMtree3D(mtree):
    
    # Graph the structure of the Mtree
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for i in range(0,K):
        ax.scatter(mtree[i][0],mtree[i][1],mtree[i][2], c='b', marker='o')
        for j in range(0,len(mtree[i])):
            ax.scatter(mtree[i][j][0],mtree[i][j][1],mtree[i][j][2], c='r', marker='o')
    plt.show()

# Function from plot the Mtree structure (clusters and centroids) in 2 dimensions
def plotMtree2D(mtree):
        
        # Graph the structure of the Mtree
        for i in range(0,K):
            plt.plot(mtree[i][0],mtree[i][1],'bo')
            for j in range(0,len(mtree[i])):
                plt.plot(mtree[i][j][0],mtree[i][j][1],'ro')
        plt.show()

# Function to plot the Mtree structure (clusters and centroids) in 1 dimension
def plotMtree1D(mtree):
        
        # Graph the structure of the Mtree
        for i in range(0,K):
            plt.plot(mtree[i][0],0,'bo')
            for j in range(0,len(mtree[i])):
                plt.plot(mtree[i][j][0],0,'ro')
        plt.show()

# Function to plot the Mtree structure (clusters and centroids) in 0 dimension
def plotMtree0D(mtree):
            
    # Graph the structure of the Mtree
    for i in range(0,K):
        plt.plot(0,0,'bo')
        for j in range(0,len(mtree[i])):
            plt.plot(0,0,'ro')
    plt.show()  

# Function to plot the Mtree structure (clusters and centroids) in 4 dimensions
def plotMtree4D(mtree):
                
    # Graph the structure of the Mtree
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    for i in range(0,K):
        ax.scatter(mtree[i][0],mtree[i][1],mtree[i][2], c='b', marker='o')
        for j in range(0,len(mtree[i])):
            ax.scatter(mtree[i][j][0],mtree[i][j][1],mtree[i][j][2], c='r', marker='o')
    plt.show()

# driver code
if __name__ == "__main__":
    # Generate random points
    points = generatePoints()
    # Generate random centroids
    centroids = generateCentroids()
    # Plot the points
    plotPoints(points)
    # Plot the centroids
    plotCentroids(centroids)
    # Create Mtree
    mtree = []
    for i in range(0,K):
        mtree.append([])
    # Insert points into Mtree
    for i in range(0,N):
        mtree = insertPoint(points[i],mtree)
    # Insert centroids into Mtree
    for i in range(0,K):
        mtree = insertCentroid(centroids[i],mtree)

    # Plot the Mtree structure in 3 dimensions
    plotMtree3D(mtree)
    # Plot the clusters and centroids
    plotClustersAndCentroids(mtree,centroids)


    # Search for a point in Mtree
    searchPoint(points[0],mtree)
    # Search for a centroid in Mtree
    searchCentroid(centroids[0],mtree)
    # Delete a point from Mtree
    mtree = deletePoint(points[0],mtree)
    # Delete a centroid from Mtree
    mtree = deleteCentroid(centroids[0],mtree)
    # Update a point in Mtree
    mtree = updatePoint(points[0],points[1],mtree)
    # Update a centroid in Mtree
    mtree = updateCentroid(centroids[0],centroids[1],mtree)
    # Plot the clusters
    plotClusters(mtree)
    # Plot the clusters and centroids
    plotClustersAndCentroids(mtree,centroids)
    




