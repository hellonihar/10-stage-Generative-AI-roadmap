import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

def pca_demo():
    # Load the Iris dataset
    iris = load_iris()
    X = iris.data
    y = iris.target
    target_names = iris.target_names

    # Initialize PCA to reduce data from 4 dimensions to 2
    pca = PCA(n_components=2)
    
    # Fit and transform the data
    X_r = pca.fit_transform(X)

    # Percentage of variance explained for each components
    print(f"Explained variance ratio (first two components): {pca.explained_variance_ratio_}")

    # Plotting the PCA-transformed data
    plt.figure(figsize=(10, 6))
    colors = ['navy', 'turquoise', 'darkorange']
    lw = 2

    for color, i, target_name in zip(colors, [0, 1, 2], target_names):
        plt.scatter(X_r[y == i, 0], X_r[y == i, 1], color=color, alpha=.8, lw=lw,
                    label=target_name)
    
    plt.legend(loc='best', shadow=False, scatterpoints=1)
    plt.title('PCA of IRIS dataset (Dimensionality Reduction)')
    plt.xlabel('Principal Component 1')
    plt.ylabel('Principal Component 2')
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.show()

if __name__ == "__main__":
    pca_demo()
