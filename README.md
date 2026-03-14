# Agentic RAG with LangGraph 🤖🔍

[![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![LangGraph](https://img.shields.io/badge/LangGraph-Stateful_Agents-orange)](https://github.com/langchain-ai/langgraph)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o-green)](https://openai.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This repository implements a **Stateful Multi-Agent RAG (Retrieval-Augmented Generation)** system using **LangGraph**. Unlike traditional linear RAG pipelines, this agentic approach incorporates self-correction, document grading, and iterative query rewriting to ensure the highest quality of generated responses.

## 🌟 Key Features

- **🔄 Self-Correcting Retrieval**: Automatically evaluates retrieved documents for relevance.
- **🧠 Query Rewriting**: If initial results are poor, the agent rewrites the query to better explore the vector space.
- **📊 Document Grading**: A specialized agent grades documents to filter out noise before generation.
- **🛡️ Hallucination Guardrails**: Final output is verified against the context to prevent hallucinations.
- **📈 Stateful Logic**: Uses LangGraph's state management to maintain context across multiple reasoning steps.

## 🏗️ Architecture

The system follows a sophisticated graph-based workflow:

1.  **Router**: Determines if the query requires a vector search or can be answered directly.
2.  **Retriever**: Fetches documents from the vector database.
3.  **Grader**: Analyzes documents for relevance to the user's query.
4.  **Rewriter**: If documents are irrelevant, it transforms the query for a better second attempt.
5.  **Generator**: Synthesizes the final answer from graded context.

## 🚀 Getting Started

### Prerequisites
- Python 3.9+
- OpenAI API Key

### Installation
`ash
git clone https://github.com/amanarora133/Agentic-RAG-LangGraph.git
cd Agentic-RAG-LangGraph
pip install -r requirements.txt
`

### Usage
`python
from agent import app

inputs = {"question": "How do multi-agent systems improve RAG reliability?"}
for output in app.stream(inputs):
    for key, value in output.items():
        print(f"Node '{key}':")
        print(value)
`

## 🛠️ Tech Stack
- **Orchestration**: LangGraph, LangChain
- **LLMs**: OpenAI GPT-4o
- **Vector DB**: ChromaDB / Pinecone
- **Evaluation**: RAGAS

---
Developed with ❤️ by [Aman Arora](https://github.com/amanarora133)