import numpy as np
import pandas as pd
import matplotlib.pyplot as plt # to plot the visuals
from sklearn.manifold import TSNE # its needed for basicall y squishing 384 dims to 2 in the vectors


embeddings = np.load("embeddings.npy")

#reducer, squishing to 2 dims
tsne = TSNE(n_components=2)

# squished to 2d
reduced = tsne.fit_transform(embeddings)# now each row is x and y coordinate

#loading the data to label the the dots in the space
df = pd.read_csv("file.csv")
categories = df["category"].to_list()

# print(categories[0])
# print(df["text"][:10])
# print(len(df))
# print(reduced[0])

unique_categories = set(categories)

for cat in unique_categories:
    for i in range(len(df)):
        x_points = []
        y_points = []
        if df["category"][i] == cat:
            x_points.append(reduced[i][0])
            y_points.append(reduced[i][1])

    plt.scatter(x_points, y_points, label=cat)

