from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma


def create_vectorstore():

    # Load movie data
    loader = TextLoader("movies.txt", encoding="utf-8")
    documents = loader.load()

    # Check if file contains data
    if not documents:
        raise ValueError("movies.txt is empty or could not be loaded.")

    print(f"Number of documents: {len(documents)}")

    # Split movie data into chunks
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    splits = text_splitter.split_documents(documents)

    print(f"Number of splits: {len(splits)}")

    # Make sure chunks exist
    if not splits:
        raise ValueError(
            "No text chunks were created. Check your movies.txt file."
        )

    # Create embeddings
    print("Loading embedding model...")

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    print("Creating vector store...")

    # Create Chroma vector database
    vectorstore = Chroma.from_documents(
        documents=splits,
        embedding=embeddings
    )

    print("Vector store created successfully!")

    return vectorstore


def retrieve_answer(vectorstore, question):

    results = vectorstore.similarity_search(
        question,
        k=2
    )

    context = "\n\n".join(
        [result.page_content for result in results]
    )

    return context