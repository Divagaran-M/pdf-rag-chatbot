import os
from dotenv import load_dotenv

load_dotenv()

# -------------------------
# Groq API Key
# -------------------------



load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

UPLOAD_FOLDER = "data/uploads"

ALLOWED_EXTENSIONS = {
    "pdf",
    "docx",
    "txt",
    "csv"
}

MAX_FILE_SIZE = 20 * 1024 * 1024