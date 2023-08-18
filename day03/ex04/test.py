import numpy as np
from Kmeans import KmeansClustering



try:
    data = np.loadtxt("./solar_system_census.csv", delimiter=',', skiprows=1)
    kmeans = KmeansClustering(max_iter=100, ncentroid=4)
    kmeans.fit(data)
    predicted_clusters = kmeans.predict(data)

    print("Centroids:", kmeans.centroids)
    print("Number of individuals in Each Cluster:", np.bincount(predicted_clusters))
except Exception as e:
    print(f"An error occured: {e}")