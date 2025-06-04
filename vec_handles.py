import logging
import numpy as np
from docloader import final_document
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
import os
from dotenv import load_dotenv
load_dotenv()


if final_document:
    logging.info("Final document loaded")
    
    from langchain_community.embeddings import JinaEmbeddings
    embeddings = JinaEmbeddings(
        model_name="jina-embeddings-v2-small-en",
        jina_api_key=os.environ.get("JINAAI_API_KEY")
    )

    # Process documents in batches of 1000
    batch_size = 1000
    for i in range(0, len(final_document), batch_size):
        batch = final_document[i:i + batch_size]
        if i == 0:
            # Create the vector store with the first batch
            vector_store = Chroma.from_documents(
                batch,
                embeddings,
                persist_directory="./jinadb",
            )
        else:
            # Add subsequent batches
            vector_store.add_documents(documents=batch)
        print(f"Processed batch {i//batch_size + 1} of {(len(final_document) + batch_size - 1)//batch_size}")

    print("DONE")
    
else:
    print("Final document not loaded")

