from models.state import ToolState
from typing import TypedDict, Literal

def intent_router(state: ToolState) -> Literal["weather_node", "news_node"]:
    return "weather_node" if state["intent"] == "weather" else "news_node"
