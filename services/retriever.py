from services.embeddings import generate_query_embedding
from services.vectordb import search_embeddings


def retrieve_context(question, filename):
    """
    Retrieve the most relevant context from the selected document.
    """

    # Generate embedding for the question
    query_embedding = generate_query_embedding(question)
    # Search only inside the selected document
    results = search_embeddings(
        query_embedding=query_embedding,
        filename=filename
    )

    # Extract retrieved chunks
    chunks = results["documents"][0]

    print(f"\nRetrieved {len(chunks)} chunks from {filename}\n")

    for i, chunk in enumerate(chunks, start=1):
        print(f"\n----- Chunk {i} -----")
        print(chunk)

    # Merge chunks
    context = "\n\n".join(chunks)

    return context