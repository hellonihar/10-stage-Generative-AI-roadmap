import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import load_iris

def clustering_demo():
    # Load the Iris dataset (we'll ignore the labels for unsupervised learning)
    iris = load_iris()
    X = iris.data  # Features only

    # Initialize the KMeans model
    # We'll try to find 3 clusters since we know there are 3 species, 
    # but in a real unsupervised scenario, we wouldn't know this!
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)

    # Fit the model (finding clusters)
    kmeans.fit(X)

    # Get cluster assignments
    labels = kmeans.labels_
    centroids = kmeans.cluster_centers_

    # Plotting the clusters (using the first two features: Sepal Length and Sepal Width)
    plt.figure(figsize=(10, 6))
    
    # Scatter plot of the data points, colored by cluster
    plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', s=50, alpha=0.7, label='Data Points')
    
    # Plot the centroids
    plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=200, marker='X', label='Centroids')
    
    plt.xlabel('Sepal Length (cm)')
    plt.ylabel('Sepal Width (cm)')
    plt.title('K-Means Clustering on Iris Dataset (Unsupervised)')
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()

    print("K-Means Clustering complete.")
    print("Cluster centroids (first two features):\n", centroids[:, :2])

if __name__ == "__main__":
    clustering_demo()
