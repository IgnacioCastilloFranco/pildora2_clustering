from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import matplotlib.pyplot as plt

# 1. Create synthetic dataset
""" 500 sample points, arranged around 1 center so the clusters are not clearly 
outlined. The random_state=42 argument seeds the generator to keep the output 
deterministic across runs. The function returns a feature matrix X, containing 
the coordinates of every sampled point, and y_true, an array of integers that 
mark the ground-truth cluster assignment for evaluation or visualization. """
X, y_true = make_blobs(n_samples=500, centers=4, cluster_std=13.6, random_state=42)
print(y_true)

# 2. Train K-Means model
""" instantiates a KMeans clustering model with 4 centroid slots, a deterministic 
random seed of 42, and scikit-learn’s modern default for the repeated 
initialization strategy (n_init="auto"). The second line passes the feature
matrix X into fit_predict, which both trains the model and returns the cluster
labels assigned to each sample; the result is stored in y_kmeans for later 
evaluation or visualization.
 """
kmeans = KMeans(n_clusters=4, random_state=42, n_init="auto")
y_kmeans = kmeans.fit_predict(X)

# 3. Validation using silhouette score
score = silhouette_score(X, y_kmeans)
print(f"Silhouette Score: {score:.3f}")

# 4. Visualization
plt.scatter(X[:, 0], X[:, 1], c=y_kmeans, s=30, cmap='viridis')
centers = kmeans.cluster_centers_
plt.scatter(centers[:, 0], centers[:, 1], c='red', s=200, alpha=0.7, marker='X')
plt.title("K-Means Clustering")
plt.show()
