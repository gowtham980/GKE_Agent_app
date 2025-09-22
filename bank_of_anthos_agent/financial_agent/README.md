# Financial Agent Design

This document outlines the architecture and design of the `financial_agent`, a multi-agent system designed to act as a personal financial assistant named Aura.

## High-Level Overview

The `financial_agent` is designed to be a friendly, relatable, and helpful financial companion. Its primary goal is to simplify personal finance for the user through a conversational interface. It achieves this by breaking down complex financial analysis into specialized tasks handled by a team of collaborating agents. The user interacts only with the main agent, "Aura," which orchestrates the work of the other agents behind the scenes.

## Architecture

The system is built around a central "manager" agent (`root_agent`) that delegates tasks to a set of specialized "sub-agents." This follows a multi-agent collaboration pattern where each agent has a distinct role and set of capabilities.

### `financial_agent` (The Root Agent - "Aura")

This is the user-facing agent. It is responsible for all communication with the user.

- **Persona**: Aura is designed to be a "Financial Friend" – relatable, encouraging, and able to explain complex topics using simple analogies.
- **Core Mission**:
    1.  **Guide the User**: Aura is the single point of contact. It synthesizes the analysis from its sub-agents to provide the single most impactful recommendation.
    2.  **Foster Interaction**: It presents information concisely and always ends with a question to encourage a two-way conversation.
    3.  **Data-Driven**: It always uses its tools to fetch financial data before engaging in conversation.
    4.  **Provide Fact-Checked Tips**: It delivers interesting and surprising financial tips that have been verified for accuracy by the `fact_checker_agent`.
- **Tools**:
    - `MCPToolset`: Connects to an external financial data service to get the user's real-time financial information. It also includes a `login_mcp` function to handle authentication with the service.
    - `export_data`: A simple tool to export a financial summary to a text file.

### Sub-Agents

These are the specialist agents that perform specific analytical tasks. They do not interact with the user directly.

#### 1. `goal_planner_agent`

- **Role**: A friendly goal-setting assistant.
- **Function**: It uses the user's financial data to help them define and plan for their financial goals. It is designed to be very focused, asking a maximum of two questions to clarify a goal before providing a suggestion with clear "Pros" and "Cons."

#### 2. `optimizer_agent`

- **Role**: A financial fitness coach.
- **Function**: This agent analyzes the user's financial data to find the single best way to make their money work harder (e.g., improving investment performance, reducing fees). It operates without asking any questions and frames its suggestions in a positive, encouraging manner.

#### 3. `simulator_agent`

- **Role**: A "Financial Time Machine."
- **Function**: This is a `LoopAgent` that creates a compelling, story-based projection of the user's financial future. It works in a two-step loop:
    1.  **`generator_agent`**: Creates a simple, exciting story about a potential financial future based on the data.
    2.  **`reviewer_agent`**: Silently reviews the story. If it's good, it approves it. If it needs changes, it provides feedback to the generator. This loop ensures the final story is data-driven and impactful.
- **Constraint**: The loop is set to run for a maximum of one iteration to keep the process quick and efficient.

#### 4. `fact_checker_agent`

- **Role**: A fact-checker for financial tips.
- **Function**: This agent's sole purpose is to verify the accuracy of any financial statement or tip. It uses Google Search to find reliable sources and confirms whether a statement is accurate, providing a brief explanation. This ensures the advice Aura gives is trustworthy.

## Workflow

1.  The user sends a message to Aura (the `financial_agent`).
2.  Aura analyzes the request. If it needs financial data, it uses the `MCPTool` to fetch it. This may involve calling the `login_mcp` function.
3.  Based on the user's query, Aura delegates the task to the most appropriate sub-agent(s):
    - For goal-setting, it calls the `goal_planner_agent`.
    - To optimize finances, it calls the `optimizer_agent`.
    - To see future impact, it calls the `simulator_agent`.
4.  The sub-agent performs its analysis and returns a structured result (e.g., a suggestion with Pros and Cons) to Aura.
5.  If Aura wants to provide an interesting financial tip, it first sends the tip to the `fact_checker_agent` for verification.
6.  Aura synthesizes the information from its sub-agents, selects the single most important insight, and formulates a friendly, conversational response.
7.  Aura presents the response to the user, ending with a question to continue the conversation.

This multi-agent design allows for a clear separation of concerns, making the system robust, scalable, and capable of providing sophisticated yet easy-to-understand financial guidance.