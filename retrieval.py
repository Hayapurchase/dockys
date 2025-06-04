from langchain_chroma import Chroma
import logging
import os
from dotenv import load_dotenv
load_dotenv()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from langchain.embeddings import JinaEmbeddings   
persist_directory = "./jinadb"
embeddings = JinaEmbeddings(
    model_name="jina-embeddings-v2-small-en",
    jina_api_key=os.environ.get("JINAAI_API_KEY")
)

# Initialize vector store with persistence
try:
    logger.info(f"Initializing vector store from {persist_directory}")
    vector_store = Chroma(
        persist_directory=persist_directory,
        embedding_function=embeddings
    )
    
    # Check if vector store has any documents
    collection = vector_store._collection
    count = collection.count()
    logger.info(f"Vector store contains {count} documents")
    
    if count == 0:
        logger.warning("Vector store is empty")
except Exception as e:
    print(f"Error initializing vector store: {e}")
    vector_store = None

def query_vector_store(query):
    if not vector_store:
        print("Vector store not initialized")
        return []
    
    try:
        logger.info(f"Querying vector store with: {query}")
        results = vector_store.similarity_search(query, k=5)
        logger.info(f"Found {len(results)} results")
        
        for result in results:
            logger.info(f"----------RESULT----------------{result}")
        
        return results
    except Exception as e:
        print(f"Error querying vector store: {e}")
        return []

def init_vectorstore_as_retriever():
    if not vector_store:
        print("Vector store not initialized")
        return None
    
    try:
        retriever = vector_store.as_retriever()
        logger.info("Successfully created retriever")
        return retriever
    except Exception as e:
        print(f"Error creating retriever: {e}")
        return None

print(init_vectorstore_as_retriever())
