from sentence_transformers import SentenceTransformer
import numpy as np
import pandas as pd

class PromptClassifier:

    def __init__(self):
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

        embeddings = np.load("embeddings.npy")
        df = pd.read_csv("file.csv")
        #computing the centroids(average) for each category
        self.centroids = {}
        unique_cats = set(df["category"])

        for cat in unique_cats:
            cat_vectors = []
            for i in range(len(df)):
                if cat == df['category'][i]:
                    cat_vectors.append(embeddings[i])

            self.centroids[cat] = np.mean(cat_vectors, axis= 0)



    def classify(self, prompt):
        embedding = self.model.encode(prompt)

        scores ={}

        for cat, centroid in self.centroids.items():
            #cosine simlilarity computation
            scores[cat] = np.dot(embedding, centroid)/ (np.linalg.norm(embedding)*np.linalg.norm(centroid))

        #softmaxx
        values = np.array(list(scores.values()))
        exp_values = np.exp(values - np.max(values))
        probabilities = exp_values/ exp_values.sum()


        #map it back to the categs
        result = {}
        for i, cat in enumerate(scores.keys()):
            result[cat]= probabilities[i]
        
        best =max(result, key=result.get)
        return best, result



    
classifier = PromptClassifier()

tests = [
    "solve x + 5 = 10",
    "write a python loop",
    "translate this to spanish",
    "summarize this article for me",
    "what are the legal requirements for an LLC",
]

for test in tests:
    best, probs = classifier.classify(test)
    print(f"\nPrompt: {test}")
    print(f"Category: {best}")
    for cat, prob in sorted(probs.items(), key=lambda x: x[1], reverse=True):
        print(f"  {cat}: {prob:.2%}")
