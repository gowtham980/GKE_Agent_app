# Project Story: Aura, the AI Financial Advisor for Bank of Anthos

## Inspiration

Our inspiration came directly from the GKE is Turning 10 Hackathon's core challenge: **"Give an existing microservice application an AI upgrade."** We were drawn to the popular "Bank of Anthos" sample application, a classic example of a distributed microservices architecture.

We saw an opportunity to do more than just add a chatbot. We wanted to build an external "brain" that could intelligently interact with the bank's existing services, providing a new layer of personalized, conversational financial guidance for its users. The goal was to create "Aura," a friendly and approachable AI financial advisor that makes understanding personal finance as easy as talking to a friend, all without modifying a single line of the original Bank of Anthos code.

## What it does

Aura is a personalized financial co-pilot for Bank of Anthos customers. It manifests as a simple, conversational mobile app built with Flutter.

Here's the user journey:
1.  A user logs in with their standard Bank of Anthos credentials.
2.  They are presented with a chat interface to talk to Aura.
3.  Users can ask natural language questions like, "What's my current balance?", "Show me my recent transactions," or "Based on my spending, should I be investing more?"
4.  Behind the scenes, Aura securely uses the user's session to communicate with the Bank of Anthos APIs, retrieves their real-time financial data, and uses the power of Gemini to provide intelligent, context-aware answers and personalized financial tips.

## How we built it

We built a full-stack solution leveraging the power of Google Cloud and modern development frameworks.

*   **AI Backend (The "Brain"):** The core of our project is the Aura agent, a multi-agent system built in Python using the **Google Agent Development Kit (ADK)**. Its intelligence and reasoning are powered by the **Gemini 1.5 Pro** model. The agent is exposed via a FastAPI server.

*   **Containerization & Orchestration:** The entire Python agent is containerized using **Docker**. We deployed this container to a **GKE Autopilot cluster**, allowing it to run alongside the existing Bank of Anthos services and communicate with them over the internal cluster network.

*   **Frontend (The "Face"):** We developed a cross-platform mobile application using **Flutter**. This provides the user-friendly chat interface where users interact with Aura. The Flutter app handles user authentication against the Bank of Anthos `userservice` and passes the secure JWT token to the agent with each request.

## Built With
*   **Languages:** Python, Dart
*   **Frameworks:** Google Agent Development Kit (ADK), FastAPI, Flutter
*   **Platforms & Cloud Services:**
    *   Google Kubernetes Engine (GKE) Autopilot
    *   Google Artifact Registry
    *   Docker
*   **APIs & AI Models:**
    *   Google Gemini 1.5 Pro
    *   Bank of Anthos internal REST APIs

## Challenges we ran into

1.  **Black-Box Integration:** The primary challenge was integrating with Bank of Anthos without touching its source code. This meant we had to reverse-engineer the internal REST API calls for services like `balancereader` and `transactionhistory` to build a compatible client tool for our agent.

2.  **Kubernetes Networking:** We initially faced connectivity issues between our agent's pod and the bank's internal services. Debugging this required inspecting pod logs and understanding GKE service discovery. A key "aha!" moment was realizing our Python `requests` library needed the `http://` prefix for the service name (e.g., `http://balancereader:8080`), which wasn't immediately obvious.

3.  **Data Formatting:** The Bank of Anthos APIs return monetary values as integers in cents. We had to build logic into our agent's tools to correctly convert these values into a human-readable dollar format before presenting them to the user, ensuring the financial information was clear and accurate.

## Accomplishments that we're proud of

*   **A True "AI Upgrade":** We successfully built a smart, external intelligence layer that adds significant value to an existing application without any modification to the original codebase.
*   **Full-Stack Implementation:** We're proud of creating a complete, end-to-end solution, from the GKE-hosted AI backend and its internal API integrations to the polished, cross-platform Flutter mobile app.
*   **Modern Cloud-Native Architecture:** Deploying a containerized Python AI agent on GKE demonstrates a modern, scalable, and robust approach to building and managing AI applications.

## What we learned

This hackathon was a fantastic learning experience. We gained hands-on experience with:
*   **GKE Autopilot:** Understanding the ease of deploying and managing containerized applications without needing to manage the underlying node infrastructure.
*   **Google ADK & Gemini:** How to structure and build sophisticated, tool-using AI agents.
*   **Microservice Interaction:** The practical challenges and solutions for making new services communicate with existing ones in a distributed environment.
*   **Flutter Development:** Building a clean, responsive UI for a mobile application that interacts with a backend API.

## What's next for Aura

This project is a strong foundation, and we see many exciting possibilities for the future:

*   **Expanded Capabilities:** Integrate with more Bank of Anthos services to allow users to perform actions, such as transferring funds or setting up payments, directly through conversation.
*   **Proactive Insights:** Enhance the agent's intelligence to proactively analyze a user's spending and offer unsolicited advice, like identifying potential savings or flagging unusual transactions.
*   **Long-Term Memory:** Give Aura a persistent memory, allowing it to remember user goals and past conversations for a truly personalized, long-term financial wellness journey.
*   **Richer Visualizations:** Add charts and graphs to the Flutter app to provide users with a more visual understanding of their financial data.