
# Semantic Search App using OpenAI Embeddings
This is a simple Streamlit app I made to try out semantic search with OpenAI embeddings. You type in a query, and it finds the most relevant document from a small list based on meaning, not just keywords.
---
## Screenshot
Here is what the app looks like when running:

![App Screenshot](Data/app_screenshot.png)
## What it does
- Uses OpenAI's `text-embedding-3-small` model to convert text into vectors
- Calculates similarity between your query and some example docs
- Shows the closest matching document and similarity scores for all docs
- Built with Streamlit so it has a simple interactive UI
---
## How to run it
1. Install required packages:
```bash
pip install streamlit langchain-openai python-dotenv scikit-learn


