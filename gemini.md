# GKE is Turning 10 Hackathon: The "Aura" Financial Advisor Agent

## 1. Project Overview

This document outlines the plan for our project for the **GKE is Turning 10 Hackathon**. The project is to adapt the existing "Aura" agent, a sophisticated multi-agent financial assistant, to work with the "Bank of Anthos" sample application. The goal is to create a unique and technically impressive "AI upgrade" that aligns with the hackathon's problem statement.

The final product will be a containerized AI agent, deployed on GKE, that acts as a **Personalized Financial Advisor** for Bank of Anthos users.

## 2. Core Hackathon Challenge

The solution directly addresses the hackathon's core challenge: **"Give an existing microservice application an AI upgrade."**

- **Constraint:** We will not touch the core Bank of Anthos application code.
- **Method:** We will build a new, containerized component (the Aura agent) that interacts with the application's existing REST APIs.
- **Goal:** Build a smart, external brain that adds a new layer of intelligence and personalization.

## 3. Hackathon Alignment & Deliverables

### Technology Requirements

- **Required:**
    - **Google Kubernetes Engine (GKE):** The Aura agent will be containerized and deployed on a GKE cluster.
    - **Google AI Models (Gemini):** The agent's intelligence is powered by the Gemini family of models.
- **Optional:**
    - **Agent Development Kit (ADK):** The Aura agent is built using a custom agentic framework, similar in principle to the ADK.
    - **Model Context Protocol (MCP):** We are opting for direct REST communication for a more lightweight and direct integration, instead of using MCP.
    - **Gemini CLI:** We are actively using the Gemini CLI to accelerate development and manage our workflow.

### Submission Checklist

- [ ] URL to the hosted Project (Web UI for the agent)
- [ ] Text description summarizing the project
- [ ] URL to public code repo
- [ ] Architecture Diagram
- [ ] ~3-minute demo video

## 4. Resources

- **[Bank of Anthos Repo](https://github.com/GoogleCloudPlatform/bank-of-anthos)**
- **[Bank of Anthos Development Guide](https://github.com/GoogleCloudPlatform/bank-of-anthos/blob/main/docs/development.md)**
- **[GKE Documentation](https://cloud.google.com/kubernetes-engine/docs)**
- **[Gemini CLI Repo](https://github.com/GoogleCloudPlatform/gemini-cli)**

## 5. Our Solution: The 'Aura' Agent

Our solution is the "Aura" agent, a pre-built, advanced agentic system.

- **Functionality:** It analyzes a user's financial data (transactions, balances) and provides personalized, conversational advice.
- **Persona:** It's designed as a "Financial Friend". It's relatable, uses analogies, and encourages a two-way conversation.
- **Architecture:** It's a multi-agent system. A `root_agent` coordinates with specialized sub-agents (`goal_planner_agent`, `simulator_agent`, `optimizer_agent`, `fact_checker_agent`) to deliver insightful and verified advice. This architecture is a key differentiator.

## 6. Technical Architecture & Integration Plan

The agent will be integrated with Bank of Anthos using the following architecture:

1.  **Base Application:** The standard Bank of Anthos application will be deployed to a **GKE Autopilot cluster**.
2.  **AI Agent:** The `aura` agent will be containerized using its `Dockerfile` and deployed as a separate set of pods on the same GKE cluster.
3.  **Communication Protocol:** The agent will create a custom tool that acts as a **REST client**. This tool will communicate directly with the Bank of Anthos's internal microservices, specifically the `transaction-history` and `balance-reader` services, using their native REST APIs.
4.  **Intelligence Core:** The agent's logic is powered by Gemini models. It will take the data fetched via the REST tool and use it to generate financial advice.
5.  **API Server:** The agent is exposed via a FastAPI web server defined in `main.py`, which can be connected to a simple UI.

## 7. Key Files & Logic

- **`financial_agent/agent.py`:** Defines the core `root_agent`, its sophisticated persona, and its multi-agent structure. This is the "brain" of the operation.
- **`main.py`:** The FastAPI server that exposes the agent's chat functionality via an API endpoint.
- **`financial_agent/tools/bank_of_anthos_tool.py` (To Be Created):** This is the most critical new component. It will be a custom tool containing a Python REST client. This tool will be responsible for all communication with the Bank of Anthos application.
- **`Dockerfile`:** Defines the Python environment and commands to containerize the agent for deployment on GKE.

## 8. Primary Goal for Gemini CLI

Based on this context, the primary task is to **create the REST client tool**. This involves understanding the REST API endpoints from the Bank of Anthos source code and implementing a Python tool that can call the `GET /balances/{accountId}` and `GET /transactions/{accountId}` endpoints, returning the data in a structured format for the `root_agent` to use.

## 9. Cluster Details

kubeclt get service frontend -o wide --watch
NAME       TYPE           CLUSTER-IP       EXTERNAL-IP     PORT(S)        AGE    SELECTOR
frontend   LoadBalancer   34.118.239.209   34.41.186.197   80:31137/TCP   7h4m   app=frontend,application=bank-of-anthos,environment=development,team=frontend,tier=web