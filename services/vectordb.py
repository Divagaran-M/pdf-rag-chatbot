import chromadb

# Create a persistent database
client = chromadb.PersistentClient(path="db")

# Create or load a collection
collection = client.get_or_create_collection(
    name="documents"
)


def store_embeddings(chunks, embeddings, filename):

    """
    Store chunks and embeddings in ChromaDB.
    """

    ids = []

    metadatas = []

    for i in range(len(chunks)):
        ids.append(f"{filename}_{i}")

        metadatas.append({
            "filename": filename
        })

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings.tolist(),
        metadatas=metadatas
    )

    return len(chunks)

def search_embeddings(query_embedding, filename, top_k=10):
    """
    Search only inside the selected document.
    """

    results = collection.query(
        query_embeddings=[query_embedding.tolist()],
        n_results=top_k,
        where={
            "filename": filename
        }
    )

    return results