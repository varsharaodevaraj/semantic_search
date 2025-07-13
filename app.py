import streamlit as st
from utils import load_pdf, split_documents, embeddingModel, vector_store, semantic_search

st.title("PDF Semantic Search")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file is not None:
    # Save uploaded file temporarily
    with open("temp.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    with st.spinner("Loading and splitting document..."):
        documents = load_pdf("temp.pdf")
        split_docs = split_documents(documents)

    embeddings = embeddingModel()
    vectorstore = vector_store(split_docs, embeddings)

    st.write(f"Document loaded and split into {len(split_docs)} chunks.")

    query = st.text_input("Ask any question related to the document:")

    if query:
        with st.spinner("Searching for answers..."):
            results = semantic_search(vectorstore, query, k=5, score_threshold=0.7)

        if not results:
            st.warning("No relevant results found for your query.")
        else:
            st.write("### 🔎 Top Results")
            for i, doc in enumerate(results):
                st.markdown(f"**Result {i+1}:**")
                st.write(doc.page_content)
                st.markdown("---")
