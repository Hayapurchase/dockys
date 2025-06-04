
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.prompts import ChatPromptTemplate
from retrieval import init_vectorstore_as_retriever
import getpass
import os 
from dotenv import load_dotenv
load_dotenv()



if not os.environ.get("GOOGLE_API_KEY"):
  os.environ["GOOGLE_API_KEY"] = getpass.getpass("Enter API key for Google Gemini: ")

from langchain.chat_models import init_chat_model

llm = init_chat_model("gemini-2.0-flash", model_provider="google_genai")


question_system_template = (
        "Given a chat history and the latest user question "
        "which might reference context in the chat history, "
        "formulate a standalone question which can be understood "
        "without the chat history. Do NOT answer the question, "
        "just reformulate it if needed and otherwise return it as is."
    )
question_system_prompt = ChatPromptTemplate.from_messages(
    [
        ("system",question_system_template),
        ("placeholder","{chat_history}"),
        ("human","{input}"),
    ]
)


history_aware_retriever =create_history_aware_retriever(
    llm, init_vectorstore_as_retriever(),question_system_prompt
)

system_prompt = (
    "You are an assistant for question-answering tasks. "
    "Use the following pieces of retrieved context to answer "
    "the question. If you don't know the answer, say that you "
    "don't know. Use three sentences maximum and keep the "
    "answer concise."
    "\n\n"
    "{context}"
)

qa_prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("placeholder", "{chat_history}"),
        ("human", "{input}"),
    ]
)

qa_chain = create_stuff_documents_chain(llm, qa_prompt)

conversational_qa_chain = create_retrieval_chain(history_aware_retriever,qa_chain)

chat_history = []

def check(query):
   
    qa_chain = create_stuff_documents_chain(llm, qa_prompt)

    conversational_qa_chain = create_retrieval_chain(history_aware_retriever,qa_chain)

    response = conversational_qa_chain.invoke(
        {
            "input" : (query),
            "chat_history":chat_history,
        }
    )
    chat_history.append(("human", query))
    chat_history.append(("ai", response["answer"])) 
    return response

check("Telecommunication")