from langgraph.graph import StateGraph

from .state import AgentState
from .service import generate_answer
from .tools.search import search_documents


builder = StateGraph(AgentState)

builder.add_node(
    "search",
    search_documents,
)

builder.add_node(
    "generate",
    generate_answer,
)

builder.set_entry_point("search")

builder.add_edge(
    "search",
    "generate",
)

builder.set_finish_point(
    "generate"
)

graph = builder.compile()