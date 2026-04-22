# server/handlers.py
from .agent_card import AGENT_CARD

async def handle_task(request) -> str:
    text_parts = [p.text for p in request.message.parts if p.type == 'text']
    combined = ' '.join(text_parts)
    
    # Check if the first word is !summarise 
    if combined.startswith('!summarise'):
        return "This is a mock summary of the provided text for the A2A lab."
    
    # ECHO skill: return the input unchanged [cite: 63]
    return combined