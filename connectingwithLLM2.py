import os
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_core.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS
from langchain_ollama import OllamaLLM

# Step 1: Setup LLM (Ollama)
OLLAMA_MODEL = "gemma3"  # Replace with your Ollama model

def load_llm(ollama_model):
    llm = OllamaLLM(model=ollama_model)
    return llm

# Step 2: Connect LLM with FAISS and Create chain

CUSTOM_PROMPT_TEMPLATE = """
You're a medical AI, you will answer in a very straight tone only give suggestions, don't provide any medications.
Use the pieces of information provided in the context to answer user's question.
If you dont know the answer, just say that you dont know, dont try to make up an answer. 
Dont provide anything out of the given context

Context: {context}
Question: {question}

Start the answer with directly. No small talks.
"""

def set_custom_prompt(custom_prompt_template):
    prompt = PromptTemplate(template=custom_prompt_template, input_variables=["context", "question"])
    return prompt

# Load Database
DB_FAISS_PATH = "vectorstore/db_faiss"
embedding_model = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
db = FAISS.load_local(DB_FAISS_PATH, embedding_model, allow_dangerous_deserialization=True)

# Create QA chain
qa_chain = RetrievalQA.from_chain_type(
    llm=load_llm(OLLAMA_MODEL),
    chain_type="stuff",
    retriever=db.as_retriever(search_kwargs={'k': 3}),
    return_source_documents=True,
    chain_type_kwargs={'prompt': set_custom_prompt(CUSTOM_PROMPT_TEMPLATE)}
)

# Now invoke with a single query
user_query = input("Write Query Here: ")
response = qa_chain.invoke({'query': user_query})
print("RESULT: ", response["result"])
print("SOURCE DOCUMENTS: ", response["source_documents"])