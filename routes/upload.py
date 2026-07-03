from fastapi import APIRouter, UploadFile, File

from services.validator import validate_file
from services.saver import save_file
from services.extractor import extract_text
from services.chunker import chunk_text
from services.embeddings import generate_document_embeddings
from services.vectordb import store_embeddings
router = APIRouter()


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):

    # Validate
    await validate_file(file)

    # Save
    saved_path = await save_file(file)

    # Extract
    text = extract_text(saved_path)

    # Chunk
    chunks = chunk_text(text)

    # Generate Embeddings
    embeddings = generate_document_embeddings(chunks)

    # Store in ChromaDB
    total_stored = store_embeddings(
        chunks=chunks,
        embeddings=embeddings,
        filename=file.filename
    )

    return {
    "success": True,
    "message": "Document indexed successfully.",
    "filename": file.filename,
    "chunks_stored": total_stored
}

    
