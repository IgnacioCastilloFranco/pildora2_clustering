# K-Means Clustering Demo

This repository contains a concise example of applying the K-Means clustering algorithm to a synthetic dataset generated with scikit-learn. The script illustrates the end-to-end workflow of creating data, fitting a clustering model, evaluating its quality with the silhouette score, and visualizing the assigned clusters.

## Project Structure

| File | Description |
| --- | --- |
| `k_means.py` | Generates blob-based sample data, fits a 4-cluster K-Means model, prints evaluation metrics, and plots the resulting clusters. |
| `requirements.txt` | Locked Python dependencies required to reproduce the demo environment. |
| `presentation.pdf` | Slide deck (Spanish) introducing clustering fundamentals and the K-Means algorithm. |

## Prerequisites

- Python 3.10 or newer (tested with the Python 3.13 series).
- A virtual environment tool such as `venv` (recommended).

## Getting Started

1. **Clone or download** this project into a local folder.
2. **Create a virtual environment** (optional but recommended) from that folder:

   ```powershell
   python -m venv .venv
   ```

3. **Activate the environment** (PowerShell on Windows):

   ```powershell
   .\.venv\Scripts\activate
   ```

   To deactivate later, run `deactivate`.

4. **Install the dependencies** listed in `requirements.txt`:

   ```powershell
   pip install -r requirements.txt
   ```

## Running the Demo

Execute the script to generate the dataset, train the clustering model, and view the visualization:

```powershell
python k_means.py
```

The script outputs:

- The ground-truth labels produced by `make_blobs`.
- The silhouette score summarizing cluster cohesion vs. separation.
- A matplotlib scatter plot showing points colored by their assigned cluster along with red `X` markers for the learned centroids.

## Customization Ideas

- Adjust the parameters of `make_blobs` (for example, `centers`, `cluster_std`, `n_samples`) to explore different cluster separations.
- Change `n_clusters` in the `KMeans` constructor to investigate under- or over-clustering scenarios.
- Replace the silhouette score with additional metrics such as the Calinski-Harabasz or Davies-Bouldin indices.

## Troubleshooting

- **Missing dependencies**: Ensure the virtual environment is active before installing packages or running the script. Re-run `pip install -r requirements.txt` if you encounter `ModuleNotFoundError` exceptions.
- **Plot window does not appear**: Some environments require an interactive backend. Running the script from a local terminal (rather than certain remote shells) typically resolves this.

## License

This project is distributed under the [MIT License](./LICENSE). You are free to use, modify, and distribute the code under the terms described in the license text.
