import operator
from typing import Annotated, Sequence, TypedDict

from langchain_openai import ChatOpenAI
from langgraph.graph import END, StateGraph
from langchain_core.messages import BaseMessage, HumanMessage

class AgentState(TypedDict):
    question: str
    documents: list[str]
    generation: str
    iteration: int

def retrieve(state: AgentState):
    print("---RETRIEVING---")
    # Mock retrieval logic for demonstration
    return {"documents": ["Document content about multi-agent RAG..."], "iteration": state["iteration"] + 1}

def grade_documents(state: AgentState):
    print("---CHECKING DOCUMENT RELEVANCE---")
    # Mock grading logic
    return {"documents": state["documents"]}

def transform_query(state: AgentState):
    print("---TRANSFORMING QUERY---")
    # Logic to rewrite the question for better retrieval
    return {"question": f"Rewritten: {state['question']}"}

def generate(state: AgentState):
    print("---GENERATING---")
    return {"generation": "Multi-agent systems improve RAG by introducing self-correction loops..."}

def decide_to_generate(state: AgentState):
    if not state["documents"] and state["iteration"] < 3:
        return "rewrite"
    return "generate"

# Define the graph
workflow = StateGraph(AgentState)

# Add nodes
workflow.add_node("retrieve", retrieve)
workflow.add_node("grade_documents", grade_documents)
workflow.add_node("generate", generate)
workflow.add_node("transform_query", transform_query)

# Build graph
workflow.set_entry_point("retrieve")
workflow.add_edge("retrieve", "grade_documents")
workflow.add_conditional_edges(
    "grade_documents",
    decide_to_generate,
    {
        "rewrite": "transform_query",
        "generate": "generate",
    },
)
workflow.add_edge("transform_query", "retrieve")
workflow.add_edge("generate", END)

# Compile
app = workflow.compile()