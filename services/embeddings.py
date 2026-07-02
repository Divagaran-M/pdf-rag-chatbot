from sentence_transformers import SentenceTransformer

# Load the embedding model only once
model = SentenceTransformer("all-MiniLM-L6-v2")


def generate_embeddings(chunks: list[str]):
    """
    Convert text chunks into embedding vectors.
    """

    embeddings = model.encode(chunks)

    return embeddings