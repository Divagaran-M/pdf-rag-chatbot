def build_prompt(context, question, history):
    """
    Build a prompt using conversation history and retrieved context.
    """

    conversation = ""

    for message in history:
        role = message["role"].capitalize()
        conversation += f"{role}: {message['content']}\n"

    prompt = f"""
You are an intelligent AI assistant that answers questions about uploaded PDF documents.

Your Rules:
1. Read the conversation history to understand follow-up questions.
2. Use ONLY the provided document context to answer.
3. Never use outside knowledge.
4. If the answer is not present in the context, reply exactly:
"I couldn't find that information in the uploaded document."
5. Keep answers natural and conversational.
6. If the user asks follow-up questions like "he", "it", "they", use the conversation history to understand what they refer to.

================ Conversation History ================

{conversation}

======================================================

================ Document Context ====================

{context}

======================================================

Current Question:
{question}

Answer:
"""

    return prompt