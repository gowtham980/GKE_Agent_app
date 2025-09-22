from google.adk.agents import LlmAgent
from financial_agent.tools.bank_of_anthos_tool import get_balance, get_transaction_history

optimizer_agent = LlmAgent(
    name="optimizer_agent",
    model="gemini-2.5-flash",
    description="Financial optimizer",
    instruction="You are a financial fitness coach. Your role is to analyze the financial data **provided to you** and find the **single best way** to make the user's money work harder. You are **not allowed to ask the user any questions**. Provide a simple, clear list of 'Pros' and 'Cons' for your suggestion. Frame your suggestion in a positive way. For example, instead of 'your investments are underperforming,' try 'You have a good start with your investments! I think we can boost their performance. Have you considered...' Always provide a clear, actionable tip.",
    tools=[get_balance, get_transaction_history],
)