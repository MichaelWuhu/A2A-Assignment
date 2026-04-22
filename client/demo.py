# client/demo.py
from client import A2AClient

def main():
    agent_url = "https://echo-a2a-agent-293994313057.us-central1.run.app"
    
    # Using the client as a context manager ensures close() is called
    with A2AClient(agent_url) as client:
        # 1. Fetch and print Agent Card details
        card = client.fetch_agent_card()
        print(f"--- Agent Discovery ---")
        print(f"Agent Name: {card.get('name')}")
        
        # 2. Print skills
        skills = client.get_skills()
        print(f"Skills: {[s.get('name') for s in skills]}")
        
        # 3. Send a task
        print(f"\n--- Sending Task ---")
        input_text = "Hello from the client!"
        print(f"Input: {input_text}")
        
        response = client.send_task(input_text)
        
        # 4. Extract and print response
        output_text = client.extract_text(response)
        print(f"Response: {output_text}")

if __name__ == "__main__":
    main()