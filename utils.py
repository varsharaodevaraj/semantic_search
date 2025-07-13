from langchain.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.embeddings import SentenceTransformerEmbeddings
from langchain.vectorstores import FAISS


def load_pdf(file_path):
    loader = PyPDFLoader(file_path)
    document = loader.load()
    return document


def split_documents(document,chunk_size=500,chunk_overlap=50):
    splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size,chunk_overlap=chunk_overlap)
    split_documents = splitter.split_documents(document)
    return split_documents


def embeddingModel():
    embeddings = SentenceTransformerEmbeddings(model_name='all-MiniLM-L6-v2')
    return embeddings


def vector_store(documents,embeddings):
    vectorestore = FAISS.from_documents(documents,embeddings)
    return vectorestore


# def semantic_search(vectorstore,query,tok_k=3):
#     results = vectorstore.similarity_search(query,k=tok_k)
#     return results

def semantic_search(vectorstore, query, k=3, score_threshold=0.7):
    docs_scores = vectorstore.similarity_search_with_score(query, k=k)

    # Filtering out results below the similarity threshold
    # filtered_results = [
    #     doc for doc, score in docs_scores if score < score_threshold
    # ]
    filtered_results = []

    for doc, score in docs_scores:
        if score < score_threshold:
            filtered_results.append(doc)


    return filtered_results