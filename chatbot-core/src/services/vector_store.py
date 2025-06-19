import os
from langchain.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter


def load_documents_to_vector_db(file_path: str = "mental_health_support_en_hi_half.txt") -> int:
    openai_api_key = os.getenv("OPENAI_API_KEY")
    chroma_path = os.getenv("CHROMA_DB_PATH", "db")

    loader = TextLoader(file_path, encoding="utf-8")
    documents = loader.load()

    splitter = CharacterTextSplitter(chunk_size=800, chunk_overlap=100)
    chunks = splitter.split_documents(documents)

    db = Chroma.from_documents(chunks, embedding=OpenAIEmbeddings(openai_api_key=openai_api_key), persist_directory=chroma_path)
    db.persist()
    return len(chunks)