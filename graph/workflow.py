from langgraph.graph import StateGraph, START, END
from models.state import ToolState
from nodes.determine_intent import determine_intent
from nodes.call_weather import call_weather
from nodes.call_news import call_news
from nodes.generate_response import generate_response
from nodes.router import intent_router

def build_graph():
    graph = StateGraph(ToolState)

    graph.add_node("determine_intent", determine_intent)
    graph.add_node("weather_node", call_weather)
    graph.add_node("news_node", call_news)
    graph.add_node("generate_response", generate_response)

    graph.set_entry_point("determine_intent")
    graph.add_conditional_edges("determine_intent", intent_router)
    graph.add_edge("weather_node", "generate_response")
    graph.add_edge("news_node", "generate_response")
    graph.add_edge("generate_response", END)

    return graph.compile()
