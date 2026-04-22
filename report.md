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
