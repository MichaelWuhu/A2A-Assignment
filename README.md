# A2A Assignment

## Setup
1. `python -m venv .venv`
2. `source .venv/bin/activate`
3. `pip install -r requirements.txt`

## Run Local
`python server/main.py`

## Deploy & Run Cloud
- **Cloud Run:** `gcloud run deploy echo-a2a-agent --source . --region us-central1 --allow-unauthenticated`
- **Agent Engine:** `PYTHONPATH=server python cloud/deploy_agent_engine.py`

## Test
`python client/demo.py`

**URL:** https://echo-a2a-agent-293994313057.us-central1.run.app