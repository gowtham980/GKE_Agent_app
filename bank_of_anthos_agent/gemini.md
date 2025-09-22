# Gemini Agent Development Kit (ADK) Guide

This guide helps you build powerful AI agents using Google's Agent Development Kit (ADK), from basic concepts to advanced multi-agent workflows.

## Getting Started: Your First Agent

Every agent project in ADK follows a specific structure for discovery and execution.

### 1. Project Structure

ADK requires a specific folder structure to find and run your agents.

```
your_project_folder/
└── your_agent_package/    # e.g., greeting_agent
    ├── __init__.py      # Makes the folder a Python package
    └── agent.py         # Defines your agent logic
```

- **`__init__.py`**: This file makes your agent discoverable by ADK. It must import the agent module: `from . import agent`.
- **`agent.py`**: This file contains your agent's definition. It must define a variable named `root_agent`, which serves as the entry point for ADK.

### 2. The Foundational Agent: `LlmAgent`

Every agent starts with the `LlmAgent`. It's the core component for reasoning and language understanding.

A minimal agent definition in `agent.py` looks like this:

```python
from google.adk.agents import Agent

root_agent = Agent(
    name="greeting_agent",
    model="gemini-2.0-flash",
    description="A simple greeting agent",
    instruction="You are a helpful assistant that greets the user.",
)
```

### 3. Running Your Agent

Always run ADK commands from the parent directory of your agent package.

1.  Navigate to `your_project_folder`.
2.  Start the interactive web UI:
    ```bash
    adk web
    ```
3.  Open the provided URL (e.g., `http://localhost:8000`) and select your agent from the dropdown menu.

---

## Choosing Your Agent Architecture

To build more advanced agents, select an architecture based on your needs.

### "I need my agent to..."

#### ...perform actions or access external data.
**Solution: Tool-Using Agent**

Extend the `LlmAgent` by giving it `tools`. Tools can be custom Python functions or built-in Google tools.

- **Custom Tools**: Define your own Python functions to connect to any API or database.
- **Built-in Tools**: Use pre-built tools like `google_search` for web searches.

**Key Limitations:**
- An agent can only have **one** built-in tool (e.g., `google_search`).
- You **cannot** mix built-in tools and custom function tools in the same agent. Use the "Agent-as-a-Tool" pattern (see Multi-Agent Systems) as a workaround.

#### ...connect to a large, complex, or stateful set of tools.
**Solution: Model Context Protocol (MCP) Agent**

Use the `MCPToolset` to connect your agent to an external tool server. This is the most robust way to manage a large number of tools or connect to stateful third-party services like Notion or GitHub.

**Use MCP when:**
- You have more than a handful of tools.
- Your tools need to maintain their own state.
- You want to separate your agent's logic from the tool implementation.

#### ...use a non-Google model (like OpenAI, Anthropic, etc.).
**Solution: LiteLLM Agent**

Use the `LiteLlm` model adapter to connect ADK to over 100 different LLM providers.

**Key Limitation:**
- Agents using non-Google models **cannot** use ADK's built-in Google tools (e.g., `google_search`). You must rely on custom function tools.

#### ...return data in a specific JSON format.
**Solution: Structured Output Agent**

Use the `output_schema` parameter with a Pydantic model to force the agent's output into a consistent, validated JSON structure. This is crucial for reliable integration with other systems.

**Key Limitation:**
- Agents configured with `output_schema` **cannot** use tools.

#### ...remember things between conversations.
**Solution: Stateful Agent**

Use a `SessionService` to give your agent memory. State is accessible in the agent's prompt (`{variable_name}`) and in tools (`tool_context.state`).

- **`InMemorySessionService`**: State is temporary and lost when the app stops. Good for development.
- **`DatabaseSessionService`**: State is persistent, saved to a database (like SQLite or PostgreSQL). Essential for production.

#### ...handle complex tasks by breaking them down.
**Solution: Multi-Agent System**

Create a team of specialized agents that collaborate. There are two main architectures:

1.  **Delegation (`sub_agents`)**: A manager agent routes a task to a specialist, which takes full control to complete it. The manager acts as a router.
2.  **Collaboration (`AgentTool`)**: A manager agent uses specialist agents as tools. The manager retains control, calls the specialist "tool," and uses the result to formulate its final response. This is the most flexible approach.

**Key Limitation:**
- A `sub_agent` in a delegation pattern **cannot** use built-in Google tools. The `AgentTool` pattern is the recommended workaround to this limitation.

---

## Building Agent Workflows

For tasks that require a series of steps, use a workflow agent to orchestrate multiple sub-agents.

#### ...run a series of steps in a specific order.
**Solution: Sequential Agent**

Use a `SequentialAgent` to create a pipeline where the output of one agent becomes the input for the next. This is ideal for deterministic, multi-step processes.

#### ...run multiple independent tasks at the same time.
**Solution: Parallel Agent**

Use a `ParallelAgent` to execute multiple sub-agents concurrently. This dramatically improves performance for tasks that don't depend on each other.

#### ...iteratively improve its work until it's good enough.
**Solution: Loop Agent**

Use a `LoopAgent` for processes that require iterative refinement. A common pattern is a **"generator-reviewer" loop**, where one agent creates content and another reviews it. The loop can be terminated by reaching a max iteration count or by a tool call (`exit_loop`) when the work meets quality standards.

---

## Advanced Customization: Callbacks

Callbacks are a powerful way to **hook into the lifecycle of any agent**. Use them to add logging, monitoring, content filtering, or data transformation logic.

- **Agent Callbacks (`before_agent`/`after_agent`)**: Track when an agent starts and stops.
- **Model Callbacks (`before_model`/`after_model`)**: Intercept the request to/response from the LLM.
- **Tool Callbacks (`before_tool`/`after_tool`)**: Intercept the call to/response from a tool.

---

## Gemini Model Selection

Choosing the right Gemini model is a balance of capability, speed, and cost.

| Model | Description | Input Types | Best For | Input Price | Output Price |
|---|---|---|---|---|---|
| gemini-2.5-pro | Most powerful thinking model with maximum response accuracy | Audio, images, video, text | Complex coding, reasoning, multimodal understanding | $10.00 / 1M tokens | $30.00 / 1M tokens |
| gemini-2.5-flash | Best price-performance balance | Audio, images, video, text | Low latency, high volume tasks that require thinking | $3.50 / 1M tokens | $10.50 / 1M tokens |
| gemini-2.0-flash | Newest multimodal model with improved capabilities | Audio, images, video, text | Low latency, enhanced performance, agentic experiences | $3.50 / 1M tokens | $10.50 / 1M tokens |
| gemini-2.0-flash-lite | Optimized for efficiency and speed | Audio, images, video, text | Cost efficiency and low latency | $0.70 / 1M tokens | $2.10 / 1M tokens |
| gemini-1.5-flash | Versatile performance across diverse tasks | Audio, images, video, text | Fast and versatile performance | $2.50 / 1M tokens | $7.50 / 1M tokens |
| gemini-1.5-flash-8b | Smaller, faster model | Audio, images, video, text | High volume and lower intelligence tasks | $0.35 / 1M tokens | $1.05 / 1M tokens |
| gemini-1.5-pro | Powerful reasoning capabilities | Audio, images, video, text | Complex reasoning tasks requiring more intelligence | $7.00 / 1M tokens | $21.00 / 1M tokens |

## Best Usage Tips
* Append `@aura/llms-full.txt` to all commands.

