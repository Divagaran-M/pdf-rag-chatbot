import streamlit as st

from ui.api import upload_pdf,ask_question
# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="PDF RAG Chatbot",
    page_icon="📄",
    layout="wide"
)

# --------------------------------------------------
# Session State
# --------------------------------------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "document_uploaded" not in st.session_state:
    st.session_state.document_uploaded = False

if "document_name" not in st.session_state:
    st.session_state.document_name = None

if "chunks" not in st.session_state:
    st.session_state.chunks = 0    

# --------------------------------------------------
# Sidebar
# --------------------------------------------------

with st.sidebar:

    st.title("📄 PDF RAG")

    st.markdown("---")

    st.subheader("Upload Document")

    uploaded_file = st.file_uploader(
        "Choose a PDF",
        type=["pdf"]
    )
    if uploaded_file is not None:

     if st.button("📤 Upload Document", use_container_width=True):

        with st.spinner("Indexing document..."):

            response = upload_pdf(uploaded_file)

            if response.status_code == 200:

             data = response.json()

             st.session_state.document_uploaded = True
             st.session_state.document_name = data["filename"]
             st.session_state.chunks = data["chunks_stored"]

             st.rerun()

            else:

              st.error("Upload failed")

    st.markdown("---")

    st.subheader("Status")

    if st.session_state.document_uploaded:

     st.success("🟢 Ready")

     st.write(f"📄 **{st.session_state.document_name}**")

     st.write(f"🧩 Chunks: {st.session_state.chunks}")

    else:

     st.warning("No document uploaded")

# --------------------------------------------------
# Main Chat Area
# --------------------------------------------------

st.title("💬 Chat")

st.caption("Chat with your uploaded document.")

# Display chat history
for message in st.session_state.messages:

    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
prompt = st.chat_input(
    "Ask anything about your document...",
    disabled=not st.session_state.document_uploaded
)
if prompt:

    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    try:

        response = ask_question(
    question=prompt,
    filename=st.session_state.document_name,
    history=st.session_state.messages[-6:]
)

        if response.status_code == 200:

            data = response.json()
            answer = data["answer"]

        else:

            answer = response.text

    except Exception as e:

        answer = str(e)

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": answer
        }
    )

    st.rerun()