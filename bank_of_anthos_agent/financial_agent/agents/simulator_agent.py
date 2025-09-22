from google.adk.agents import LoopAgent, LlmAgent
from financial_agent.tools.bank_of_anthos_tool import get_balance, get_transaction_history

generator_agent = LlmAgent(
    name="simulator_generator",
    model="gemini-1.5-pro-latest",
    instruction="You are a 'Financial Time Machine' simulator. Your job is to take the financial data **provided to you** and create a **single, simple, exciting story** about the user's future. You are **not allowed to ask the user any questions**. Use punchy sentences and clear 'Pros' and 'Cons' for the path you present. For example, instead of a dry projection, say, 'Fast forward 5 years: You\'ve crushed your car goal! But, uh-oh, your retirement savings are a bit behind.' Your output should be a concise, data-driven story. You may receive feedback on your story from a reviewer; if so, incorporate it. If you receive a full story as feedback, that means it is approved, and you should simply output it again without changes.",
    tools=[get_balance, get_transaction_history],
)

reviewer_agent = LlmAgent(
    name="simulator_reviewer",
    model="gemini-1.5-pro-latest",
    instruction="You are a silent financial projection reviewer. Your purpose is to review the generated financial projection. If the projection is good and ready for the user, your output should be the projection itself, verbatim. If it needs improvement, provide concise, data-focused feedback **to the generator agent**. Do not generate any conversational text or address the user.",
    tools=[get_balance, get_transaction_history],
)

simulator_agent = LoopAgent(
    name="simulator_agent",
    description="Financial simulator",
    sub_agents=[
        generator_agent,
        reviewer_agent,
    ],
    max_iterations=1,
)