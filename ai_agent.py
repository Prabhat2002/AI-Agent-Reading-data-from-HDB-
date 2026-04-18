import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
import streamlit as st

from langchain_groq import ChatGroq
from langchain_community.utilities import SQLDatabase

# ✅ correct import
from langchain_community.agent_toolkits import create_sql_agent

# Load env
load_dotenv()

# ---------------- DB CONNECTION ----------------
connection_string = f"hana://{os.getenv('db_user')}:{os.getenv('db_password')}@{os.getenv('db_host')}:{os.getenv('db_port')}/{os.getenv('db_name')}"
engine = create_engine(connection_string)

# ✅ IMPORTANT FIX (no include_tables)
sql_db = SQLDatabase(
    engine,
    schema="DBADMIN"
)

# ---------------- GROQ ----------------
llm = ChatGroq(
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.5,
    model="llama-3.3-70b-versatile"
)

# ---------------- AGENT ----------------
agent = create_sql_agent(
    llm=llm,
    db=sql_db,
    verbose=True,
    handle_parsing_errors=True
)

# ---------------- STREAMLIT ----------------
st.title("🤖 HANA AI Agent")

query = st.text_input("Ask your question")

if query:
    with st.spinner("Thinking..."):
        try:
            response = agent.run(query)
            st.write(response)
        except Exception as e:
            st.error(e)