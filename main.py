from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate   
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq

import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()

#langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "TRUE"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

#Prompt Template
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "you are a helpful assistant. Please answer the questions of the users as best you can."),
        ("user", "Question: {question}")
    ]
)

# streamlit framework
st.title("Langchain Chatbot with Gemini and Groq")
input_text= st.text_input("Ask your question here: ")

#gemini model llm
llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.6
)
output_parser= StrOutputParser() 
chain= prompt | llm | output_parser

#groq model llm
groq_llm = ChatGroq(
    model="qwen-qwq-32b",
    temperature=0.6
)

llm_choice= st.selectbox(
    "Select LLM",
    options=["Gemini", "Groq"],
    index=1
)

if input_text:
    st.write(chain.invoke({"question":input_text}))

