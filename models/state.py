from typing import TypedDict, Literal
from pydantic import BaseModel, Field

class ToolState(TypedDict, total=False):
    user_input: str
    intent: Literal["weather", "news"]
    tool_result: str
    result: str
    invoked_tool: str

class IntentSchema(BaseModel):
    intent: Literal["weather", "news"] = Field(description="User's intent based on the query")
