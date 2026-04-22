# server/main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Any, Optional
import uuid, datetime
from .agent_card import AGENT_CARD
from .handlers import handle_task

app = FastAPI(title='Echo A2A Agent')

# ── Health Endpoint ──────────────────────────────────────────────
@app.get('/health')
async def health_check():
    # Returns the agent ID from the card as required [cite: 65]
    return {"status": "ok", "agent": AGENT_CARD["id"]}

# ── Endpoint 1: Agent Card ──────────────────────────────────────────
@app.get('/.well-known/agent.json')
async def get_agent_card():
    return AGENT_CARD

# ── Pydantic models for the A2A task message schema ─────────────────
class TextPart(BaseModel):
    type: str = 'text'
    text: str

class FilePart(BaseModel):
    type: str = 'file'
    url: str
    mimeType: str

# Update Message to accept either TextPart or FilePart
class Message(BaseModel):
    role: str           # 'user' or 'agent'
    parts: list[TextPart | FilePart]  

class TaskRequest(BaseModel):
    id: str             # client-generated task ID
    sessionId: Optional[str] = None
    message: Message
    metadata: Optional[dict[str, Any]] = None

# ── Endpoint 2: Send Task ────────────────────────────────────────────
@app.post('/tasks/send')
async def send_task(request: TaskRequest):
    # Error handling: Raise 400 if no parts are provided [cite: 66]
    if not request.message.parts:
        raise HTTPException(status_code=400, detail="Message parts cannot be empty")

    result_text = await handle_task(request)
    return {
        'id':     request.id,
        'status': {'state': 'completed'},
        'artifacts': [
            {
                'parts': [{'type': 'text', 'text': result_text}]
            }
        ]
    }
    
    
 