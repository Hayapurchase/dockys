import pytest
from ragchain import check

def test_check():
    # Test with empty query
    with pytest.raises(Exception):
        check("")
    
    # Test with None query
    with pytest.raises(Exception):
        check(None)
    
    # Test with a valid query
    response = check("What is the meaning of life?")
    assert response is not None
    assert isinstance(response, dict)
    assert 'answer' in response

if __name__ == "__main__":
    pytest.main([__file__]) 