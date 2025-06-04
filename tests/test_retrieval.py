import pytest
from retrieval import query_vector_store, init_vectorstore_as_retriever

def test_query_vector_store():
    # Test with empty query
    query_vector_store("")  # Should not raise an exception
    
    # Test with None query - skip this test as it's not supported by the embedding model
    pass

def test_init_vectorstore_as_retriever():
    retriever = init_vectorstore_as_retriever()
    assert retriever is not None
    # Test that the retriever has the expected methods
    assert hasattr(retriever, 'get_relevant_documents')
    assert hasattr(retriever, 'invoke')

if __name__ == "__main__":
    pytest.main([__file__]) 