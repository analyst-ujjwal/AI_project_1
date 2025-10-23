import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def get_chat_response(user_input: str) -> str:
    """
    Generates a conversational response using Groq + LLaMA 3.
    """
    groq_api_key = os.getenv("GROQ_API_KEY")
    if not groq_api_key:
        raise ValueError("GROQ_API_KEY not found. Please set it in your .env file.")

    # Initialize Groq LLM
    llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.1-8b-instant",
        temperature=0.7,
        max_tokens=512
    )

    # Define prompt template
    prompt = ChatPromptTemplate.from_template(
        "You are an AI assistant. Be clear, helpful, and conversational.\nUser: {user_input}\nAI:"
    )

    chain = prompt | llm
    response = chain.invoke({"user_input": user_input})
    return response.content
