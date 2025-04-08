import numpy as np
import matplotlib.pyplot as plt
from sklearn.manifold import TSNE
from sentence_transformers import SentenceTransformer

# Sample text data
sentences = [
    "I love taking my dog for a walk.",
    "The weather is perfect for a stroll in the park.",
    "I enjoy reading books on a rainy day.",
    "My cat loves to sleep next to me.",
    "Walking my dog in the morning is my favorite routine.",
    "Books are a window to different worlds.",
    "It’s raining today, perfect for staying in and reading."
]

# Load a pre-trained SentenceTransformer model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Generate embeddings
embeddings = model.encode(sentences)

# Reduce dimensionality to 2D using t-SNE
tsne = TSNE(n_components=2, perplexity=3, random_state=42)
embeddings_2d = tsne.fit_transform(embeddings)

# Visualize the embeddings
plt.figure(figsize=(8, 6))
plt.scatter(embeddings_2d[:, 0], embeddings_2d[:, 1], c='blue')

# Annotate points with their sentences
for i, sentence in enumerate(sentences):
    plt.annotate(sentence[:15] + '...', (embeddings_2d[i, 0], embeddings_2d[i, 1]))

plt.title('2D Visualization of Text Embeddings')
plt.xlabel('Dimension 1')
plt.ylabel('Dimension 2')
plt.show()