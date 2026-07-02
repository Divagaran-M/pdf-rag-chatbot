from fastapi import APIRouter
from pydantic import BaseModel

from services.retriever import retrieve_context
from services.prompt_builder import build_prompt
from services.llm import generate_response

router = APIRouter()


class ChatRequest(BaseModel):
    question: str
    filename: str
    history: list = []


@router.post("/chat")
async def chat(request: ChatRequest):

    # Retrieve relevant context
    context = retrieve_context(
    question=request.question,
    filename=request.filename
)

    # Build prompt
    prompt = build_prompt(
        context=context,
        question=request.question,
        history=request.history
    )

    print("\n========== PROMPT ==========\n")
    print(prompt)
    print("\n============================\n")

    # Generate answer
    answer = generate_response(prompt)

    print("\n========== ANSWER ==========\n")
    print(answer)
    print("\n============================\n")

    return {
        "question": request.question,
        "answer": answer
    }