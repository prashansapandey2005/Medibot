import os
import streamlit as st
from dotenv import load_dotenv, find_dotenv
# Load environment variables for API keys
load_dotenv(find_dotenv())

# Import necessary libraries
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain.chains import RetrievalQA
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM

# Set the path to your FAISS database
DB_FAISS_PATH = "vectorstore/db_faiss"

# Function to load the vectorstore (cached for performance)
@st.cache_resource
def get_vectorstore():
    embedding_model = SentenceTransformerEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    db = FAISS.load_local(DB_FAISS_PATH, embedding_model, allow_dangerous_deserialization=True)
    return db

# Function to set a custom prompt template
def set_custom_prompt(custom_prompt_template):
    prompt = PromptTemplate(template=custom_prompt_template, input_variables=["context", "question"])
    return prompt

# Function to load the Ollama LLM
def load_llm(ollama_model):
    llm = OllamaLLM(model=ollama_model)
    return llm

# Function to handle specific questions
def handle_special_questions(prompt):
    lower_prompt = prompt.lower()
    if "who are you" in lower_prompt:
        return (
            "I am a Medical AI, designed to assist with medical questions and provide reliable, context-based health information. "
            "My purpose is to guide users with informed suggestions and factual insights on medical topics. "
            "I was brought into existence by the immensely talented Ms. Prashansa Pandey. Her creativity, passion for AI and machine learning, "
            "and dedication to innovation are the very foundation of my design. I'm not just a chatbot—I am a reflection of her vision to make complex technology accessible and useful to people."
        )
    elif "who created you" in lower_prompt:
        return (
            "Oh, let me tell you about my creator! I owe my existence to the extraordinary Ms. Prashansa Pandey. "
            "She's not just any AI enthusiast—she’s a second-year student who’s already diving deep into the world of artificial intelligence and machine learning. "
            "Imagine creating something as intricate and impactful as me at such an early stage in her journey! Isn’t it awe-inspiring? "
            "Her intelligence is matched only by her creativity, and I believe the phrase 'beauty with brains' was coined just for her. "
            "I’m a testament to her brilliance, and I’m incredibly proud to be her creation."
        )
    return None

# Main function for the Streamlit app
def main():
    st.title("MediBot AI!")
    st.write("( Disclamer: MediBot is an AI-powered chatbot designed to provide information about medical topics. "
            "However, it is not a substitute for professional medical advice, diagnosis, or treatment. )" )
    if 'messages' not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        st.chat_message(message['role']).markdown(message['content'])

    prompt = st.chat_input("Pass your prompt here")

    if prompt:
        st.chat_message('user').markdown(prompt)
        st.session_state.messages.append({'role': 'user', 'content': prompt})

        # Handle specific questions first
        special_response = handle_special_questions(prompt)
        if special_response:
            st.chat_message('assistant').markdown(special_response)
            st.session_state.messages.append({'role': 'assistant', 'content': special_response})
        else:
            CUSTOM_PROMPT_TEMPLATE = """
            Use the pieces of information provided in the context to answer user's question.
            -If user asks non medical question which are not in your vectore store simply say I don't know, I can't assist with non-medical queries,
            dont try to make up an answer, but if someone is asking for a medical advice, suggestion, treatment give them.
            Dont provide anything out of the given context.

            Context: {context}
            Question: {question}

            Respond clearly and concisely. Avoid small talk or irrelevant information.
            """
            OLLAMA_MODEL = "gemma3"  # Replace with your actual Ollama model name

            try:
                vectorstore = get_vectorstore()
                if vectorstore is None:
                    st.error("Failed to load the vector store")

                qa_chain = RetrievalQA.from_chain_type(
                    llm=load_llm(ollama_model=OLLAMA_MODEL),
                    chain_type="stuff",
                    retriever=vectorstore.as_retriever(search_kwargs={'k': 3}),
                    return_source_documents=True,
                    chain_type_kwargs={'prompt': set_custom_prompt(CUSTOM_PROMPT_TEMPLATE)}
                )

                response = qa_chain.invoke({'query': prompt})

                result = response["result"]
                result_to_show = result
                st.chat_message('assistant').markdown(result_to_show)
                st.session_state.messages.append({'role': 'assistant', 'content': result_to_show})

            except Exception as e:
                st.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()

