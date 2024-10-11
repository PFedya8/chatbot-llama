""" make and return the llm instace """

from langchain_community.chat_models.ollama import ChatOllama


def get_llm():
    """returns llama3 model instance"""
    return ChatOllama(model="llama3.1", temperature=0)
