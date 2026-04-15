from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Any, Optional
import uuid, datetime
from agent_card import AGENT_CARD
from handlers import handle_task

app = FastAPI(title='Echo Agent API')

# -- Endpoint 1: Agent Card --
@app.get('/.well-known/agent.json')
async def get_agent_card():
    if not AGENT_CARD:
        raise HTTPException(status_code=500, detail="Agent card not found")
    return AGENT_CARD


# -- Pydantic model for A2A task message schema --
class TextPart(BaseModel):
    type: str = 'text/plain'
    text: str

class Message(BaseModel):
    role: str       # "user" or "agent"
    parts: list[TextPart]

class TaskRequest(BaseModel):
    id: str         # client-generated task ID
    sessionId: Optional[str] = None  # optional session ID for context
    message: Message
    metadata: Optional[dict[str, Any]] = None

# -- Endpoint 2: Send Task --
@app.post('/task/send')
async def send_task(request: TaskRequest):
    result_text = await handle_task(request)
    result {
        'id': request.id,
        'status': {'state': 'completed'},
        'artifacts': [
            {
                'parts': [{
                    'type': 'text/plain',
                    'text': result_text
                }]
            }
        ]
    }