import logging
from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_csv(file_path:str):

    loader = CSVLoader(file_path)

    try:
        documents =loader.load()
        logging.info("File successfully loaded")
        return documents
    except Exception as e:
        logging.error(f"Error loading CSV file: {e}")
    

def split_documents(file_path, chunk_size:int, chunk_overlap:int):

    documents = load_csv(file_path)

    if documents:
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )

        split_docs=text_splitter.split_documents(documents)
        print(f"Successfully split {len(documents)} documents into {len(split_docs)} chunks.")
        return split_docs
    else:
        logging.info("Documents not found")
        return []

final_document = split_documents("Documents/final_combined.csv", 1000, 200)