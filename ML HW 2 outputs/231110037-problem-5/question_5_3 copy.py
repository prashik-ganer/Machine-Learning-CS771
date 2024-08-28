import pickle
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE

import numpy as np
import matplotlib.pyplot as plt

# Specify the path to your pickle file
pickle_file_path = 'mnist_small.pkl'

# Open the pickle file for reading (rb stands for read binary)
with open(pickle_file_path, 'rb') as file:
    # Load the data from the pickle file
    loaded_data = pickle.load(file)

# Now, 'loaded_data' contains the data from the pickle file
# print(loaded_data)


component_x = loaded_data['X']
component_y = loaded_data['Y']

print(component_x)
print(component_y)


# # Apply PCA
pca = PCA(n_components=2)
pca_result = pca.fit_transform(component_x)

# Plot the original data
# plt.scatter(component_x[:, 0], component_x[:, 1], label='Original Data')

# Plot the PCA-transformed data
plt.scatter(pca_result[:, 0], pca_result[:, 1], c=component_y)



# For tSNE
tsne = TSNE(n_components=2)
tsne_result = tsne.fit_transform(component_x)
# Plot the PCA-transformed data
plt.scatter(tsne_result[:, 0], tsne_result[:, 1], c=component_y)


# Customize the plot
plt.title('PCA Visualization')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.legend()

# Show the plot
plt.show()