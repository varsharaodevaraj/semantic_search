# PDF Semantic Search
This is my learning project where I created a simple basic Streamlit web app,
that allows users to upload any PDF document and ask natural language questions about its content. 
It uses semantic search powered by embeddings and vector similarity to find the most relevant sections of the document.

## Features
- Upload any PDF document
- Split the document into smaller chunks for better search accuracy
- Generate embeddings locally for semantic understanding
- Use cosine similarity to find relevant answers based on user queries
- Interactive web interface built with Streamlit

## How to Run
1. Clone the repository:
git clone https://github.com/your-username/pdf-semantic-search.git
cd pdf-semantic-search

2.Create a virtual environment and activate it:
python -m venv venv
 - On Windows:
venv\Scripts\activate
 - On macOS/Linux:
source venv/bin/activate

3.Install the required packages:
pip install -r requirements.txt

4.Run the Streamlit app:
streamlit run app.py

5.Open your browser and go to:
http://localhost:8501

--> Upload a PDF and start asking questions!
