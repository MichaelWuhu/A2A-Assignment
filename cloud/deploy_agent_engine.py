# cloud/deploy_agent_engine.py
import vertexai
from vertexai.preview import reasoning_engines
import sys, os

PROJECT_ID = 'a2a-assignment-michaelwu'
REGION     = 'us-central1'
STAGING_BUCKET = f'gs://{PROJECT_ID}-a2a-staging'

# Add the project root to path so we can import as 'server.agent_engine_wrapper'
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from server.agent_engine_wrapper import EchoAgent

vertexai.init(project=PROJECT_ID, location=REGION, staging_bucket=STAGING_BUCKET)

# Package and deploy
remote_agent = reasoning_engines.ReasoningEngine.create(
    EchoAgent(),
    requirements=[
        'fastapi==0.111.0',
        'uvicorn==0.29.0',
        'pydantic==2.7.0',
        'google-cloud-aiplatform[reasoningengine,langchain]',
    ],
    extra_packages=['server'],    
    display_name='Echo A2A Agent',
    description='A2A Lab — Echo Agent on Agent Engine',
)

print('Deployed! Resource name:', remote_agent.resource_name)
print('Engine ID:', remote_agent.resource_name.split('/')[-1])