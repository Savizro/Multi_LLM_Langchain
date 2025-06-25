from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_groq import ChatGroq
import gradio as gr

import os
from dotenv import load_dotenv


# Load environment variables
load_dotenv()
os.environ["LANGCHAIN_TRACING_V2"] = "TRUE"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["GEMINI_API_KEY"] = os.getenv("GEMINI_API_KEY")
os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")
os.environ["MISTRAL_API_KEY"] = os.getenv("MISTRAL_API_KEY")

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Please answer the questions of the users as best you can."),
    ("user", "Question: {question}")
])
output_parser = StrOutputParser()

gemini_llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.6
)
groq_llm = ChatGroq(
    model="qwen-qwq-32b",
    temperature=0.6
)

mistral_llm = ChatGroq(
    model="mistral-7b",
    temperature=0.4
)

def chatllm(question, model_choice):
    if not question:
        return "Please enter a question."
    
    llm = gemini_llm if model_choice == "Gemini" else groq_llm
    response = (prompt | llm | output_parser).invoke({"question": question})
    return response

iface = gr.Interface(
    fn=chatllm,
    inputs=[
        gr.Textbox(label="Ask your question here:"),
        gr.Dropdown(["Gemini", "Groq"], value="Groq", label="Select LLM")
    ],
    outputs=gr.Textbox(label="Response"),
    title="Langchain Chatbot with Gemini and Groq",
    description="Ask any question and get responses from Gemini or Groq-powered LLMs."
)
# failsafe!!
if __name__ == "__main__":
    iface.launch(share=True)
