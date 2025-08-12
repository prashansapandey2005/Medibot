import streamlit as st

def medibot():
    st.title("About MediBot AI")

    st.write(
        "MediBot AI is a Retrieval-Augmented Generation (RAG) based project implemented using Ollama. "
        "It's designed to be your personal AI medical assistant, providing information and answering "
        "your health-related questions based on a pre-trained knowledge base. "
    )
    
    st.markdown("<h2 style='text-align: left;'>Key Features</h2>", unsafe_allow_html=True)

    st.markdown("**Personal AI**")
    st.write(
        "Think of MediBot AI as your personal medical assistant. It's like having a knowledgeable companion "
        "who can provide guidance and suggestions on health topics. While it cannot replace a doctor, "
        "it can be a valuable resource for understanding medical information."
    )

    st.markdown("**No to Internet**")
    st.write(
        "One of the unique features of MediBot AI is that it doesn't require an internet connection to run. "
        "This means you can access medical information even when you're offline, such as while traveling or "
        "in areas with limited connectivity. No need to rely on servers or internet access!"
    )

    st.markdown("**Multiple Use Cases**")
    st.write(
        "The underlying Ollama technology used in MediBot AI allows you to create various personal chatbots "
        "tailored to your needs. Imagine having a study AI to help with your coursework, a cooking AI "
        "to assist in the kitchen, or any other personalized AI assistant you can think of!"
    )

    st.markdown("<h2 style='text-align: left;'>Technologies Used</h2>", unsafe_allow_html=True)

    st.markdown("**RAG**")
    st.write(
        "Retrieval-Augmented Generation (RAG) is a technique that combines information retrieval with "
        "text generation. MediBot AI uses RAG to access and process information from a pre-trained "
        "knowledge base to answer your questions accurately."
    )

    st.markdown("**Ollama**")
    st.write(
        "Ollama is a powerful tool developed by Meta that allows you to run large language models locally "
        "on your device. This ensures privacy and accessibility without relying on cloud services. "
        "The model used in MediBot AI is llama3.2."
    )

    st.markdown("**Other Technologies**")
    st.write(
        "MediBot AI also utilizes Streamlit for the user interface and Langchain for orchestrating "
        "the interactions between the language model and the knowledge base."
    )
