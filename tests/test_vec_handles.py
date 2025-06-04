import pytest
from vec_handles import final_document

def test_final_document():
    # Test that final_document is either a list or None
    assert final_document is not None
    assert isinstance(final_document, list)
    
    # If there are documents, test their structure
    if final_document:
        for doc in final_document:
            assert hasattr(doc, 'page_content')
            assert hasattr(doc, 'metadata')

if __name__ == "__main__":
    pytest.main([__file__]) 