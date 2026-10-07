import streamlit as st

from rag import create_vectorstore, retrieve_answer
from ollama_client import ask_ollama


st.set_page_config(
    page_title="Movie Knowledge Assistant",
    page_icon="🎬"
)

st.title("🎬 Movie Knowledge Assistant")

st.write(
    "Ask questions about movies and get answers "
    "based on the provided movie information."
)


@st.cache_resource
def get_vectorstore():

    return create_vectorstore()


vectorstore = get_vectorstore()


question = st.text_input(
    "Enter your movie question:"
)


if question:

    context = retrieve_answer(
        vectorstore,
        question
    )

    prompt = f"""
You are a Movie Knowledge Assistant.

Answer the question based only on the movie
information provided in the context below.

If the answer is not available in the context,
say "I don't know".

Do not invent movie information.

Context:
{context}

Question:
{question}

Answer:
"""

    answer = ask_ollama(prompt)

    st.subheader("🤖 Answer:")

    st.write(answer)