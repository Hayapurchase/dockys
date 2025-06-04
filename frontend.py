import streamlit as st
from ragchain import check 

# Set the title of the app
st.set_page_config(
    page_title="DOCyTalky",
    page_icon="💬",
    layout="centered"
)


# Custom CSS to style the navbar and title
st.markdown("""
    <style>
        .navbar {
            background-color: #333;
            overflow: hidden;
            display: flex;
            justify-content: center;
            padding: 10px;
            width:100%;
        }
        .title {
            text-align: center;
            font-size: 32px;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)


# Set the title of the app with centered alignment
st.markdown('<div class="title">DockyTalky</div>', unsafe_allow_html=True)


# Initialize the session state to hold messages if not already initialized
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat input field outside the expander
user_input = st.chat_input("Enter message")

# Display initial AI message
if len(st.session_state.messages) == 0:
    with st.chat_message("ai"):
        st.write("Hello Human")

# Display previous chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Process user input and display it
if user_input:
    # Add the user's message to the session state
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Display the user's message
    with st.chat_message("user"):
        st.write(user_input)
    
    # Simulate AI response (replace with actual backend logic)
    with st.chat_message("ai"):
        with st.spinner("Thinking..."):
            # Replace this with actual backend for AI response
            answer = check(user_input)  
            st.write(answer)
    
    # Add AI response to the session state
    st.session_state.messages.append({"role": "ai", "content": answer['answer']})
