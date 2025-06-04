import pytest
import os
from docloader import load_csv, split_documents

def test_load_csv():
    # Test with a non-existent file
    result = load_csv("non_existent.csv")
    assert result is None
    
    # Test with an empty file
    with open("test_empty.csv", "w") as f:
        f.write("")
    result = load_csv("test_empty.csv")
    assert result is None
    os.remove("test_empty.csv")

def test_split_documents():
    # Test with invalid chunk size
    result = split_documents("test.csv", chunk_size=0, chunk_overlap=0)
    assert result == []
    
    # Test with invalid chunk overlap
    result = split_documents("test.csv", chunk_size=100, chunk_overlap=-1)
    assert result == []

if __name__ == "__main__":
    pytest.main([__file__]) 