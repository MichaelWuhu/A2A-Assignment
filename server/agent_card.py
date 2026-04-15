
# Agent card definition for the Echo Agent
# To be transformed into a JSON file later, but defined as a Python dictionary for now
AGENT_CARD = {
    "id": "echo-agent-v1",
    "name": "Echo Agent",
    "version": "1.0.0",
    "description": "A simple agent that echoes back any text it receives.",
    "url": "http://localhost:8000",
    "capabilities": {
        "streaming": False,
        "pushNotifications": False
    },
    "defaultInputModes": ["text/plain"],
    "defaultOutputModes": ["text/plain"],
    "skills": [
        {
            "id": "echo",
            "name": "Echo",
            "description": "Returns the user message verbatim.",
            "inputModes": ["text/plain"],
            "outputModes": ["text/plain"]
        },
        {
            "id": "summarise",
            "name": "Summarise",
            "description": "Returns a one-sentence mock summary of the text.",
            "inputModes": ["text/plain"],
            "outputModes": ["text/plain"]
        }
    ],
    "contact": {
        "email": "your_email@example.com"
    }
}

# Summarisation function for the Echo Agent
def summarise(text):
    # Placeholder summarisation function that returns a fixed summary.
    # To change later
    return "This is a one-sentence summary of the provided text."


# Validate the agent card structure
def validate_card(card: dict) -> bool:
    # Return True if all required Agent Card fields are present.
    required_fields = ["id", "name", "version", "description", "url", "capabilities", "defaultInputModes", "defaultOutputModes", "skills", "contact"]
    for field in required_fields:
        if field not in card:
            print(f"Missing required field: {field}")
            return False

    if "email" not in card.get("contact", {}):
        print("Missing required contact email")
        return False

    return True
