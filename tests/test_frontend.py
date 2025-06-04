import pytest
import streamlit as st
from frontend import check

def test_session_state_initialization():
    # Test that session state is initialized correctly
    assert "messages" in st.session_state
    assert isinstance(st.session_state.messages, list)

def test_chat_input():
    # Test that chat input is properly handled
    test_input = "Hello, world!"
    response = check(test_input)
    assert response is not None
    assert isinstance(response, dict)
    assert 'answer' in response

if __name__ == "__main__":
    pytest.main([__file__]) 