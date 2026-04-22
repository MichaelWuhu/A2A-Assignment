# server/agent_card.py

AGENT_CARD = {
    "id":          "echo-agent-v1",
    "name":        "Echo Agent",
    "version":     "1.0.0",
    "description": "A simple agent that echoes back any text it receives.",
    "url":         "https://echo-a2a-agent-bo6iuilfoq-uc.a.run.app",   # updated at deploy time
    "contact": {
        "email": "student@example.com"
    },
    "capabilities": {
        "streaming": False,
        "pushNotifications": False
    },
    "defaultInputModes":  ["text/plain"],
    "defaultOutputModes": ["text/plain"],
    "skills": [
        {
            "id":          "echo",
            "name":        "Echo",
            "description": "Returns the user message verbatim.",
            "inputModes":  ["text/plain"],
            "outputModes": ["text/plain"]
        },
        {
            "id":          "summarise",
            "name":        "Summarise",
            "description": "Returns a concise summary of the input text.",
            "inputModes":  ["text/plain"],
            "outputModes": ["text/plain"]
        }
    ]
}

def validate_card(card: dict) -> bool:
    """
    Checks if the Agent Card contains all mandatory A2A fields.
    Returns True if valid, False if any required keys are missing.
    """
    required_fields = [
        "id", "name", "version", "description", "url", 
        "capabilities", "defaultInputModes", "defaultOutputModes", 
        "skills", "contact"
    ]
    
    # Check for top-level required fields
    for field in required_fields:
        if field not in card:
            return False
            
    # Check for the required 'email' key inside 'contact'
    if "email" not in card["contact"]:
        return False
        
    return True