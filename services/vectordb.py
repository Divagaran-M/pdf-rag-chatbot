from qdrant_client import QdrantClient
from qdrant_client.models import (
    Distance,
    VectorParams,
    PointStruct,
    Filter,
    FieldCondition,
    MatchValue,
    PayloadSchemaType,
)

from config import QDRANT_URL, QDRANT_API_KEY

client = QdrantClient(
    url=QDRANT_URL,
    api_key=QDRANT_API_KEY,
)

COLLECTION_NAME = "pdf-rag-chatbot"

# --------------------------------------------------
# Create Collection
# --------------------------------------------------

collections = client.get_collections().collections

if COLLECTION_NAME not in [c.name for c in collections]:

    client.create_collection(
        collection_name=COLLECTION_NAME,
        vectors_config=VectorParams(
            size=1024,
            distance=Distance.COSINE,
        ),
    )

try:
    client.create_payload_index(
        collection_name=COLLECTION_NAME,
        field_name="filename",
        field_schema=PayloadSchemaType.KEYWORD,
    )
except Exception:
    pass


# --------------------------------------------------
# Store Embeddings
# --------------------------------------------------

def store_embeddings(chunks, embeddings, filename):

    points = []

    for i, (chunk, embedding) in enumerate(zip(chunks, embeddings)):

        points.append(
            PointStruct(
                id=abs(hash(f"{filename}_{i}")),
                vector=list(embedding),
                payload={
                    "filename": filename,
                    "document": chunk,
                },
            )
        )

    client.upsert(
        collection_name=COLLECTION_NAME,
        points=points,
        wait=True,
    )

    return len(points)


# --------------------------------------------------
# Search
# --------------------------------------------------

def search_embeddings(query_embedding, filename, top_k=10):

    response = client.query_points(
        collection_name=COLLECTION_NAME,
        query=list(query_embedding),
        limit=top_k,
        query_filter=Filter(
            must=[
                FieldCondition(
                    key="filename",
                    match=MatchValue(value=filename),
                )
            ]
        ),
    )

    documents = [
        point.payload["document"]
        for point in response.points
    ]

    return {
        "documents": [documents]
    }