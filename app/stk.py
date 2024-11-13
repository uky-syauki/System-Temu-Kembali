from sklearn.metrics.pairwise import cosine_similarity
import numpy as np


produk = ['Laptop', 'Smartphone', 'Tablet', 'Handphone']
daftar_produk = np.array([
    [0.8, 0.2, 0.1],
    [0.7, 0.1, 0.4],
    [0.6, 0.4, 0.3],
    [0.1, 0.8, 0.5]
])


def rekomendasi_produk(user_input, produk, daftar_produk):
    produk_input = daftar_produk[produk.index(user_input)]
    similarity_scores = cosine_similarity([produk_input], daftar_produk)
    rekomendasi_idx = np.argsort(similarity_scores[0])[-2:][::-1]
    return [produk[i] for i in rekomendasi_idx]


