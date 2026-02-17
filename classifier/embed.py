"""
we load the csv file
load the sentence model
turn each text row into a vector using embedding
and then we save the embeddings
"""
#imports
from sentence_transformers import SentenceTransformer
import pandas as pd
import numpy as np


#loading the model for the embedding
model = SentenceTransformer("all-MiniLM-L6-v2")

df = pd.read_csv("file.csv")

texts = df["text"].to_list()
embeddings = model.encode(texts)

# print(embeddings.shape)

np.save("embeddings.npy", embeddings)