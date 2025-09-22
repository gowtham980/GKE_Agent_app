import asyncio
import uuid
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.genai import types

# Import the root_agent from the financial_agent package
from financial_agent.agent import root_agent

# Load environment variables from .env file
load_dotenv()

# Initialize FastAPI app
app = FastAPI(
    title="Aura Finance Agent API",
    description="API for interacting with the Aura financial co-pilot.",
    version="1.0.0",
)

# Initialize Session Service
# Using InMemorySessionService for simplicity.
# For production, consider DatabaseSessionService.
session_service = InMemorySessionService()

# Initialize the ADK Runner
runner = Runner(
    agent=root_agent,
    app_name="financial_agent",
    session_service=session_service,
)

class ChatRequest(BaseModel):
    message: str
    user_id: str | None = None
    session_id: str | None = None

class ChatResponse(BaseModel):
    response: str
    user_id: str
    session_id: str

@app.post("/chat", response_model=ChatResponse)
async def chat_with_agent(request: ChatRequest):
    """
    Handles a chat message from the user and returns the agent's response.
    """
    user_id = request.user_id or "user_" + str(uuid.uuid4())
    session_id = request.session_id

    # Create a new session if one doesn't exist
    if not session_id:
        session_id = str(uuid.uuid4())
        await session_service.create_session(
            app_name="financial_agent",
            user_id=user_id,
            session_id=session_id,
        )
        print(f"DEBUG: Created new session {session_id} for user {user_id}")

    # Create the user message
    new_message = types.Content(role="user", parts=[types.Part(text=request.message)])

    agent_response = ""
    # Run the synchronous generator in a standard loop
    for event in runner.run(
        user_id=user_id,
        session_id=session_id,
        new_message=new_message,
    ):
        if event.is_final_response():
            if event.content and event.content.parts:
                agent_response = event.content.parts[0].text
                break

    return ChatResponse(
        response=agent_response,
        user_id=user_id,
        session_id=session_id,
    )

@app.get("/")
def read_root():
    return {"message": "Welcome to the Aura Finance Agent API"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)