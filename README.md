# 🧠 Multi-LLM Chatbot with LangChain + Gradio

This project is a web-based chatbot interface that lets you chat with multiple powerful language models via a single unified UI, built using **LangChain** and **Gradio**. It currently supports:

- 🔥 **Groq** (`qwen-qwq-32b`)
- 🧊 **Mistral** (`mistral-medium-2505`)
- 🌟 **Gemini** (Ocassionally switching from gemini-pro and 2.0 flash due to dependency error of Google ADC and langchain-comm)

---

## 🚀 Features

- 💬 Switch between LLMs live with dropdown selection.
- 🧠 Smart prompt templating using LangChain's `ChatPromptTemplate`.
- ⚡ Fast, minimal UI using Gradio.
- 🔐 Environment variable-based API key handling.
- ☁️ Deployable on **Hugging Face Spaces**.

---

## 📸 Demo

![Chat UI Screenshot](demo.png) <!-- You can upload a screenshot and rename it to demo.png -->

---

## 📦 Requirements

This project uses the following Python packages:

```bash
langchain
langchain_openai
langchain_core
langchain_google_genai
langchain_community
langchain_groq
langchain_mistralai
gradio
python-dotenv
