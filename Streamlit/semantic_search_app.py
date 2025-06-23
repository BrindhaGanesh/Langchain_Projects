import streamlit as st
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import os

st.set_page_config(page_title="Semantic Search Demo")
st.title("🔍 Semantic Search with OpenAI Embeddings")

# Debug
st.write("App started.")

load_dotenv()

try:
    embedding = OpenAIEmbeddings(model="text-embedding-3-small", dimensions=300)
except Exception as e:
    st.error(f"Error loading embeddings: {e}")
    st.stop()

documents = [
    'Lionel Messi dazzles the football world with his vision, dribbling, and unmatched goal-scoring finesse.',
    'Usain Bolt is the fastest man alive, known for his electrifying speed and Olympic gold streak.',
    'Serena Williams dominates the tennis court with power, precision, and a record-breaking Grand Slam legacy.',
    'Sachin Tendulkar is a cricket legend, revered for his technical mastery and countless international records.',
    'Michael Phelps reigns in the pool, with 23 Olympic golds marking him as the most decorated swimmer in history.'
]

query = st.text_input("Enter your query:", "tell me about Serena Williams")

if st.button("Search"):
    with st.spinner("Calculating similarity..."):
        try:
            doc_embeddings = embedding.embed_documents(documents)
            query_embedding = embedding.embed_query(query)
            similarity_scores = cosine_similarity([query_embedding], doc_embeddings)
            best_idx = similarity_scores.argmax()

            st.markdown("### ✅ Most Relevant Document")
            st.write(documents[best_idx])
            st.markdown(f"**Similarity Score:** {similarity_scores[0][best_idx]:.4f}")

            st.markdown("### 📊 Ranked Results")
            sorted_indices = similarity_scores[0].argsort()[::-1]
            for idx in sorted_indices:
                st.write(f"Score: {similarity_scores[0][idx]:.4f} - {documents[idx]}")

        except Exception as e:
            st.error(f"An error occurred during embedding or similarity: {e}")
