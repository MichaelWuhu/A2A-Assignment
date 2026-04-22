# Section 3: Schema Analysis & Extension

#### Why does the request use a client-generated id rather than a server-generated one? What problem does this solve in distributed systems?

The request uses a client-generated id rather than a server-generated one so that if the client doesn't know if their message was able to get through, then they are able to let the server know that they already saw the ID and that it won't have to do it a second time. This fixes the problem of having things happening twice when they shouldn't which could be something like letting a purchase order go through twice.

---

#### The status.state can be 'working'. Under what circumstances would a server return this state in a non-streaming call, and how should a client react?

The server would return this state when a request is too large and is unable to be finished instantly. In this case, the client should respond by acknowledging it, waiting a few seconds, and then checking in on it later to see if the job is done.

--- 

#### What is the purpose of the sessionId field? Give a concrete example of two related tasks that should share a session.

The sessionId field is to help the agent remember the conversation so that it can remember any context that was previously talked about. An example is if you tell the agent that your name is "Joe" then it will still remember that your name is "Joe" and can do something like sign your name at the bottom of an email saying "Sincerely, Joe"

---

#### The parts array supports types text, file, and data. Describe a realistic multi-agent workflow where all three part types appear in a single conversation.

A realistic multi-agent workflow is uploading a picture of a math problem and asking the agent to help you solve it. The agent sees the photo and sends back text with the steps and the data as well so that the calculator is able to solve it.

---

# Section 4: Deploying the Agent Service to Cloud Run

### (a) what the --allow-unauthenticated flag does and its security implications 

The --allow-unauthenticated flag prevents any unwanted users from accessing the agent. Since unauthenticated is allowed, this means that hackers or bots can find my address and do things like spam messages costing me a lot of money.

--- 

### (b) how Cloud Run scales to zero and what cold start latency means for A2A clients.

Cloud run makes it so that Google turns off the agent if no one is talking to it so that it won't cost money. Cold start means that the first run may take longer since its been idle for a longer period of time.

---

# Section 5: Deploying to Vertex AI Agent Engine

### (a) the difference between deploying to Cloud Run vs Agent Engine in terms of operational burden and use-case fit, 

Deploying to Cloud Run builds from the ground up and is more work but will be exactly how the user wants it. Agent Engine on the other hand is already existing but the user gets less freedom.

---

### (b) why the wrapper class uses a synchronous query() method even though the underlying handler is async.

The wrapper class uses a synchronous query() method even though the underlying handler is async since it is more compatible with Vertex AI SDK.

---

# Section 6: How an A2A Client Connects to an A2A Server


### client/demo.py output

```bash
(.venv) michaelwu@Michaels-MacBook-Air A2A-Assignment % python client/demo.py

[REQUEST] GET https://echo-a2a-agent-293994313057.us-central1.run.app/.well-known/agent.json
[RESPONSE] 200 - {"id":"echo-agent-v1","name":"Echo Agent","version":"1.0.0",...
--- Agent Discovery ---
Agent Name: Echo Agent
Skills: ['Echo', 'Summarise']

--- Sending Task ---
Input: Hello from the client!

[REQUEST] POST https://echo-a2a-agent-293994313057.us-central1.run.app/tasks/send | Payload: {'id': '2457f46a-edf4-4b42-973b-7129d833e59a', 'sessionId': ...
[RESPONSE] 200 - {"id":"2457f46a-edf4-4b42-973b-7129d833e59a","status":{"stat...
Response: Hello from the client!
```

---

### UML sequence diagram

```
Actor User          A2AClient            Cloud Run (A2AServer)        handlers.py
    |                   |                         |                        |
    |----(1) Input ---->|                         |                        |
    |                   |---(2) GET /.well-known/agent.json -------------->|
    |                   |<------------- (Agent Card JSON) -----------------|
    |                   |                         |                        |
    |                   |---(3) POST /tasks/send ------------------------->|
    |                   |    (Task Payload)       |----(4) handle_task()-->|
    |                   |                         |                        |
    |                   |                         |<---(5) Result String---|
    |                   |<---(6) HTTP 200 OK -----|                        |
    |                   |    (Artifact JSON)      |                        |
    |<---(7) Output-----|                         |                        | 
```

### If a client loses the network connection after sending the POST but before receiving the response, how could it safely retry? What field in the A2A protocol helps with idempotency?

It can safely retry by sending the same requesting using the same identifier. The same identifier will make it so that the server won't reprocess it and will return a result if it exists already. The Task ID field in the A2A protocol helps with idempotency.