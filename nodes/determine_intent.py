from models.state import ToolState, IntentSchema
from utils.llm import model

intent_model = model.with_structured_output(IntentSchema)

def determine_intent(state: ToolState):
    intent = intent_model.invoke(state['user_input']).intent
    return {'intent': intent}
