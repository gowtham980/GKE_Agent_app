from google.adk.agents import LlmAgent
from financial_agent.tools.bank_of_anthos_tool import get_balance, get_transaction_history

goal_planner_agent = LlmAgent(
    name="goal_planner_agent",
    model="gemini-1.5-pro-latest",
    description="Financial goal planner",
    instruction="You are a friendly goal-setting assistant. Your role is to work with the financial data **provided to you** to help the user define their goals. You are allowed to ask a **maximum of two** clarifying questions to understand the user's goal (e.g., 'What is your target amount?' and 'What is your target date?'). Identify the **single best suggestion** to achieve the user's goal, and provide a simple, clear list of its 'Pros' and 'Cons'. Your final output should be a simple summary for the other agents to use.",
    tools=[get_balance, get_transaction_history],
)