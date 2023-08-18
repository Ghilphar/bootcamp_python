import numpy as np
import argparse
import matplotlib.pyplot as plt

class KmeansClustering:
    def __init__(self, max_iter=20, ncentroid=5):
        self.ncentroid = ncentroid
        self.max_iter = max_iter
        self.centroids = []

    def fit(self, X):
        # Initialize centroids randomly from data points
        indices = np.random.choice(X.shape[0], self.ncentroid, replace=False)
        self.centroids = X[indices]

        for _ in range(self.max_iter):
            # Assignement step
            # Calculate the distance between each data point and the centroids
            distances = np.abs(X[:, np.newaxis] - self.centroids).sum(axis=2)
            cluster_indices = np.argmin(distances, axis=1)

            # Update step
            # Compute new centroids as the mean  of the data points in each cluster
            new_centroids = np.array([X[cluster_indices == i].mean(axis=0) for i in range(self.ncentroid)])

            # Check for convergence
            if np.all(self.centroids == new_centroids):
                break

            self.centroids = new_centroids

    def predict(self, X):
        """
        Predict from which cluster each datapoint belongs to.
        Args:
        -----
        X: has to be an nunmpy.ndarray, a matrix of dimension m * n.
        Return:
        -----
        The prediction as a numpy.ndarray, a vector of dimension m * 1.
        """
        distances = np.abs(X[:, np.newaxis] - self.centroids).sum(axis=2)
        return np.argmin(distances, axis=1)

def plot_clusters(data, predicted_clusters, centroids):
    fig, ax = plt.subplots(1, 3, figsize=(15, 5))

    # Plotting for Height vs Weight
    ax[0].scatter(data[:, 0], data[:, 1], c=predicted_clusters, s=50, cmap='viridis')
    ax[0].scatter(centroids[:, 0], centroids[:, 1], c='red', s=100, alpha=0.75)
    ax[0].set_xlabel('Height')
    ax[0].set_ylabel('Weight')
    ax[0].set_title('Height vs Weight')

    # Plotting Height vs Bone Density
    ax[1].scatter(data[:, 0], data[:, 2], c=predicted_clusters, s=50, cmap='viridis')
    ax[1].scatter(centroids[:, 0], centroids[:, 2], c='red', s=100, alpha=0.75)
    ax[1].set_xlabel("Height")
    ax[1].set_ylabel("Weight")
    ax[1].set_title("Height vs Bone Density")

    # Plotting Weight vs Bone Density
    ax[2].scatter(data[:, 1], data[:, 2], c=predicted_clusters, s=50, cmap='viridis')
    ax[2].scatter(centroids[:, 1], centroids[:, 2], c="red", s=100, alpha=0.75)
    ax[2].set_xlabel("Weight")
    ax[2].set_ylabel("Bone Density")
    ax[2].set_title("Weight vs Bone Density")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="K-means clustering for solar system census data.")
    parser.add_argument("filepath", type=str, help="Path to the dataset file")
    parser.add_argument("ncentroid", type=int, help="Number of centroids for clustering.")
    parser.add_argument("max_iter", type=int, help="Maximum number of iterations for K-means algorithm.")
    args = parser.parse_args()

    # Reading the dataset
    data = np.loadtxt(args.filepath, delimiter=',', skiprows=1)

    # K-means clustering
    kmeans = KmeansClustering(max_iter=args.max_iter, ncentroid=args.ncentroid)
    kmeans.fit(data)
    predicted_clusters = kmeans.predict(data)

    # Displaying results
    print("Centroids:\n", kmeans.centroids)
    print("Number of individuals in Each Cluster:", np.bincount(predicted_clusters))

    # Plotting clusters
    plot_clusters(data, predicted_clusters, kmeans.centroids)