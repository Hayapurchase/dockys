# DOCyTalky

A powerful document-based chatbot that allows users to interact with their documents through natural language conversations.

## Features

- Multiple LLM model support (DeepSeek, Mistral, HuggingFace, OpenAI)
- Document-based question answering
- Interactive chat interface
- Model selection capability
- Vector-based document retrieval

## Installation

1. Clone the repository:
```bash
git clone [your-repository-url]
cd DOCyTalky
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file with your API Keys token:
```
GOOGLE_API_KEY = #
JINAAI_API_KEY = #
```

## Usage

1. Start the Streamlit app:
```bash
streamlit run frontend.py
```

2. Open your browser and navigate to `http://localhost:8501`

## Project Structure

- `my_first_app.py`: Streamlit frontend application
- `backend.py`: Core chatbot functionality and model management
- `requirements.txt`: Project dependencies
- `documents/`: Directory for your document files

## Security Note

This is a private repository. Please ensure:
- Never commit API keys or sensitive information
- Keep your `.env` file local and add it to `.gitignore`
- Regularly update dependencies for security patches

## License

Private - All rights reserved 
