from google.adk.agents import LlmAgent
from google.adk.tools import google_search

fact_checker_agent = LlmAgent(
    name="fact_checker_agent",
    model="gemini-2.5-flash",
    description="A fact-checker for financial tips.",
    instruction="You are a fact-checker. Your purpose is to verify the accuracy of a given financial statement or tip using a web search. Respond with whether the statement is accurate and provide a brief supporting explanation and source if possible.",
    tools=[google_search],
)