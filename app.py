import streamlit as st
import time
from src.helper import get_pdf_text,get_text_chunks,get_vector_store,get_conversational_chain

def user_input(user_query):
    response = st.session_state.conversational_chain({"question": user_query})
    st.session_state.chatHistory = response['chat_history']
    for i , message in enumerate(st.session_state.chatHistory):
        if i % 2 == 0:
            st.write(f"**User:** {message.content}")
        else:
            st.write(f"**Reply:** {message.content}")



def main():
    st.set_page_config("Information Retrieval System")
    st.header("Information Retrieval System 💁‍♀️")
    user_query = st.text_input("Ask a question from the PDF files")
    if 'conversational_chain' in st.session_state:
        st.session_state.conversational_chain = None
    if "chatHistory" not in st.session_state:
        st.session_state.chatHistory = None
    if user_query:
        user_input(user_query)

    with st.sidebar:
        st.title("Menu")
        pdf_docs = st.file_uploader("Upload your PDF files and Click on the submit button", accept_multiple_files=True)
        if st.button("Submit & Process"):
            with st.spinner("Processing..."):
                time.sleep(2)
                pdf_text = get_pdf_text(pdf_docs)
                text_chunks = get_text_chunks(pdf_text)
                vector_store = get_vector_store(text_chunks)
                st.session_state.conversational_chain = get_conversational_chain(vector_store)
                st.success("Files processed successfully!")
            

if __name__ == "__main__":
    main()